import numpy as np
import matplotlib.pyplot as plt

name = "/home/plutoSDR/dev/audio.pcm"

data = []
imag = []
real = []
count = []
counter = 0
with open(name, "rb") as f:
    index = 0
    while (byte := f.read(2)):
        if(index % 2 == 0):
            real.append(int.from_bytes(byte, byteorder='little', signed=True))
            counter += 1
            count.append(counter)
        else:
            imag.append(int.from_bytes(byte, byteorder='little', signed=True))
        index += 1
        
name2 = "/home/plutoSDR/dev/rxdata.pcm"

data1 = []
imag1 = []
real1 = []
count1 = []
counter1 = 0
with open(name2, "rb") as f:
    index1 = 0
    while (byte := f.read(2)):
        if(index1 % 2 == 0):  # Исправлено: index1 вместо index
            real1.append(int.from_bytes(byte, byteorder='little', signed=True))  
            counter1 += 1
            count1.append(counter1)
        else:
            imag1.append(int.from_bytes(byte, byteorder='little', signed=True))  
        index1 += 1

#TX
plt.figure(1)
plt.plot(count, imag, color='red', label='TX Imag')
plt.plot(count, real, color='blue', label='TX Real')
plt.show()

#RX
plt.figure(2)
plt.plot(count1, imag1, color='red', label='RX Imag')  # Исправлено: imag1
plt.plot(count1, real1, color='blue', label='RX Real')  # Исправлено: real1
plt.show()