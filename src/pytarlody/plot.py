import matplotlib.pyplot as plt
import numpy as np


def plot_tf(tf: np.ndarray, Nsamples: int, Fs: int, freq: np.ndarray):
    """
    A function to plot time-frequency data
    
    Parameters
    ----------
    tf 
        Array of time frequency
    Nsamples
        Dimension of data
    Fs
        Sampling rate
    freq
        Logarithmic scale of the frequency
    """

    TimeLo = 0
    TimeHi = Nsamples/Fs
    TimeStep = 1
    FreqLo = freq[0]
    FreqHi = freq[-1]
    FreqStep = 5
    # Define tick for plotting
    Nfreq, Ntime = tf.shape
    
    Xtick = np.arange(TimeLo, TimeHi + 1, TimeStep)
    Ytick = np.arange(FreqLo, FreqHi + 1, FreqStep)
    # Plot
    plt.figure()
    plt.imshow(np.flipud(tf), 
               extent=[Xtick[0], Xtick[-1], Ytick[0], Ytick[-1]],  
               aspect='auto')

    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.title('Time-Frequency Analysis')
    plt.show()
     
 