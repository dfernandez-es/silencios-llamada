import wave
import numpy as np
import matplotlib.pyplot as plt



for file in pathlib.Path('/home/s3v3n/Escritorio/Nueva carpeta (1)/').glob('*.wav'):
    signal_wave = wave.open(file.name, 'r')
    sample_rate = 100000
    sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)
    sig = sig[:]
    plt.figure(1)
    plot_a = plt.subplot(211)
    plot_a.plot(sig)
    plot_a.set_xlabel(file.name)

    plt.show()