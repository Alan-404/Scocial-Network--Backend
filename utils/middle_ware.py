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
    
    def get_account_id(self, access_token: str) -> str:
        if access_token.startswith('Bearer ') == False:
            return None
        token: str = access_token.split(' ')[1]
        return jwt.decode(token, key=self.config['TOKEN_KEY'], algorithms=self.config['ALGORITHM'])['id']
