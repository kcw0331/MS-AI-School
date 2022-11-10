using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mail;
using System.Net.NetworkInformation;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

using System.Timers;
using Microsoft.Azure.Devices.Client;
using Newtonsoft; /* 제이쓴 페키지를 사용한다. */

namespace IoTClient
{
    internal class Program
    {
        private static System.Timers.Timer SensorTimer;   /*참조할 거는 여기에 쓴다, 시간만 되면 만들어지는 객체를 만들었다.*/
        private const string DeviceConnectionString = "HostName=labuser2iot.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=yoZfxsINLSJcHw6gnSFHWMivy4Yhd6f8DxtPUjD3Xig=";
        private const string DeviceID = "Device1";  /*Device1로 설정해준다.*/
        private static DeviceClient SensorDevice = null; /*IoT와 연결할 수 있는 객체이다.*/
        private static DummySensor DummySensor = new DummySensor(); /* 더미센서는 하나 생성한다. */
        static void Main(string[] args) /*프로그램이 시작되는 부분이다.*/
        {
            SetTimer(); /*셋타이머를 호출해준다.*/

            SensorDevice = DeviceClient.CreateFromConnectionString(DeviceConnectionString, DeviceID); /* 디바이스 객체를 생성한다. DeviceID 해당되는 것을 가지고 온다.*/

            if(SensorDevice == null) /* null이라면 연결이 안된 거다.*/
            {
                Console.WriteLine("Failed to create DeviceClient!!");
                SensorTimer.Stop();

            }
            Console.WriteLine("\nPress Enter Key to exit the application...\n"); /*엔터를 누르게 되면 프로그램이 종료가 된다는 것이다.*/
            Console.WriteLine("The application started at {0:HH:mm:ss.fff}", DateTime.Now);
            Console.ReadLine(); /*여기에서 프로그램이 종료가 되지 않고 가만히 있게 한다.*/
            SensorTimer.Stop(); /*센서타이머를 스탑시킨다.*/
            SensorTimer.Dispose(); /*메모리에서 곧 죽을 놈이라고 붙여주는 것이다. 그럼 명시시켜준 것 부터 없애준다.*/
        }
        private static void SetTimer()
        {
            SensorTimer = new System.Timers.Timer(2000); /*2000이라고 하면 2초에 한번씩 타이머가 발생이 된다. 2초에 한번씩 IoT로 데이터를 쏜다.*/
            SensorTimer.Elapsed += SensorTimer_Elapsed; /*번개 마크가 이벤트이다., 델리게이터를 만든다.*/
            SensorTimer.AutoReset = true;
            SensorTimer.Enabled = true;
        }/*메소드를 여기에다가 쓴다. 새로운 타이머하나를 만든다.*/

        private static async void SensorTimer_Elapsed(object sender, ElapsedEventArgs e)
        {
            /*throw new NotImplementedException(); 여기가 2초에 한번씩 실행이 된다. 여기오면 이 안에 구현이 되지 않았다는 것을 말 한다.*/
            Console.WriteLine("The Elapsed event was raised at {0:HH:mm:ss.fff}", e.SignalTime); /*2초에 한번씩 쓰는것을 해본다. SignalTime이 넘어가서 정확하게 출력이 된다.*/
            await SendEvent(); // 네트워크로 전송하는 얘이다. 그리고 비동기를 호출할 때는 awiat를 해줘야한다.
            await ReceiveCommands(); // 2초마다 한번씩 보내는 것과 받는것를 동시에 해준다.
        }

        private static async Task SendEvent() // async는 비 동기화로 작동되는 얘이다. 그리고 Task로 해야한다.
        {
            WeatherModel model = DummySensor.GetWeatherModel(DeviceID);

            string json = Newtonsoft.Json.JsonConvert.SerializeObject(model); /* SerializeObject이거는 메모리상에 있는 클래스 모델이다. */

            Console.WriteLine(json);

            Message message = new Message(Encoding.UTF8.GetBytes(json));    //데이터를 보내기 위해서 메세지를 쓴다
            await SensorDevice.SendEventAsync(message);   //여기에 넣으면 바로 동작이 된다. 그리고 비동기형으로 실행할 때는 await을 써줘야 한다.
        }

        private static async Task ReceiveCommands() // 선생님이 주신거 붙여넣기를 하였다. 클라우드쪽에서 어떤게 들어오는지 체크하는 것이다.
        {
            Message receivedMessage;
            string messageData;

            receivedMessage = await SensorDevice.ReceiveAsync(TimeSpan.FromSeconds(1));

            if (receivedMessage != null)
            {
                messageData = Encoding.ASCII.GetString(receivedMessage.GetBytes());
                Console.WriteLine("\t{0}> Received message: {1}", DateTime.Now.ToLocalTime(), messageData);

                await SensorDevice.CompleteAsync(receivedMessage);
            }
        }
    }
}
