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

namespace SQLServer01
{
    public partial class frmVIPMembers : Form
    {
        private const string CONNECTION_STRING = ""; // const 상수는 대문자로 쓰는게 관례이다.
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public frmVIPMembers()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void frmVIPMembers_Load(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING); // 로딩되면서 커넥션 하는걸 가지고 온다.

            string query = "SELECT * FROM dbo.VIPmembers"; // @id는 부분만 가지고 오는 거고 WHERE를 지워서 전체가 출력되게 한다.
            SqlCommand cmd = SqlCon.CreateCommand(); // 바로 command객체를 만들어준다.
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain);

            grdMemberList.DataSource = dataMain.Tables[0]; // 테이블 0번을 바인딩해준다.
        }
    }
}
