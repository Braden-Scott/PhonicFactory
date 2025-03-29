from gtts import gTTS

letter = "apple"
tts = gTTS(text=letter, lang='en', slow=False)
tts.save('test.mp3')