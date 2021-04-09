from web3 import Web3
import json
from datetime import datetime

class Transaction(): #this works
    def __init__(self, buyer, seller, value):
        ganache_url = "HTTP://127.0.0.1:7545" #ganache url, don't want to spend my money on gas fees

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))
        self.__buyer = buyer
        self.__seller = seller
        self.__value = value

        nonce = self.__web3.eth.getTransactionCount(self.__buyer)
        self.__tx = {
            'nonce': nonce,
            'to': self.__seller,
            'value': self.__web3.toWei(self.__value, 'ether'),
            'gas': 2000000, #gas limit
            'gasPrice': self.__web3.toWei('50', 'gwei')
        }

    def send_transaction(self, private_key):
        signed_tx = self.__web3.eth.account.signTransaction(self.__tx, private_key)
        self.__web3.eth.sendRawTransaction(signed_tx.rawTransaction) 

    '''def update_database(user):
        with open('users.json') as json_file: 
            data = json.load(json_file) 
            temp = data['users'] 
            temp.append(user)
            write_json(data)'''

    def save_transaction(self): 
        def write_json(data, filename='transactions.json'):
            with open(filename,'w') as f: 
                json.dump(data,f)
        
        transaction = {
            "buyer": self.__buyer,
            "seller": self.__seller,
            "value": self.__value,
            "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        with open('transactions.json') as json_file: 
            data = json.load(json_file) 
            temp = data['transactions'] 
            temp.append(transaction)
            write_json(data)
       
        

