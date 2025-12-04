import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.example("trumpet"))
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform of Trumpet Sound")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
