from scipy.signal import argrelmin
import numpy as np


def frequency_database():
    """
    A function to generate frequency on the first 12 frets
    we have dimension 6 on the row for the strings and 12 for column as frets

    
    
    """
    
    database_freq = np.zeros((6, 12))

    database_freq[0, :] = [349.23, 369.99, 392, 415.3, 440, 466.16, 493.88, 
                           523.25, 554.37, 587.33, 622.25, 659.25]
    database_freq[1, :] = [261.63, 277.18, 293.67, 311.13, 329.63, 349.23, 
                           369.99, 392, 415.3, 440, 466.16, 493.88]
    database_freq[2, :] = [207.65, 220, 233.08, 246.94, 261.63, 277.18, 293.67, 
                           311.13, 329.63, 349.23, 369.99, 392]
    database_freq[3, :] = [155.56, 164.81, 174.61, 185, 196, 207.65, 220, 
                           233.08, 246.94, 261.63, 277.18, 293.67]
    database_freq[4, :] = [116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 
                           164.81, 174.61, 185, 196, 207.65, 220]
    database_freq[5, :] = [87.307, 92.499, 97.999, 103.83, 110, 116.54, 123.47,
                           130.81, 138.59, 146.83, 155.56, 164.81]
    
    return database_freq


def mapping_to_tablature(tf: np.array, order: int, Nsamples: int,
                         freq: np.array):
    """
    A function to map from time-frequency data 
    to guitar tablature. Here we use simple mapping with 
    database frequency

    Parameters
    -----------
    tf 
        Time frequency results
    
    order
        Distance to find local minimum in the signal

    Nsamples
        Dimension of our data array
    
    freq
        Frequency in logarithmic scale

    Returns
    -------
    """
    
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

    database_freq = frequency_database()
    b, k = database_freq.shape

    # For each maximum compare to database
    tablature = np.zeros((6, len(exp_logy)), dtype=np.object)
    tablature[:] = '-'

    for idx_l in range(len(exp_logy)):
        string_fret = np.unravel_index(np.argmin(np.abs(database_freq - 
                                       exp_logy[idx_l])**2), 
                                       database_freq.shape)
        tablature[string_fret[0], idx_l] = str(string_fret[1] + 1)

    # Finding maximum length
    len_all = []
    for idx_str in range(6):
        len_all.append(len('-'.join(list(tablature[idx_str]))))

    len_max = np.max(len_all)

    # Create tablature
    tablature_list = ''
    temp_str = ''
    for string in range(6):
        temp_str = '-'.join(list(tablature[string])) 
        if len(temp_str) < len_max:
            temp_str = 'Str.' + str(string + 1) + ':' + temp_str + '-'*(len_max - len(temp_str)) + '\n'
 
        else:
            temp_str = 'Str.' + str(string + 1) + ':'+ temp_str + '\n'
        tablature_list = tablature_list + temp_str
    
    return tablature_list
