from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from TextToSpeech import synthesize_text
from FileToSpeech import FileToSpeech
from OTPSpeech import OTPSpeech
from OTPFileToSpeech import OTPFileToSpeech
import uvicorn
import os

app = FastAPI()

@app.get('/')
async def index():
    return 0

@app.get('/TextToVoice')
async def response(text:str = None):
    if(text == None):
        return {
            "detail": {
                "status": 400,
                "text": "None"
            }
        }
    audio_file = synthesize_text(text)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/OTPVoice')
async def response(text:str = None):
    if(text == None):
        return {
            "detail": {
                "status": 400,
                "text": "None"
            }
        }
    audio_file = OTPSpeech(text)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/FileToVoice')
async def response(file:UploadFile = File(...)):
    if not file.content_type.startswith("text"):
        return {
            "detail": {
                "status": 400,
                "file": "File Is Not txt"
            }
        }
    audio_file = await FileToSpeech(file)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/OTPFileToVoice')
async def response(file:UploadFile = File(...)):
    if not file.content_type.startswith("text"):
        return {
            "detail": {
                "status": 400,
                "file": "File Is Not txt"
            }
        }
    audio_file = await OTPFileToSpeech(file)
    return file
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)