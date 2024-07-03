from dataclasses import dataclass

from openai import OpenAI

from common.chatgpt import settings
from services.file import Filework

@dataclass
class OpenChatAI:
    api_key: str = settings.token
    
    def response(self, file: Filework) -> str:
        content = file.get_content()
        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": content}
                ]
            )
        return completion.choices[0].message.content