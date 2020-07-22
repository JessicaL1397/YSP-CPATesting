# %%
import numpy as np
import matplotlib.pyplot as plt

with open("first_line.txt",'r') as f:
    x = f.readline().split()
x = [int(y) for y in x]
#print(x)
plt.plot(x)



traces = np.loadtxt('traces.txt')
plainText = np.loadtxt('plaintexts.txt')
firstLine = np.loadtxt('first_line.txt')

numTraces = np.shape(traces)[0]

for b in range(0, 16):
    cpaOutput = [0]*256
    for guess in range(0, 256):
        print ("Poskey %d, hyp = %02x"%(b, guess))        


# %%

