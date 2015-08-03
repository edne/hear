from distutils.core import setup

setup(
    name="Hear",
    author="Edoardo Negri",
    author_email="edne@gmx.com",
    url="https://github.com/edne/hear",
    description="Boilerplate for Jack and PyAudio",
    long_description="Offers an easy way to read audio input streams, using \
Jack OR PortAudio backends",
    version="0.1",
    packages=["hear"],
    license="MIT License",
    install_requires=[
        "numpy",
        "pyaudio",
        "jack-client"
    ],
)
