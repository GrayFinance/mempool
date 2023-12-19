import requests

class Mempool:

    def __init__(self) -> None:
        self.__url = "https://mempool.space"
        self.__ln_url = "https://liquid.network" 
    
    def get_node_stats(self, id: str) -> dict:
        url = f"{self.__url}/api/v1/lightning/nodes/{id}"
        return requests.get(url).json()

    def fees_recommended(self) -> dict:
        url = f"{self.__url}/api/v1/fees/recommended"
        return requests.get(url).json()

    def get_address(self, address: str, network="bitcoin"):
        if network == "liquid":
            url = f"{self.__ln_url}/api/address/{address}"
        else:
            url = f"{self.url}/api/address/{address}"
        
        return requests.get(url).json()
