async def OTPFileToSpeech(file):
    from OTPSpeech import OTPSpeech

    text = await file.read()
    text = text.decode("utf-8") 

    return await OTPSpeech(text)