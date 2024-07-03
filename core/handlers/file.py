import os
import aiofiles
from fastapi import APIRouter, File, UploadFile

from services.chatgpt import OpenChatAI
from services.file import Filework


router = APIRouter(tags=['files'], prefix='/files')


os.makedirs('files', exist_ok=True)

@router.post(
    "/uploadfile/",
    description='Получить ответ от Модельки',
    summary='Кинуть excel или pdf файл, потом получить ответ от модельки',
    operation_id='postUploadFile',
)
async def upload_file(file: UploadFile = File(...)):
    file_worker=Filework(
        file_name=file.filename,
        file_location=f"files/{file.filename}",
    )
    
    async with aiofiles.open(file_worker.file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    openchat=OpenChatAI()
    file_worker.content=openchat.response(file=file_worker)
    
    try:
        os.remove(file_worker.file_location)
    except Exception as e:
        return {"info": f"Ошибка при удалении файла: {str(e)}"}
    
    
    return {"info": 
        f"file '{file_worker.file_name}' saved at '{file_worker.file_location}'",
        f"response":{file_worker.content}    
    }
