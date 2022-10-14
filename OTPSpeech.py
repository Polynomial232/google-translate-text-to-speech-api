async def OTPSpeech(text):
    from TextToSpeech import synthesize_text
    alfanum = {
        '0': "nol",
        '1': "satu",
        '2': "dua",
        '3': "tiga",
        '4': "empat",
        '5': "lima",
        '6': "enam",
        '7': "tujuh",
        '8': "delapan",
        '9': "sembilan"
    }
    temp_text = list(text)
    for index, i in enumerate(text):
        if i.isdigit():
            temp_text[index] = alfanum[i] + " "
    text = "".join(temp_text)

    return synthesize_text(text)