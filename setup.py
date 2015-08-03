from distutils.core import setup

try:
    readme = "README.md"
    try:
        from pypandoc import convert
        long_description = convert(readme, 'rst')
    except ImportError:
        print("warning: pypandoc not found, could not convert Markdown to RST")
        long_description = open(readme, 'r').read()
except IOError:
    long_description = ""

setup(
    name="Hear",
    author="Edoardo Negri",
    author_email="edne@gmx.com",
    url="https://github.com/edne/hear",
    description="Boilerplate for Jack and PyAudio",
    long_description=long_description,
    version="0.1.1",
    packages=["hear"],
    license="MIT License",
    install_requires=[
        "numpy",
        "pyaudio",
        "jack-client"
    ],
)
