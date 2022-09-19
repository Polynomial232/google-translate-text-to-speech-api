async def FileToSpeech(file):
    from TextToSpeech import synthesize_text

    text = await file.read()
    text = text.decode("utf-8") 

    return synthesize_text(text)