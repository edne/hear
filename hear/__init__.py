import numpy as np

__all__ = ["hear"]


def hear(callback, channels=2, body=None,
         jack_client="Hear",
         rate=44100, frames_per_buffer=1024):

    def default_body():
        from time import sleep
        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            print("\nInterrupted by user")

    if body is None:
        body = default_body

    if is_jack_active():
        hear_jack(callback, channels, body, jack_client)
    else:
        hear_pa(callback, channels, body, rate, frames_per_buffer)


def hear_jack(callback, channels, body, client_name):
    import jack
    client = jack.Client(client_name)

    if client.status.server_started:
        print("JACK server started")
    if client.status.name_not_unique:
        print("unique name {0!r} assigned".format(client.name))

    @client.set_process_callback
    def process(frames):
        assert len(client.inports) == channels
        assert frames == client.blocksize

        data = [np.fromstring(channel.get_buffer(),
                              dtype=np.float32)
                for channel in client.inports]

        callback(data)

        return jack.CALL_AGAIN

    for i in range(channels):
        client.inports.register("input_{0}".format(i+1))

    client.activate()
    capture = client.get_ports(is_physical=True, is_output=True)

    if capture:
        for src, dest in zip(capture, client.inports):
            try:
                client.connect(src, dest)
            except jack.JackError:
                pass

    body()

    client.deactivate()
    client.close()


def hear_pa(callback, channels, body, rate, frames_per_buffer):
    import pyaudio
    pa = pyaudio.PyAudio()

    def stream_cb(in_data, frame_count, time_info, status):
        data = np.fromstring(in_data, dtype=np.float32)
        data = np.reshape(data, (frame_count, channels))
        data = [data[:, i]
                for i in range(channels)]

        callback(data)

        return (in_data, pyaudio.paContinue)

    stream = pa.open(format=pyaudio.paFloat32,
                     channels=channels,
                     rate=rate,
                     frames_per_buffer=frames_per_buffer,
                     input=True,
                     input_device_index=0,
                     stream_callback=stream_cb
                     )

    stream.start_stream()

    body()

    stream.stop_stream()
    stream.close()

    pa.terminate()


def is_jack_active():
    import pyaudio
    print("--- portaudio annoying verbosity:")
    pa = pyaudio.PyAudio()
    print("---\n")

    apis = [pa.get_host_api_info_by_index(i)["name"]
            for i in range(pa.get_host_api_count())]

    return any([api.lower().startswith("jack")
                for api in apis])
