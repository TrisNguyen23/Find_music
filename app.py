from record import record_audio
from audd_recognize import recognize_song

if __name__ == "__main__":
    filename = "query.wav"
    record_audio(filename, duration=6.0)
    recognize_song(filename)
