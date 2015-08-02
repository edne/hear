# Hear
Boilerplate for Jack and PyAudio


## Why?
[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) offers a binding for the
old good [PortAudio](http://www.portaudio.com/), it works everywhere but is
quite low-level and if you are using [Jack](http://jackaudio.org/) can be painful
(ok, it is supported, but I was not able to create a client, nor to find working
code by someone else).

[Jack-Client](https://github.com/spatialaudio/jackclient-python/) is way better,
but, obviously, works only with an active Jack server.

I want both.
