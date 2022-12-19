def synthesize_text(text):
    from gtts import gTTS
    import time
    import librosa
    import soundfile as sf
    import audio_metadata

    seconds = time.time()
    tts = gTTS(text, lang='id')
    audio_file = './audio/'+str(seconds)+'.wav'
    tts.save(audio_file)
    x,_ = librosa.load(audio_file, sr=8000)
    sf.write(audio_file, x, 8000)
    metadata = audio_metadata.load(audio_file)

    return audio_file