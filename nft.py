from web3 import Web3
import json

class NFT:
    def __init__(self, iid, tipe,cover, name, desctiption, price, owner_adress):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))
        
        self.__id = iid
        self.__type = tipe
        self.__cover = cover
        self.__name = name
        self.__description = desctiption
        self.__price = price
        self.__owner = owner_adress

    def getOwner(self):
        users_file = open("users.json")
        users_data = json.load(users_file)

        for u in users_data:
            if self.__owner == users_data[u]['adress']:
                return users_data[u]['username']
                
    def getPrice(self):
        return self.__price
    def getName(self):
        return self.__name
    def getCover(self):
        return self.__cover


    


