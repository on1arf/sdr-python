# sdr-python
Learning Signal processing and SDR with numpy and scipy

Some jupyter notebooks + datafiles on my experiences to learn how to do signal-processing and SDR with python, numpy and scipy.signal.

This runs in a jupyter notebook with python3, numpy, scipy, scipy.signal and matplotlib.

If you run docker, this image will provide everything you need:
https://hub.docker.com/r/jupyter/scipy-notebook

## available notebooks:
- exercise 1: getting started: efr_teleswitch.ipynb<br>
 efr_teleswitch, slow-speed FSK demodulation.<br>
 Decoded slow-speed FSK from DCF39, DCF49 and HGA22 in Gernamy and Hungary at 129.1, 135.6 and 139.9 KHz.<br>
 Requires: efr_teleswitch_30s.f32

- exercise 2: slow-speed PSK: tdf_162KHz.ipynb<br>
 slow-speed PSK from the TDF transmitter in France on 162 KHz.<br>
 The first exercise decoding phase-shift keying signals.<br>
 Requires: schmitt.py, tdf_120s.f32

- exercise 3: PSK: dcf77psk.ipynb<br>
 Decode the PSK transmission from the DCF77 time transmitter in germany on 77.5 KHz.<br>
 The 2nd exercise decoding phase-shift keying signals, now decoding PSK in the phase domain.<br>
 Requires: schmitt.py, dcf77_30s.f32

- exercise 3bis: PSK: dcf77psk-alternative-end.ipynb<br>
 Decode the PSK transmission from the DCF77 time transmitter in germany on 77.5 KHz.<br>
 This is an alternative version of exercise 3 above. This notebook does not actually decode the PSK signal, but uses
 correlation to determine the polarity of the PSK signal.<br>
 Requires: schmitt.py, dcf77_30s.f32

