def synthesize_text(text):
    from gtts import gTTS
    import time

    seconds = time.time()
    tts = gTTS(text, lang='id')
    audio_file = './audio/'+str(seconds)+'.mp3'
    tts.save(audio_file)
    
    # from playsound import playsound
    # playsound(audio_file)

    return audio_file