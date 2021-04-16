from flask import Flask, request, render_template, session, redirect, url_for
import json
from web3 import Web3
from transactions import Transaction
from user import User
import os
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

        users.append(User(users_data[u]["username"], users_data[u]["password"],users_data[u]["adress"], nfts)) 

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

def adress_valid(address):
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

@app.route('/')
def home():
    if current_user.getUsername()!="":
        return render_template('home.html', logged_in=True)
        
    return render_template('home.html')
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if login_func(username, password): 
            return home()
        
    return render_template("login.html", content = "Username or password not matching. Try again")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register', methods=['GET','POST'])
def register_user():
    global current_user
    if request.method == "POST":
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

    return render_template("register.html", content="Uknown error")

@app.route('/nfts')
def artwork():
    return render_template("nfts.html")

@app.route('/nfts', methods=['GET', 'POST'])
def choosen_nft():
    if request.method=='post':
        return render_template('nftID.html') #treba ubaciti podatke na tu stranicu (slika, naziv, cena.....)

load_users(users)
app.run()







