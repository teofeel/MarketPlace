from web3 import Web3
import json

class User():
    def __init__(self, username, password, adress, nfts):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))

        self.__username = username
        self.__password = password
        self.__adress = adress
        if(adress == ""):
            self.__funds = 0
        else:
            self.__funds = self.__web3.fromWei(self.__web3.eth.getBalance(adress), 'ether')

        self.__nfts = nfts

    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getAdress(self):
        return 
    def getFunds(self):
        return self.__funds

    def getNFTS(self):
        return self.__nfts
    
    def setUsername(self, username):
        self.__username = username
    def setPassword(self, password):
        self.__password = password

    def add_nft(self, nft):
        #nft.setAdress(user.adress)
        self.__nfts.append(nft)
    
    def check_password_match(self, password):
        if self.__password == password:
            return True
        return False

    '''def save_user(self): 
        def write_json(data, filename='users.json'):
            with open(filename,'w') as f: 
                json.dump(data,f)
        
        user = {
            "username": self.__username,
            "password": self.__password,
            "adress": self.__adress,
            "funds": float(self.__funds),
            "nfts": self.__nfts,
            "cart": self.__cart
        }
        with open('users.json') as json_file: 
            data = json.load(json_file) 
            data[self.__username] = user
            write_json(data)'''
        
    def save_user(self): 
        user = {
            self.__username:{
                "username": self.__username,
                "password": self.__password,
                "adress": self.__adress,
                "funds": float(self.__funds),
                "nfts": self.__nfts
            }
        }

        with open('users.json', 'r+') as json_file: 
            data = json.load(json_file) 
            data.update(user)
            json_file.seek(0)
            json.dump(data, json_file)
    




