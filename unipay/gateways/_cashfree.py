

class Cashfree():
    def __init__(self, client_id:str, client_secret:str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.gateway = 'cashfree'
        self.api_version = ""