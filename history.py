from typing import Dict, List

chat_history:List[Dict] = []
def add_to_history(role: str, content: str) -> None: 
    chat_history.append(
        {
            'role': role,
            'content': content
        }
    )