namespace Marketplace_project
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panelSideMenu = new System.Windows.Forms.Panel();
            this.panelLogo = new System.Windows.Forms.Panel();
            this.buttonNFT = new System.Windows.Forms.Button();
            this.panelSubMenu = new System.Windows.Forms.Panel();
            this.buttonNFTArt = new System.Windows.Forms.Button();
            this.button3NFTCards = new System.Windows.Forms.Button();
            this.buttonNFTVideos = new System.Windows.Forms.Button();
            this.panelMainMenu = new System.Windows.Forms.Panel();
            this.pictureBoxLogo = new System.Windows.Forms.PictureBox();
            this.buttonHome = new System.Windows.Forms.Button();
            this.buttonAbout = new System.Windows.Forms.Button();
            this.buttonAccount = new System.Windows.Forms.Button();
            this.panelSubMenuAccount = new System.Windows.Forms.Panel();
            this.buttonLogin = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.panelSideMenu.SuspendLayout();
            this.panelLogo.SuspendLayout();
            this.panelSubMenu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxLogo)).BeginInit();
            this.panelSubMenuAccount.SuspendLayout();
            this.SuspendLayout();
            // 
            // panelSideMenu
            // 
            this.panelSideMenu.AutoScroll = true;
            this.panelSideMenu.BackColor = System.Drawing.Color.DimGray;
            this.panelSideMenu.Controls.Add(this.panelSubMenuAccount);
            this.panelSideMenu.Controls.Add(this.buttonAccount);
            this.panelSideMenu.Controls.Add(this.buttonAbout);
            this.panelSideMenu.Controls.Add(this.buttonHome);
            this.panelSideMenu.Controls.Add(this.panelSubMenu);
            this.panelSideMenu.Controls.Add(this.buttonNFT);
            this.panelSideMenu.Controls.Add(this.panelLogo);
            this.panelSideMenu.Dock = System.Windows.Forms.DockStyle.Left;
            this.panelSideMenu.Location = new System.Drawing.Point(0, 0);
            this.panelSideMenu.Name = "panelSideMenu";
            this.panelSideMenu.Size = new System.Drawing.Size(249, 570);
            this.panelSideMenu.TabIndex = 0;
            // 
            // panelLogo
            // 
            this.panelLogo.Controls.Add(this.pictureBoxLogo);
            this.panelLogo.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelLogo.Location = new System.Drawing.Point(0, 0);
            this.panelLogo.Name = "panelLogo";
            this.panelLogo.Size = new System.Drawing.Size(249, 105);
            this.panelLogo.TabIndex = 1;
            // 
            // buttonNFT
            // 
            this.buttonNFT.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonNFT.FlatAppearance.BorderSize = 0;
            this.buttonNFT.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonNFT.ForeColor = System.Drawing.Color.White;
            this.buttonNFT.Location = new System.Drawing.Point(0, 105);
            this.buttonNFT.Name = "buttonNFT";
            this.buttonNFT.Padding = new System.Windows.Forms.Padding(15, 0, 0, 0);
            this.buttonNFT.Size = new System.Drawing.Size(249, 45);
            this.buttonNFT.TabIndex = 1;
            this.buttonNFT.Text = "NFTs";
            this.buttonNFT.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonNFT.UseVisualStyleBackColor = true;
            this.buttonNFT.Click += new System.EventHandler(this.button1_Click);
            // 
            // panelSubMenu
            // 
            this.panelSubMenu.BackColor = System.Drawing.Color.Maroon;
            this.panelSubMenu.Controls.Add(this.buttonNFTVideos);
            this.panelSubMenu.Controls.Add(this.button3NFTCards);
            this.panelSubMenu.Controls.Add(this.buttonNFTArt);
            this.panelSubMenu.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelSubMenu.Location = new System.Drawing.Point(0, 150);
            this.panelSubMenu.Name = "panelSubMenu";
            this.panelSubMenu.Size = new System.Drawing.Size(249, 120);
            this.panelSubMenu.TabIndex = 1;
            // 
            // buttonNFTArt
            // 
            this.buttonNFTArt.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonNFTArt.FlatAppearance.BorderSize = 0;
            this.buttonNFTArt.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonNFTArt.ForeColor = System.Drawing.SystemColors.ControlLight;
            this.buttonNFTArt.Location = new System.Drawing.Point(0, 0);
            this.buttonNFTArt.Name = "buttonNFTArt";
            this.buttonNFTArt.Padding = new System.Windows.Forms.Padding(35, 0, 0, 0);
            this.buttonNFTArt.Size = new System.Drawing.Size(249, 40);
            this.buttonNFTArt.TabIndex = 1;
            this.buttonNFTArt.Text = "Art";
            this.buttonNFTArt.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonNFTArt.UseVisualStyleBackColor = true;
            // 
            // button3NFTCards
            // 
            this.button3NFTCards.Dock = System.Windows.Forms.DockStyle.Top;
            this.button3NFTCards.FlatAppearance.BorderSize = 0;
            this.button3NFTCards.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button3NFTCards.ForeColor = System.Drawing.SystemColors.ControlLight;
            this.button3NFTCards.Location = new System.Drawing.Point(0, 40);
            this.button3NFTCards.Name = "button3NFTCards";
            this.button3NFTCards.Padding = new System.Windows.Forms.Padding(35, 0, 0, 0);
            this.button3NFTCards.Size = new System.Drawing.Size(249, 40);
            this.button3NFTCards.TabIndex = 2;
            this.button3NFTCards.Text = "Trading Cards";
            this.button3NFTCards.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.button3NFTCards.UseVisualStyleBackColor = true;
            // 
            // buttonNFTVideos
            // 
            this.buttonNFTVideos.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonNFTVideos.FlatAppearance.BorderSize = 0;
            this.buttonNFTVideos.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonNFTVideos.ForeColor = System.Drawing.SystemColors.ControlLight;
            this.buttonNFTVideos.Location = new System.Drawing.Point(0, 80);
            this.buttonNFTVideos.Name = "buttonNFTVideos";
            this.buttonNFTVideos.Padding = new System.Windows.Forms.Padding(35, 0, 0, 0);
            this.buttonNFTVideos.Size = new System.Drawing.Size(249, 40);
            this.buttonNFTVideos.TabIndex = 3;
            this.buttonNFTVideos.Text = "Videos";
            this.buttonNFTVideos.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonNFTVideos.UseVisualStyleBackColor = true;
            // 
            // panelMainMenu
            // 
            this.panelMainMenu.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.panelMainMenu.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelMainMenu.Location = new System.Drawing.Point(249, 0);
            this.panelMainMenu.Name = "panelMainMenu";
            this.panelMainMenu.Size = new System.Drawing.Size(662, 570);
            this.panelMainMenu.TabIndex = 1;
            // 
            // pictureBoxLogo
            // 
            this.pictureBoxLogo.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBoxLogo.Location = new System.Drawing.Point(0, 0);
            this.pictureBoxLogo.Name = "pictureBoxLogo";
            this.pictureBoxLogo.Size = new System.Drawing.Size(249, 105);
            this.pictureBoxLogo.TabIndex = 0;
            this.pictureBoxLogo.TabStop = false;
            // 
            // buttonHome
            // 
            this.buttonHome.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonHome.FlatAppearance.BorderSize = 0;
            this.buttonHome.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonHome.ForeColor = System.Drawing.Color.White;
            this.buttonHome.Location = new System.Drawing.Point(0, 270);
            this.buttonHome.Name = "buttonHome";
            this.buttonHome.Padding = new System.Windows.Forms.Padding(15, 0, 0, 0);
            this.buttonHome.Size = new System.Drawing.Size(249, 45);
            this.buttonHome.TabIndex = 0;
            this.buttonHome.Text = "Home";
            this.buttonHome.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonHome.UseVisualStyleBackColor = true;
            // 
            // buttonAbout
            // 
            this.buttonAbout.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonAbout.FlatAppearance.BorderSize = 0;
            this.buttonAbout.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonAbout.ForeColor = System.Drawing.SystemColors.Control;
            this.buttonAbout.Location = new System.Drawing.Point(0, 315);
            this.buttonAbout.Name = "buttonAbout";
            this.buttonAbout.Padding = new System.Windows.Forms.Padding(15, 0, 0, 0);
            this.buttonAbout.Size = new System.Drawing.Size(249, 45);
            this.buttonAbout.TabIndex = 0;
            this.buttonAbout.Text = "About";
            this.buttonAbout.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonAbout.UseVisualStyleBackColor = true;
            // 
            // buttonAccount
            // 
            this.buttonAccount.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonAccount.FlatAppearance.BorderSize = 0;
            this.buttonAccount.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonAccount.ForeColor = System.Drawing.SystemColors.Control;
            this.buttonAccount.Location = new System.Drawing.Point(0, 360);
            this.buttonAccount.Name = "buttonAccount";
            this.buttonAccount.Padding = new System.Windows.Forms.Padding(15, 0, 0, 0);
            this.buttonAccount.Size = new System.Drawing.Size(249, 45);
            this.buttonAccount.TabIndex = 0;
            this.buttonAccount.Text = "Account";
            this.buttonAccount.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonAccount.UseVisualStyleBackColor = true;
            this.buttonAccount.Click += new System.EventHandler(this.buttonAccount_Click);
            // 
            // panelSubMenuAccount
            // 
            this.panelSubMenuAccount.BackColor = System.Drawing.Color.Maroon;
            this.panelSubMenuAccount.Controls.Add(this.button1);
            this.panelSubMenuAccount.Controls.Add(this.buttonLogin);
            this.panelSubMenuAccount.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelSubMenuAccount.Location = new System.Drawing.Point(0, 405);
            this.panelSubMenuAccount.Name = "panelSubMenuAccount";
            this.panelSubMenuAccount.Size = new System.Drawing.Size(249, 80);
            this.panelSubMenuAccount.TabIndex = 0;
            // 
            // buttonLogin
            // 
            this.buttonLogin.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonLogin.FlatAppearance.BorderSize = 0;
            this.buttonLogin.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonLogin.ForeColor = System.Drawing.SystemColors.Control;
            this.buttonLogin.Location = new System.Drawing.Point(0, 0);
            this.buttonLogin.Name = "buttonLogin";
            this.buttonLogin.Padding = new System.Windows.Forms.Padding(30, 0, 0, 0);
            this.buttonLogin.Size = new System.Drawing.Size(249, 40);
            this.buttonLogin.TabIndex = 0;
            this.buttonLogin.Text = "Login";
            this.buttonLogin.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonLogin.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            this.button1.Dock = System.Windows.Forms.DockStyle.Top;
            this.button1.FlatAppearance.BorderSize = 0;
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.ForeColor = System.Drawing.SystemColors.Control;
            this.button1.Location = new System.Drawing.Point(0, 40);
            this.button1.Name = "button1";
            this.button1.Padding = new System.Windows.Forms.Padding(30, 0, 0, 0);
            this.button1.Size = new System.Drawing.Size(249, 40);
            this.button1.TabIndex = 1;
            this.button1.Text = "Register";
            this.button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.button1.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(911, 570);
            this.Controls.Add(this.panelMainMenu);
            this.Controls.Add(this.panelSideMenu);
            this.Name = "Form1";
            this.Text = "Form1";
            this.panelSideMenu.ResumeLayout(false);
            this.panelLogo.ResumeLayout(false);
            this.panelSubMenu.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxLogo)).EndInit();
            this.panelSubMenuAccount.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panelSideMenu;
        private System.Windows.Forms.Panel panelSubMenu;
        private System.Windows.Forms.Button buttonNFTVideos;
        private System.Windows.Forms.Button button3NFTCards;
        private System.Windows.Forms.Button buttonNFTArt;
        private System.Windows.Forms.Button buttonNFT;
        private System.Windows.Forms.Panel panelLogo;
        private System.Windows.Forms.PictureBox pictureBoxLogo;
        private System.Windows.Forms.Panel panelMainMenu;
        private System.Windows.Forms.Button buttonHome;
        private System.Windows.Forms.Panel panelSubMenuAccount;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button buttonLogin;
        private System.Windows.Forms.Button buttonAccount;
        private System.Windows.Forms.Button buttonAbout;
    }
}

