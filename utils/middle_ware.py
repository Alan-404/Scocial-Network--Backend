import jwt
from dotenv import dotenv_values


class JwtFilter:
    def __init__(self) -> None:
        self.config = dotenv_values('.env')

    def generate_access_token(self, account_id: str):
        payload = {
            'id': account_id
        }
        return jwt.encode(payload=payload, key=self.config['TOKEN_KEY'], algorithm=self.config['ALGORITHM'])
    
    def get_account_id(self, token: str) -> str:
        return jwt.decode(token, key=self.config['TOKEN_KEY'])
