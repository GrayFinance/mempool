import requests

class Mempool:

    def __init__(self) -> None:
        self.__url = "https://mempool.space"

    def get_node_stats(self, id: str) -> dict:
        url = f"{self.__url}/api/v1/lightning/nodes/{id}"
        return requests.get(url).json()

    def fees_recommended(self) -> dict:
        url = f"{self.__url}/api/v1/fees/recommended"
        return requests.get(url).json()

