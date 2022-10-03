# from gtts import gTTS 

# # The text that you want to convert to audio 
# mytext = "Halo selamat siang"

# tts = gTTS(mytext, lang='id')
# audio_file = 'aaa.wav'
# tts.save(audio_file)

import librosa
import soundfile as sf
import audio_metadata
# x,_ = librosa.load('./audio/1664779207.1984305.wav', sr=8000)
# sf.write('tmp.wav', x, 8000)
metadata = audio_metadata.load('./audio/1664779301.0111027.wav')
print(metadata)