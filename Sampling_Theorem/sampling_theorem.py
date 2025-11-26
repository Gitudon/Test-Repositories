import matplotlib.pyplot as plt
import numpy as np


def draw_sin_wave(frequency: float):
    sampling_rate = 1000  # サンプリング周波数
    t = np.arange(0, 1, 1 / sampling_rate)  # 時間軸
    y = np.sin(2 * np.pi * frequency * t)  # 正弦波

    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f"Sine Wave with Frequency {frequency} Hz")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.xlim(0, 0.1)  # 最初の0.1秒だけ表示
    plt.show()


if __name__ == "__main__":
    freq = float(input("Enter the frequency of the sine wave (Hz): "))
    draw_sin_wave(freq)
