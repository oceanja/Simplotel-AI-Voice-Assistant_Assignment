import sounddevice as sd
import scipy.io.wavfile as wav
import whisper

def record_audio(filename="audio/input.wav", duration=5, fs=44100):
    print("🎤 Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Audio recorded")

def speech_to_text():
    model = whisper.load_model("base")
    result = model.transcribe("audio/input.wav")
    return result["text"]
