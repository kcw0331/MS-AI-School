using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IoTClient
{
    internal class DummySensor
    {
        private Random _Random = new Random(); /* 랜덤 클래스를 추가를 하였다. */
        public WeatherModel GetWeatherModel(string deviceID)
        {
            var model = new WeatherModel(); /* 사용자가 디바이스 1을 주면 웨더 모델을 만들고 클래스를 만드는 것을 한다. */
            model.DeviceID = deviceID;
            model.Temperature = _Random.Next(20, 35); /* 랜던값으로 20에서 35사이의 값을 생성해서 넣어준다. */
            model.Humidity = _Random.Next(40, 80);
            model.Dust = model.Temperature + 50 + _Random.Next(1,5); /* 오차가 1에서 5가된다. */

            return model; /* 모델 리턴을 하면 값이 나오게 된다. */
        }
    }
}
