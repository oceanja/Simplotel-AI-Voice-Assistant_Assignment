from utils.speech_to_text import record_audio_streamlit, speech_to_text
from utils.text_to_speech import text_to_speech
from utils.nlp import get_response

def run_voicebot():
    filepath = record_audio_streamlit()

    if not filepath:
        return "", "No audio recorded.", None

    user_text = speech_to_text(filepath)
    print("User said:", user_text)

    response = get_response(user_text)
    print("Bot:", response)

    audio_file = text_to_speech(response)

    return user_text, response, audio_file
