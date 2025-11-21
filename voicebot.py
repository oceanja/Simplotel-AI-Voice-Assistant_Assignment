from utils.speech_to_text import record_audio, speech_to_text
from utils.text_to_speech import speak
from utils.nlp import get_response

def run_voicebot():
    # 1. Record voice
    record_audio()

    # 2. Convert speech to text
    user_text = speech_to_text()
    print("User said:", user_text)

    # 3. Get AI response
    response = get_response(user_text)
    print("Bot:", response)

    # 4. Convert text to speech
    audio_file = speak(response)

    return user_text, response, audio_file
