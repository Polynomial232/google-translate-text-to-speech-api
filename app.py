from fastapi import FastAPI, UploadFile, File, HTTPException, status
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

@app.get('/text-to-voice')
async def response(text:str = None):
    if(text == None):
        raise HTTPException(status_code=400)
    audio_file = synthesize_text(text)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/otp-voice')
async def response(text:str = None):
    if(text == None):
        raise HTTPException(status_code=400)
    audio_file = await OTPSpeech(text)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/file-to-voice')
async def response(file:UploadFile = File(...)):
    if not file.content_type.startswith("text"):
        raise HTTPException(status_code=400)
    audio_file = await FileToSpeech(file)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

@app.get('/otp-file-to-voice')
async def response(file:UploadFile = File(...)):
    if not file.content_type.startswith("text"):
        raise HTTPException(status_code=400)
    audio_file = await OTPFileToSpeech(file)
    file_path = os.path.join(audio_file)
    return FileResponse(file_path, media_type='wav', filename=audio_file)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)