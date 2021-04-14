from web3 import Web3
import json

class NFT:
    def __init__(self, iid, tipe, name, desctiption, price, owner_adress):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))
        
        self.__id = iid
        self.__type = tipe
        self.__name = name
        self.__description = desctiption
        self.__price = price
        self.__owner = owner_adress

    def ownerOF(self):
        return self.__owner
    
    
    def transfer(self, adressTo):

    def takeownership(self):

    


