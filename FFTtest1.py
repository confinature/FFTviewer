import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 64 # サンプル数
freq1 = 2 # 周期1
freq2 = 6 # 周期2
a1 = 1.5 # 振幅1
a2 = 3 # 振幅2
n = np.arange(N)
fn = a1 * np.sin(freq1 * 2 * np.pi * (n/N)) + a2 * np.sin(freq2 * 2 * np.pi * (n/N))  # フーリエ変換する信号f(n)
Fn = np.fft.fft(fn) # 高速フーリエ変換したものF(n)
Fn_abs = np.abs(Fn) # F(n)の絶対値
Fn_abs_amp = Fn_abs / N * 2 # 交流成分はデータ数で割って2倍する
Fn_abs_amp[0] = Fn_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要

plt.figure(figsize=(8, 4)) 
plt.xlabel('n')
plt.ylabel('Signal')
plt.plot(Fn_abs_amp[:int(N/2)+1]) # 鏡像を無視したパワースペクトルをプロット

plt.show()