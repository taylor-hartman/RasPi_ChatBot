import setuptools

setuptools.setup(
    name="RasPi_ChatBot",
    version="1.0",
    author="Taylor Hartman",
    author_email="taylorhartmandev@gmail.com",
    url="https://github.com/taylor-hartman/RasPi_ChatBot",
    packages=['RasPi_ChatBot'],
    install_requires=[
    'nltk==3.5',
    'Keras==2.4.3',
    'numpy==1.18.5',
    'SpeechRecognition==3.8.1',
    'gTTS==2.1.1',
    'board==1.0']
)