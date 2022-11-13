using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Configuration;
using System.Data.SqlClient;

namespace SQLServer01
{
    public partial class frmVIPMembersInput : Form
    {
        private string CONNECTION_STRING; // 변수를 선언해 놓는다. //OK를 누르면 커넥션 스트링을 가져오는 걸 해본다.
        private frmVIPMembers frm_vip_members; // 이런이름으로 정의한다.
        public frmVIPMembersInput(frmVIPMembers vipmembers)  // vipmembers로 받겠다는 것이다.
        {
            InitializeComponent();

            frm_vip_members= vipmembers; // 자기자산에 넘겨받은 것을 세팅해준다.
        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            if (txtName.Text.Trim().Length == 0) // 텍스트 박스에 내용이 비어 있으면 안된다./trim을 해주면 공백을 제거해준다.
            {
                MessageBox.Show("Please input VIP name!", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Error); //메세지를 뿌려준다./ 원하는 버튼 타입은 MessageBoxIcon여기에 있다.
                return;
            }

            CONNECTION_STRING = ConfigurationManager.AppSettings["connection_string"]; // 이렇게 해서 커넥션 스트링을 가져온다.
            // MessageBox.Show(CONNECTION_STRING);
            string query = "INSERT INTO dbo.VIPmembers(member_name, member_email, member_phone) VALUES(@name, @email, @phone)";

            SqlConnection con = new SqlConnection(CONNECTION_STRING);
            SqlCommand cmd = con.CreateCommand();
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.VarChar, 200)).Value = txtName.Text; // 200자가 넘어가면 잘라버린다.
            cmd.Parameters.Add(new SqlParameter("@email", SqlDbType.VarChar, 100)).Value = txtEmail.Text;
            cmd.Parameters.Add(new SqlParameter("@phone", SqlDbType.VarChar, 25)).Value = txtPhone.Text;

            con.Open(); // 쿼리를 실행할때 열고
            cmd.ExecuteNonQuery(); // 쿼리를 실행시키고 결과를 리턴시키지 않는 것이다.
            con.Close(); // 끝나면 닫아준다.

            frm_vip_members.ReloadData(); // 리플레이스 해주고 이상이 없으면 닫아준다.

            this.Close();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            if(txtName.Text.Trim().Length != 0) // 입력한게 있는데 취소를 할 경우 한번더 물어보는 if문이다.
            {
               var buttonResult =  MessageBox.Show("Close rigth now?", "Close", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
               if (buttonResult == DialogResult.No)
                {
                    return; // NO라고 하면 바로 return을 해준다.
                }
            }
            this.Close(); // 바로 닫아버리게 된다.
        }
    }
}
