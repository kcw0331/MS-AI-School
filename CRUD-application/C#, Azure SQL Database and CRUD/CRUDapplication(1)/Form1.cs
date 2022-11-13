using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Collections;


namespace SQLServer01
{
    public partial class frmMain : Form
    {
        private const string CONNECTION_STRING = "Server=tcp:labuser2sqlserver.database.windows.net,1433;Initial Catalog=labuser2sql;Persist Security Info=False;User ID=kcw0331;Password=Sa8o5m7x1!@;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"; // const 상수는 대문자로 쓰는게 관례이다.
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter(); // Sql 어댑트를 만들어 준다.

        private DataSet dataMain = new DataSet();
        public frmMain()
        {
            InitializeComponent();
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING);  // 클릭을 하면 데이터 베이스에 연결하도록 해준다.
            btnConnect.Enabled = false;
        }

        private void btnGetData_Click(object sender, EventArgs e)
        {
            // 기존에 만들었던 부분을 가지고 온다.
            // string query = "SELECT * FROM production.brands WHERE brand_id > @id";
            string query = "SELECT * FROM production.brands"; // @id는 부분만 가지고 오는 거고 WHERE를 지워서 전체가 출력되게 한다.
            SqlCommand cmd = SqlCon.CreateCommand(); // 바로 command객체를 만들어준다.
            cmd.CommandText = query;
            // cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value = 5;// 데이터를 가지고 와서 채워주는 것까지 끝나게 된다.

            SqlApt.SelectCommand =cmd;
            SqlApt.Fill(dataMain);

            lstBrends.Items.Clear(); // 가지고 왔을 때, 새로 비워주고 추가해준다.

            DataRowCollection dataRows = dataMain.Tables[0].Rows; //테이블 복수로 되어 있어서 여러개로 되어있다./ Rows를 사용해서 컬렉션을 가져온다.

            for (int i = 0;i<dataRows.Count;i++)
            {
                lstBrends.Items.Add(dataRows[i][1].ToString()); // 컬럼을 1로 지정해준다.
            }

            // lstBrends.Items.Add("Test"); // 글자도 object이다.

            btnGetData.Enabled = false; // 버튼을 사용하고 나서 필요없으면 false로 해준다.
        }

        private void lstBrends_SelectedIndexChanged(object sender, EventArgs e) // 얘를 이벤트 핸들러라고 부른다.
        {
            if(lstBrends.SelectedIndex == -1) // 선택되어 있는 index의 값이다., -1이면 선택이 되어있지 않은 것이다.
            {
                // MessageBox.Show("test");
                return; // 선택하지 않으면 아무것도 선택하지 않는다.
            }

            // Fill to DataGridView
            int selectedIndex = lstBrends.SelectedIndex; // 인덱스에 해당하는 값을 가지고 온다.
            int selectedBrandId = Int32.Parse(dataMain.Tables[0].Rows[selectedIndex][0].ToString()); // 0번째 항목을 가지고 온다.
            DataSet dataProducts = new DataSet();
            string query = "SELECT * FROM production.products WHERE brand_id = @brand_id"; // query를 임시로 사용한다.
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.Parameters.Add(new SqlParameter("@brand_id", SqlDbType.Int)).Value = selectedBrandId;
            cmd.CommandText = query; // 아이템을 선택할때 마다 내용들을 채워준다.
            SqlApt.SelectCommand = cmd; // 새로만든 cmd객체가 어댑터 객체에 반응하게 만들어 줘야 한다.
            SqlApt.Fill(dataProducts);
            grdProducts.DataSource = dataProducts.Tables[0]; // 첫번째 테이블에 있는 것을 바인딩 시켜준다.
            //grdProducts.DataBindings();
        }

        private void btnVIPmembers_Click(object sender, EventArgs e)
        {
            frmVIPMembers vip = new frmVIPMembers(); // 새로운 객체를 만들어준다.
            vip.ShowDialog(); // ShowDialog이거는 이창이 끝나기 전에 다른창을 선택할 수 없게 한다.
        }
    }
}
