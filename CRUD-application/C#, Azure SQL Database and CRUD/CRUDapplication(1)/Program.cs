using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// 새로 추가한 것을 적어주기 위해서는 한 줄 띄워준다.
using System.Data.SqlClient;   // SqlClient를 사용한다.
using System.Data;

namespace CRUD_Sample1
{
    internal class Program  // 맴버 변수
    {
        private const string ConnectionString = "Server=tcp:labuser2sqlserver.database.windows.net,1433;Initial Catalog=labuser2sql;Persist Security Info=False;User ID=kcw0331;Password=Sa8o5m7x1!@;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"; // 연결문자열을 사용한다.
        // const로 해 놓아서 아래 SqlConnection이 된다.
        static void Main(string[] args) // 지역 변수
        {
            SqlConnection con = new SqlConnection(ConnectionString); // Connection객체를 사용한다. ConnectionString을 사용한다.
            SqlCommand cmd = con.CreateCommand(); // 커넥션 객체에 의해서 만들어 진다. 커맨드는 커넥션 객체에 종속적인 얘이다.
            IDataReader reader = null;

            // string query = "SELECT * FROM production.brands"; // 쿼리의 결과를 가져온다.
            // string query = "SELECT * FROM production.brands WHERE brand_id > 5"; // 조건에 맞는 것만 출력하게 해준다.
            string query = "SELECT * FROM production.brands WHERE brand_id > @id"; // @id라고해서 parameter로 처리를 해준다.
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value= 5; // 파라메타에 들어가는 값은 5
            // cmd.CommandText = query; // 명령어들을 여기에 셋팅한다.
            
            con.Open();
            Console.WriteLine("Database Connected!");
            reader = cmd.ExecuteReader(); // 실행결과가 reader객체로 떨어진다.

            while (reader.Read()) // 안에 있는 데이터를 읽어 들일때 사용한다.
            {
                Console.WriteLine("{0} - {1}", reader.GetInt32(0), reader.GetString(1)); // 읽어들인 첫번째 값이 0번에 들어간다., 두번째 값은 1번에 들어간다.
            }
         
            con.Close();
            Console.ReadLine(); // 우리가 엔터를 치기 전까지는 유지가 된다.
         }
    }
}
