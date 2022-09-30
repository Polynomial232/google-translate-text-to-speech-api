from gtts import gTTS 

# The text that you want to convert to audio 
mytext = "Halo selamat siang"

tts = gTTS(mytext, lang='id')
audio_file = 'aaa.wav'
tts.save(audio_file)