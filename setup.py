from distutils.core import setup

try:
    with open("README.rst", "r") as f:
        long_description = f.read()
except EnvironmentError:
    long_description = ""

setup(
    name="Hear",
    author="Edoardo Negri",
    author_email="edne@gmx.com",
    url="https://github.com/edne/hear",
    description="Boilerplate for Jack and PyAudio",
    long_description=long_description,
    version="0.2",
    packages=["hear"],
    license="MIT License",
    install_requires=[
        "numpy",
        "pyaudio",
        "jack-client"
    ],
)
