import matplotlib.pyplot as plt
import numpy as np

spectrum = np.loadtxt("overdrive-eh.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1]+100, label="Overdrive EH")

spectrum = np.loadtxt("edge-eh.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1], label="Edge EH")

spectrum = np.loadtxt("edge-a.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1], label="Edge A")

spectrum = np.loadtxt("curbing-uh.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1]-100, label="Curbing UH")

spectrum = np.loadtxt("curbing-oo.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1]-100, label="Curbing OO")

spectrum = np.loadtxt("neutral-ee.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1]-200, label="Neutral EE")

spectrum = np.loadtxt("neutral-oo.txt", skiprows=1)
plt.plot(spectrum[:,0], spectrum[:,1]-200, label="Neutral OO")

plt.legend()
plt.xlim([0.0, 5000.0])
plt.show()

