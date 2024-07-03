from dataclasses import dataclass
import pathlib
import environ

BASE_DIR = pathlib.Path(__file__).parent
env = environ.Env()
env.__class__.read_env(BASE_DIR / '.env')

@dataclass
class Response_Reader():
    token: str=env('OPEN_API_KEY')
    
    
settings=Response_Reader()