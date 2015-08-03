Hear
====

Boilerplate for Jack and PyAudio

Why?
----

`PyAudio <https://people.csail.mit.edu/hubert/pyaudio/>`__ offers a
binding for the old good `PortAudio <http://www.portaudio.com/>`__, it
works everywhere but is quite low-level and if you are using
`Jack <http://jackaudio.org/>`__ can be painful (ok, it is supported,
but I was not able to create a client, nor to find working code by
someone else).

`Jack-Client <https://github.com/spatialaudio/jackclient-python/>`__ is
way better, but, obviously, works only with an active Jack server.

I want both.

Usage
-----

To read audio from the microphone:

.. code:: python

    from hear import hear


    def callback(data):
        left  = data[0]
        right = data[1]
        # do stuff

    hear(callback)

where ``data`` is a `NumPy <http://www.numpy.org/>`__ array.

If you have an active Jack server running the callback is processed by a
Jack client, otherwise by PyAudio.

``hear`` takes also other arguments:

.. code:: python

    def hear(callback, channels=2, body=None, jack_client="Hear"):
        ...

``jack_client`` is the client name, and ``body`` is the action (a
function) performed while the client/pa-stream is running, by default:

.. code:: python

    def body():
        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            print("Interrupted by user")

Installing
----------

.. code:: bash

    pip install hear --allow-unverified pyaudio

Known Issues
------------

-  If you change the Jack state you have to reload the whole
   application. (To check the available backends Hear uses PyAudio, and
   the C part inizializes everything just one time storing the state in
   some global variables)
