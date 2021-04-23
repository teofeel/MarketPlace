from web3 import Web3
import json

class User():
    def __init__(self, username, password, address, nfts):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))

        self.__username = username
        self.__password = password
        self.__address = address
        if(address == ""):
            self.__funds = 0
        else:
            self.__funds = self.__web3.fromWei(self.__web3.eth.getBalance(address), 'ether')

        self.__nfts = nfts

    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getAdress(self):
        return self.__address
    def getFunds(self):
        return self.__funds

    def getNFTS(self):
        return self.__nfts
    
    def setUsername(self, username):
        self.__username = username
    def setPassword(self, password):
        self.__password = password
    def setAddress(self, address):
        self.__address = address

    def add_nft(self, nft):
        #nft.setAdress(user.adress)
        self.__nfts.append(nft)
    
    def check_password_match(self, password):
        if self.__password == password:
            return True
        return False


    def update_username(self, username):
        with open("users.json", 'r+') as users_file:
            users_data = json.load(users_file)
            users_data[username] = users_data.pop(self.__username)

            self.setUsername(username)
            users_data[username]["username"] = self.__username

        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=2)
        

    def update_password(self, password):
        with open("users.json", 'r+') as users_file:
            users_data = json.load(users_file)
            users_data[self.__username]["password"] = password
            self.setPassword(password)

        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=2)

    def update_address(self, address):
        with open("users.json", 'r+') as users_file:
            users_data = json.load(users_file)
            users_data[self.__username]["address"] = address
            self.setAddress(address)

        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=2)


    def save_user(self): 
        user = {
            self.__username:{
                "username": self.__username,
                "password": self.__password,
                "address": self.__address,
                "funds": float(self.__funds),
                "nfts": self.__nfts
            }
        }

        with open('users.json', 'r+') as json_file: 
            data = json.load(json_file) 
            data.update(user)
            json_file.seek(0)
            json.dump(data, json_file)
    




