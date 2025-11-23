import whisper
import tempfile
from st_audiorec import st_audiorec

model = whisper.load_model("base")

def record_audio_streamlit():
    audio_bytes = st_audiorec()

    if audio_bytes is not None:
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp.write(audio_bytes)
        temp.close()
        return temp.name

    return None


def speech_to_text(filepath):
    if filepath:
        result = model.transcribe(filepath)
        return result["text"]

    return ""
