import matplotlib.pyplot as plt
import numpy as np


def draw_sin_wave(frequency: float, sampling_rate: float):
    t = np.arange(0, 2, 1 / sampling_rate)  # サンプリング時間軸
    t_continuous = np.linspace(0, 2, 1000)  # 連続時間軸

    y = np.sin(2 * np.pi * frequency * t)  # サンプリングした正弦波
    y_continuous = np.sin(2 * np.pi * frequency * t_continuous)  # 連続正弦波

    plt.figure(figsize=(10, 5))

    # 連続波とサンプリング波を1つのグラフに表示
    plt.plot(t_continuous, y_continuous, label="Continuous", linewidth=2)
    plt.plot(t, y, "-o", label="Sampled", color="red", linewidth=2, markersize=6)

    plt.title(f"Sine Wave: {frequency} Hz, Sampling Rate: {sampling_rate} Hz")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.xlim(0, 1)
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    freq = float(input("正弦波の周波数を入力してください(Hz): "))
    sampling_rate = float(input("サンプリング周波数を入力してください(Hz): "))
    draw_sin_wave(freq, sampling_rate)
