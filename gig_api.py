import time
import os
from dotenv import load_dotenv
import promts
import uuid
import requests
from typing import Dict, List, Optional
from history import chat_history

load_dotenv()
rquid = str(uuid.uuid4())
AUTORIZATION_DATA = os.getenv('A_DATA')


def get_token() -> str:
    token: Optional[str] = None
    token_time: float = 0
    scope: str = 'GIGACHAT_API_PERS'

    if (
        token and
        token_time and
        (time.monotonic() - token_time < 1000)
    ):
        return token
    headers = {
        'Authorization': f'Bearer {AUTORIZATION_DATA}',
        'RqUID': str(uuid.uuid4()),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'scope': scope}
    response = requests.post(
        "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
        headers=headers,
        data=data,
        verify=False
    )
    if response.status_code == 200:
        token_time = time.monotonic()
        token = response.json()["access_token"]
        if isinstance(token, str):
            return token
    raise Exception(f'Error[{response.status_code}]: {response.text}')

def make_data(message:str, promt = promts.base_prompt) -> List[Dict]:
    messages: List[Dict] = [
            {
                'role': 'system',
                'content': promt                
            }, 
            *chat_history, 
            {
                'role': 'user',
                'content': message    
            }
        ] 
    print(promt)
    return messages
    
def gigachat_response(message:str, role: str) -> str:
        token = get_token()
        messages = make_data(message, promt = promts.get_prompt(role))
        data = {
            'messages': messages,
            'model': 'GigaChat:latest',
            'temperature': 1
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(
            'https://gigachat.devices.sberbank.ru/api/v1/chat/completions',
            verify = False,
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            newdata = response.json()
            return newdata["choices"][0]["message"]["content"]
        raise Exception(f'Error[{response.status_code}]: {response.text}')