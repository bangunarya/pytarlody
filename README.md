# Python Implementation of Guitar Melody Detection
This repository contains the code to map from time-frequency representation of guitar signal
to the guitar tablature. \
This code is reimplementation in python from 
[Arya Bangun's bachelor thesis](https://openlibrary.telkomuniversity.ac.id/pustaka/92118/deteksi-melody-pada-gitar-menggunakan-transformasi-wavelet.html
) in Indonesian.\
The time-frequency representation is obtained by using Gabor Wavelet.

# Requirements

The following Python libraries are required to run the code in this repository:

```
numpy
scipy
```
and can be installed with ```pip install -e .```

# Usage
All the figures in the paper can be reproduced by running the notebook ```Example.ipynb``` 

# Results
The following figures are examples of time-frequency representation and mapping to guitar tablature.

 <img src="https://user-images.githubusercontent.com/47388866/183309550-e329cd0f-0ecf-44c5-97ef-4ccc9194ea02.png" width="300" height="250"  class="center"/>
 
```
Str.1:8-7-7-7-5-3-1------
Str.2:--------------5-5-3
Str.3:-------------------
Str.4:-------------------
Str.5:-------------------
Str.6:-------------------
```

The feature for guitar tuning is provided
```
Frequency for 1 string is  329.63
Recorded frequency  326.8996177109342
Too low! Increase the string tension
```
## Licence
All files are provided under the terms of the MIT License
