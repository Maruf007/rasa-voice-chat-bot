import requests
import speech_recognition as sr
import pyttsx3 
from flask import Flask, request
from flask_cors import CORS
import io
from pydub import AudioSegment

app = Flask(__name__)

CORS(app)

@app.route('/api/v1/bot', methods=['POST'])
def handle_endpoint():
    converter = pyttsx3.init() 
    converter.setProperty('rate', 150) 
    converter.setProperty('volume', 0.7) 
    voices = converter.getProperty('voices')
    converter.setProperty('voice', voices[1].id)
    rec = sr.Recognizer()

    bot_message = ""
    files = request.files['audio']
    
    audio_file = files.stream.read()
    
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_file))
    audio_segment.export('output.wav', format='wav')
    with sr.AudioFile('output.wav') as source:
        audio_data = rec.record(source)
        
    try:
        query = rec.recognize_google(audio_data, language="en-in")
        print("You Said : {}".format(query))
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"user": "user","message":query})

        for i in r.json():
            print("RASA Said : {}".format(i['text']))
            bot_message += i['text']

    except Exception as e:
        print(e)
    
    return {'message': bot_message}, 200

app.run(host='0.0.0.0', port=5000)