from web3 import Web3

class User():
    def __init__(self, username, password, adress, funds, nfts, cart, tokens):
        ganache_url = "HTTP://127.0.0.1:7545"

        self.__web3 = Web3(Web3.HTTPProvider(ganache_url))

        self.__username = username
        self.__password = password
        self.__adress = adress
        self.__funds = web3.eth.getBalance(adress)
        self.__nfts = nfts
        self.__cart = car
        self.__tokens = tokens

    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getAdress(self):
        return 
    def getFunds(self):
        return self.__web3.fromWei(self.__funds, "ether")

    def getNFTS(self):
        return self.__nfts
    def getCart(self):
        return self.__cart
    def getTokens(self):
        return self.__tokens
    
    def setUsername(self, username):
        self.__username = username
    def setPassword(self, password):
        self.__password = password

    def add_nft(self, nft):
        #nft.setAdress(user.adress)
        self.__nfts.append(nft)
    
    def add_to_cart(self, nft):
        self.__cart.append(nft)
    
    def add_token(self, token):
        self.__tokens.append(token)




