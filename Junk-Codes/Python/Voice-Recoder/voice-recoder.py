import sounddevice as sd
import scipy.io.wavfile as wav

sec = int(input("Record Seconds: "))
fs = 44100
print("Recording...")
audio = sd.rec(int(sec * fs), samplerate=fs, channels=2)
sd.wait()
wav.write("record.wav", fs, audio)
print("Saved record.wav")
