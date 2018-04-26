# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def main():

    # パラメータ
    N = 1024 # サンプル数
    dt = 0.01 # サンプリング間隔
    f1 = 10 # 周波数
    t = np.arange(0, N*dt, dt) # 時間軸
    freq = np.linspace(0, 1.0/dt, N) # 周波数軸

    # 正弦波にランダムノイズを加えたもの
    f = np.sin(2*np.pi*f1*t) + 0.3 * np.random.randn(N)
    
    # FFT
    F = np.fft.fft(f)
    # 振幅スペクトル
    Amp = np.abs(F)

    # グラフを表示する
    plt.figure()
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 17
    plt.subplot(121)
    plt.plot(t, f, label='f(n)')
    plt.xlabel("Time", fontsize=20)
    plt.ylabel("Signal", fontsize=20)
    plt.grid()
    leg = plt.legend(loc=1, fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.subplot(122)
    plt.plot(freq, Amp, label='|F(k)|')
    plt.xlabel('Frequency', fontsize=20)
    plt.ylabel('Amplitude', fontsize=20)
    plt.grid()
    leg = plt.legend(loc=1, fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.show()


if __name__ == "__main__":
    main()