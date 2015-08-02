from distutils.core import setup

setup(
    name='Hear',
    version='0.1',
    packages=['hear'],
    license='MIT License',
    install_requires=[
        "numpy",
        "pyaudio",
        "jack-client"
    ],
)
