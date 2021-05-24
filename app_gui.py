from flask import Flask, request, render_template, session, redirect, url_for, Blueprint
import json
from web3 import Web3
from transactions import Transaction
from user import User
import os
from nft import NFT 
#from brownie import nft

app = Flask(__name__)

infuria_url = "https://mainnet.infura.io/v3/639b3d222da343759f90819765eb6c55" #infura api to connect to eth blockchain network, if for real
ganache_url = "HTTP://127.0.0.1:7545" #'local' eth network
web3 = Web3(Web3.HTTPProvider(ganache_url))


users = []
nfts = []
current_user = User("","","",[]) #user that is currently logged in

def load_users(users):
    users_file = open("users.json")
    users_data = json.load(users_file)

    for u in users_data:
        nfts = []

        for acc in users_data[u]["nfts"]:
            nfts.append(acc)

        users.append(User(users_data[u]["username"], users_data[u]["password"],users_data[u]["address"], nfts)) 

def load_nfts(nfts):
    nfts_file = open("nfts.json")
    nfts_data = json.load(nfts_file)

    for u in nfts_data:
        nfts.append(NFT(nfts_data[u]["id"], nfts_data[u]["type"],nfts_data[u]["cover"], nfts_data[u]["name"],nfts_data[u]["description"], nfts_data[u]["price"], nfts_data[u]["owner"])) 

def login_func(username, password):
    global current_user

    for user in users:
        if username == user.getUsername() and user.check_password_match(password):
            current_user = user
            return True
    return False

def check_existing_username(username):
    for user in users:
        if username == user.getUsername():
            return False
    return True

def address_valid(address):
    if web3.isAddress(address):
        return True
    return False

def register_func(username, password, conf_pass, address):
    if password != conf_pass:
        return 1
    elif not check_existing_username(username):
        return 2
    elif not address_valid(address):
        return 3
    else:
        u = User(username, password, address, [])
        u.save_user()
        return 4

def username_valid(username):
    users_file = open("users.json")
    users_data = json.load(users_file)

    try:
        users_data[username]
        return False
    except:
        return True

def confirm_change_password(old_password, new_password, conf_password):
    global current_user

    if current_user.getPassword()==old_password:
        if new_password == conf_password:
            current_user.update_password(new_password)
            return True
        else:
             return False
    return False

@app.route('/')
def home():
    if current_user.getUsername()!="":
        return render_template('home.html', logged_in=True)

    return render_template('home.html')

@app.route('/logout')
def logout():
    global current_user
    current_user = User("","","",[])  
      
    return home()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if login_func(username, password): 
            return home()
        return render_template("login.html", content = "Username or password not matching. Try again")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="GET":
        return render_template("register.html")
    
    if request.method == "POST":
        global current_user
        username = request.form.get("username")
        password = request.form.get("password")
        conf_pass = request.form.get("confirm_password")
        adress = request.form.get("wallet_address")

        if register_func(username, password, conf_pass, adress)==4:
            current_user = User(username,password,adress,[])
            return home()

        elif register_func(username, password, conf_pass, adress)==3:
            return render_template("register.html", content="Wallet adress is not valid")

        elif register_func(username, password, conf_pass, adress)==2:
            return render_template("register.html", content="Username already exists")

        elif register_func(username, password, conf_pass, adress)==1:
            return render_template("register.html", content="Passwords don't match")
        else:
            return render_template("register.html", content="Uknown error")


@app.route('/nfts')
def artwork():
    if current_user.getUsername()!="":
        return render_template("nfts.html", nft = nfts, logged_in=True)

    return render_template("nfts.html", nft = nfts)

'''@app.route('/nfts', methods=['GET', 'POST'])
def choosen_nft():
    if request.method=='post':
        if current_user.getUsername()!="":
            return render_template('nftID.html', logged_in=True) 
        return render_template('nftID.html')'''

@app.route('/account')
def account():
    return render_template('account.html', user = current_user, nft=nfts, logged_in=True)

@app.route('/settings')
def settings():
    return render_template('account-settings.html', logged_in=True)
    

@app.route('/changeUsername', methods=['GET', 'POST'])
def changeUsername(): 
    if request.method == 'GET':
        return render_template('change-username.html', logged_in=True)
    else:
        global current_user
        username = request.form.get("username")

        if username_valid(username):
            current_user.update_username(username) 
            current_user.setUsername(username)
            return settings()

@app.route('/changePassword', methods=['GET', 'POST'])
def changePassword(): 
    if request.method == 'GET':
        return render_template('change-password.html', logged_in=True)
    else:
        global current_user
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        conf_password = request.form.get("confirm_password")

        if confirm_change_password(old_password, new_password, conf_password):
            return settings()

@app.route('/changeAddress', methods=['GET', 'POST'])
def changeAddress(): 
    if request.method == 'GET':
        return render_template('change-address.html', logged_in=True)
    else:
        global current_user
        address = request.form.get("address")
        if address_valid(address):
            current_user.update_address(address)
            current_user.setAddress(address)
            return settings()
    
@app.route('/nftID/<ID>')
def nft(ID):
    for i in nfts:
        if int(ID) == i.getID():
            if current_user.getUsername() != "":
                return render_template("nftID.html", NFT=i, logged_in=True)
            return render_template('nftID.html', NFT=i)

@app.route('/buy-nft/<ID>')
def buy_nft(ID):
    for i in nfts:
        if int(ID) == i.getID():
            if current_user.getUsername()!="":
                return render_template('buy-nft.html', nft=i,logged_in=True)
            return login()

@app.route('/buy', methods=['POST'])
def buy():
    ID = request.form.get("id")
    print(ID)
    if current_user.getUsername()=="":
        return login()
    for i in nfts:
        print(ID)
        if ID == i.getID():
            print('ovde si')
            transaction = Transaction(current_user.getAdress(), i.getAdress(), i.getPrice())
            transaction.send_transaction(request.form.get("private_key"))
            transaction.save_transaction()
            return account()
    return home()

    


load_users(users)
load_nfts(nfts)

app.run(debug=True)








