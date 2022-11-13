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
using System.Configuration;

namespace SQLServer01
{
    public partial class frmVIPMembers : Form
    {
        private string connection_string = ""; // 변수라서 소문자로 고친다.
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public frmVIPMembers()
        {
            InitializeComponent(); // 생성자
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void frmVIPMembers_Load(object sender, EventArgs e)
        {
            connection_string = ConfigurationManager.AppSettings["connection_string"];
            ReloadData();
        }

        public void ReloadData() // public으로 만들면 다른곳에서 불러올 수 있다.
        {
            dataMain.Clear(); // 시작하기 전에 데이터 메인을 지워준다.

            SqlCon = new SqlConnection(connection_string); // 로딩되면서 커넥션 하는걸 가지고 온다.

            string query = "SELECT * FROM dbo.VIPmembers"; // @id는 부분만 가지고 오는 거고 WHERE를 지워서 전체가 출력되게 한다.
            SqlCommand cmd = SqlCon.CreateCommand(); // 바로 command객체를 만들어준다.
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain);

            grdMemberList.DataSource = dataMain.Tables[0]; // 테이블 0번을 바인딩해준다.
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            frmVIPMembersInput vipInput = new frmVIPMembersInput(this);
            vipInput.ShowDialog(); // 이 코드 작성후 실행하면 새로운 화면이 띄워진다.
        }
    }
}
