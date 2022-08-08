import os
from pytarlody.load_data import load_wav_data, play_wav
from pytarlody.time_frequency import generate_gabor, time_frequency_analysis
from pytarlody.plot import plot_tf
from scipy.signal import argrelmin
import re

import numpy as np


def tuning(tf, order, freq, string):

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
    # Frequency open strings
    open_string = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]

    # Dimension of frequency and time
    Nfreq, Ntime = tf.shape

    FreqLo = freq[0]
    FreqHi = freq[-1]
    logy = np.linspace(np.log(FreqLo), np.log(FreqHi), Nfreq)

    # Fioding maximum index of our time-frequency data
    arr_maks = tf[np.argmax(tf, 0), np.arange(tf.shape[1])]

    # for local minima to estimate the length of the Frequncy
    loc_min = argrelmin(arr_maks, order=order)
    idx_loc = loc_min[0]
    
    # Get only minimum below the average, to avoid accessing higher minimum
    idx_loc = idx_loc[arr_maks[loc_min] < np.mean(arr_maks)]

    idx_start = 0
    exp_logy = []

    for idi in range(len(idx_loc)):
        
        idx_end = idx_loc[idi]

        # Getting maximum position or frequency of certain windowing
        max_position = np.argmax(np.sum(tf[:, idx_start:idx_end], 1))
        logy_max = np.exp(logy[max_position])
        idx_start = idx_end
        exp_logy.append(logy_max)

    # For each maximum compare to database
    idx_min = np.argmin(np.abs(open_string[string - 1] - np.array(exp_logy)))
    print('Frequency for ' + str(string) + ' string is ', str(open_string[string - 1]))
    print('Recorded frequency ', str(exp_logy[idx_min]))
    if exp_logy[idx_min] < open_string[string - 1]:
        print('Too low! Increase the string tension')
    elif exp_logy[idx_min] > open_string[string - 1]:
        print('Too high! Decrease the string tension')
    else:
        print('Perfect!')
        
    
def main_tuning(path: str, Bandwidth: float, Flo: float, 
                Fhi: float, Nsteps: int, order: int, string: int):

    """
    Function to generate tablature of the guitar melody

    path
        Path of our data
    Bandwidth
        Bandwidth for our analysis
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
    
    tuning(tf, order, freq, string)


if __name__ == '__main__':

    # Give path
    # filename = '6th_open.wav'     
    # filename = '5th_open.wav'
    # filename = '4th_open.wav'
    # filename = '3rd_open.wav'
    # filename = '2nd_open.wav'
    filename = '1st_open.wav'

    dir = '/home/bangun/Documents/pytarlody/data'
    path = os.path.join(dir, filename)

    # Play sound
    play_wav(path)

    # Parameters
    # Lowest frequency
    Flo = 70
    # Highest Frequency
    Fhi = 660
    # Discrete step between frequency
    Nsteps = 100
    # Bandiwdth signal
    Bandwidth = 1/12

    # Distance to find local minimum
    order = 250
    # Generate tab
    string = int(re.split('(\d+)', filename.split('_')[0])[1])
    
    main_tuning(path, Bandwidth, Flo,
                Fhi, Nsteps, order, string)
