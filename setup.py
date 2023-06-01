from setuptools import setup, find_packages
import os

filename = 'PyAudio-0.2.12-cp39-cp39-win_amd64.whl'
abs_path = os.path.abspath(filename)
setup(
    name='rasa-voice-bot',
    version='1.0',
    author='Maruf',
    description='RASA voice bot',
    keywords='rasa, voice, bot',
    python_requires='==3.9',
    packages=find_packages(),
    install_requires=[
        'PyAudio @ file:///' + abs_path,
        'rasa==3.4.6',
        'pyttsx3==2.90',
        'SpeechRecognition==3.8.1',
        'websockets==10.0',
        'pandas',
        'flask',
        'flask_cors',
        'pydub'
    ],
    package_data={
        'sample': [],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)