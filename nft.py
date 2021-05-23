from eth_account import Account
from web3 import Web3, HTTPProvider
import json
from solc import compile_source, compile_standard

class NFT:
    def __init__(self, iid, tipe,cover, name, description, price, owner_adress):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))
        #self.__web3.eth.default_account = owner_adress

        self.__id = iid
        self.__type = tipe
        self.__cover = cover
        self.__name = name
        self.__description = description
        self.__price = price
        self.__owner = owner_adress

        '''self.__contractSourceCode=compile_standard({
            "language": "Solidity",
            "sources": {"NFT.sol"},
            "settings":{
                "outputSelection": {
                    "*": {
                        "*": [
                            "metadata", "evm.bytecode"
                            , "evm.bytecode.sourceMap"
                        ]
                    }
                }
            }
        })'''#ovo ne radi

    def deployContract(self, privateKey):
        bytecode = compiled_sol['contracts']['NFT.sol']['NFT']['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts']['NFT.sol']['NFT']['metadata'])['output']['abi']

        nft = self.__web3.eth.contract(abi=abi,bytecode=bytecode)
        tx_hash = nft.constructor(self.__name, self.__id).transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    def getOwner(self):
        users_file = open("users.json")
        users_data = json.load(users_file)

        for u in users_data:
            if self.__owner == users_data[u]['address']:
                return users_data[u]['username']
                
    def getPrice(self):
        return self.__price

    def getName(self):
        return self.__name

    def getCover(self):
        return self.__cover
    def getID(self):
        return self.__id


    


