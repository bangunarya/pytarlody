import numpy as np


def generate_gabor(Bandwidth: float, Fs: int, Flo: float, 
                   Fhi: float, Nsteps: int):
    """
    A function to generate Gabor filter
    before apply Fourier transform

    Parameters
    ----------
    Bandiwdth

    Fs
        Sampling rate of our data

    Flo
        The lowest frequency
    Fhi
        The highest frequency
    Nsteps
        Sample of the frequency

    Return
    ------


    """
    K = np.sqrt(2*np.log(2))
    M = K * (2**Bandwidth + 1) / (2**Bandwidth - 1)
    # B = np.log2((1+K/M)/(1-K/M))
    freq = np.exp(np.linspace(np.log(Flo), np.log(Fhi), Nsteps))
    phase = np.pi/4 
    gabor_h = {}
    gabor_g = {}

    for idx in range(Nsteps):
        f = freq[idx]
        # Deviation in frequency
        
        sigma_freq = f/M
        # Deviation in time
        sigma_time = 1/(2*np.pi*sigma_freq)
        
        # Parameter Windows
        w = np.ceil(3.5*sigma_time*Fs)
        t = np.arange(-w, w+1)*(1/Fs)
        
        # Generate envelope
        env = np.exp(-t**2/(2*sigma_time**2))
        # Wave signal without envelope
        wave = np.cos(2*np.pi*f*t+phase)

        # Product with window
        g = env*wave
        h = g[::-1]

        # Amplitude
        amp = np.sqrt(np.sum(g**2 + h**2))

        # Normalization
        g = (1/amp)*g
        h = (1/amp)*h
        # Store 
        gabor_g[idx] = g
        gabor_h[idx] = h

    return gabor_g, gabor_h, freq


def time_frequency_analysis(data, gabor_g, gabor_h, Nsamples, Nsteps):
    """
    A function for time frequency analysis

    Parameters
    ----------
    data
        Signal we want to analyze

    gabor_g, gabor_h
        The Filter we generated to create window for our signal
    
    Nsamples
        Length of the array of our data

    Nsteps
        Number of frequency grid

    Return
    ------
    tf 
        Time-frequency analysis of our data

    
    
    """
    # length of largest filter
    N = len(gabor_g[0]) 

    # Determine number of FFT points
    NFFT = int(2**np.ceil(np.log2(np.abs(Nsamples + np.floor(N/2)))))
    
    # Apply Fourier transform on data
    S = np.fft.fft(data, NFFT, norm='ortho')
    
    tf = np.zeros((Nsteps, Nsamples))
    for id in range(Nsteps):
        # Create complex kernel
        kernel = gabor_g[id] + 1j*gabor_h[id]
        # Apply Fourier transform on the kernel
        T = np.fft.fft(kernel, NFFT, norm='ortho')

        # Time-Frequency Matrix
        result = np.abs(np.fft.ifft(S*T, norm='ortho'))
        index = (np.floor(len(kernel)/2) + 
                 np.arange(1, Nsamples+1)).astype(int)

        tf[id, :] = result[index]

    return tf