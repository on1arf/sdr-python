# sdr-python
Learning Signal processing and SDR with numpy and scipy

Some jupyter notebooks + datafiles on my experiences to learn how to do signal-processing and SDR with python, numpy and scipy.signal.

This runs in a jupyter notebook with python3, numpy, scipy, scipy.signal and matplotlib.

If you run docker, this image will provide everything you need:
https://hub.docker.com/r/jupyter/scipy-notebook

## available notebooks:
- exercise 1: getting started: efr_teleswitch.ipynb
 efr_teleswitch, slow-speed FSK demodulation.
 Decoded slow-speed FSK from DCF39, DCF49 and HGA22 in Gernamy and Hungary at 129.1, 135.6 and 139.9 KHz.
 Requires: efr_teleswitch_30s.f32

- exercise 2: slow-speed PSK: tdf_162KHz.ipynb
 slow-speed PSK from the TDF transmitter in France on 162 KHz.
 The first exercise decoding phase-shift keying signals.
 Requires: schmitt.py, tdf_120s.f32.bz2
 Due to the 25 MB filesize limit of github, the tdf_120s.f32 has been compressed. Do not forget to first uncompress this file.
