# Python Implementation of Guitar Melody Detection
This repository contains the code to map from time-frequency representation of guitar signal
to the guitar tablature. This code is reimplentation in python of 
[Arya Bangun's bachelor thesis](https://openlibrary.telkomuniversity.ac.id/pustaka/92118/deteksi-melody-pada-gitar-menggunakan-transformasi-wavelet.html
)\
The time-frequency representation is obtained by using Gabor Wavelet.

#Requirements

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
 <img src="https://user-images.githubusercontent.com/47388866/183309550-e329cd0f-0ecf-44c5-97ef-4ccc9194ea02.png" width="200" height="150" style="float:left"/>
 
```
Str.1:8-7-7-7-5-3-1------
Str.2:--------------5-5-3
Str.3:-------------------
Str.4:-------------------
Str.5:-------------------
Str.6:-------------------
```
