from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio/output.mp3")
    return "audio/output.mp3"
