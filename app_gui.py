from flask import Flask
from flask import render_template
import json
from web3 import Web3
from transactions import Transaction

app = Flask(__name__)
infuria_url = "https://mainnet.infura.io/v3/639b3d222da343759f90819765eb6c55" #infura api to connect to eth blockchain network, if for real
ganache_url = "HTTP://127.0.0.1:7545" #'local' eth network

users = []
nfts = []

@app.route('/')
def home():
    return render_template('home.html')

'''@app.route('/login')
def login():

@app.route('/register')
def register():

@app.route('/photo_nfts')
def photo_nfts():

@app.route('/video_nfts')
def video_nfts():

@app.route('/gif_nfts')
def gif_nfts():'''

app.run()




