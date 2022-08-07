from scipy.io import wavfile


def load_wav_data(path: str):
    """
    A function to load .wav file of our guitar melody


    Parameters
    ----------
    path
        Path of our data

    Returns
    -------
    data
        Array of our guitar melody
    
    samplerate
        The sample rate of our data
    """

    samplerate, data = wavfile.read(path)

    return samplerate, data

