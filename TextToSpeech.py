def synthesize_text(text, format):
    print(format)
    from gtts import gTTS
    import time

    seconds = time.time()
    tts = gTTS(text, lang='id')
    audio_file = './audio/'+str(seconds)+'.'+str(format)
    tts.save(audio_file)

    return audio_file