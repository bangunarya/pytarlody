import os
from pytarlody.load_data import load_wav_data, play_wav
from pytarlody.time_frequency import generate_gabor, time_frequency_analysis
from pytarlody.maps_to_tab import mapping_to_tablature
from pytarlody.plot import plot_tf


def generate_tab(path: str, Bandwidth: float, Flo: float, 
                 Fhi: float, Nsteps: int, order: int):

    """
    Function to generate tablature of the guitar melody

    path
        Path of our data
    Bandwidth
        Bandiwidth for our analysis
    Flo
        Lowest frequency
    Fhi 
        Highest frequency
    Nsteps
        Sampling grid in the frequency
    order
        Distance range to find local minimum

    """

    # Load data
    Fs, data = load_wav_data(path)
    
    # Dimension of our data
    Nsamples = data.shape[0]

    # Generate gabor filter
    gabor_g, gabor_h, freq = generate_gabor(Bandwidth, Fs, Flo,
                                            Fhi, Nsteps)

    # Create time-frequency analysis
    tf = time_frequency_analysis(data, gabor_g, gabor_h, Nsamples, Nsteps)

    # Plot
    plot_tf(tf, Nsamples, Fs, freq)

    # Generate tablature
    
    tab = mapping_to_tablature(tf, order, freq)

    return tab


if __name__ == '__main__':
    # Give path
    filename = 'C-Doremi Descending1.wav'
    # filename = 'Doraemon.wav'
    # filename = 'A Pentatonik Ascending1.wav'
    # filename = 'A-Pentatonik Descending1.wav'
    dir = '/home/bangun/Documents/pytarlody/data'
    path = os.path.join(dir, filename)

    # Play sound
    play_wav(path)

    # Parameters
    # Lowest frequency
    Flo = 80
    # Highest Frequency
    Fhi = 660
    # Discrete step between frequency
    Nsteps = 100
    # Bandiwdth signal
    Bandwidth = 1/12

    # Distance to find local minimum
    order = 250
    # Generate tab
    tab = generate_tab(path, Bandwidth, Flo,
                       Fhi, Nsteps, order)
    print(tab)
