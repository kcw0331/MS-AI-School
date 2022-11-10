using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IoTClient
{
    internal class WeatherModel
    {
        public string DeviceID {  get; set; } /* 하나의 자료구조가 만들어진다. */
        public int Temperature { get; set; }
        public int Humidity { get; set; }
        public int Dust { get; set; } /* weather 모델이라는 자료구조를 만든 것이다. */
    }
}
