using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Marketplace_project
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            SubMenus();
        }

        private void SubMenus()
        {
            panelSubMenu.Visible = false;
            panelSubMenuAccount.Visible = false;
        }
        private void ShowSubMenus(Panel sub)
        {
            if(sub.Visible==false)
            {
                sub.Visible = true;
                return;
            }
            sub.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e) //nft button
        {
            ShowSubMenus(panelSubMenu);
        }

        private void buttonAccount_Click(object sender, EventArgs e)
        {
            ShowSubMenus(panelSubMenuAccount);
        }
    }
}
