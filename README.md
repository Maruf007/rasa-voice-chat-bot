# rasa-voice-chat-bot
Steps:

```
docker run -p 8000:8000 rasa/duckling
```

Backend:

```
virtualenv -p python3.9 bot3.9
```
For powershell

```
bot3.9/Scripts/activate
```

```
pip install -e .
```

```
pip install websockets==10.0
```
```
rasa run --enable-api --cors "*"
```

```
rasa run actions
```

Frontend:
Node 16

```
npm i
```

```
npm start
```
