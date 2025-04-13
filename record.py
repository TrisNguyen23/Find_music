import sounddevice as sd
import wavio

def record_audio(filename, duration=5, fs=44100):
    print("Ghi âm bắt đầu...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavio.write(filename, recording, fs, sampwidth=2)
    print("Ghi âm hoàn tất.")
