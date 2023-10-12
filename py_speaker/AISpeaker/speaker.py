import speech_recognition as sr
import time, os
import openai
from gtts import gTTS
from playsound import playsound

openai.api_key = ""
model="gpt-3.5-turbo"
"""messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]"""

messages=[]

#음성 인식(듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') #음성 인식이 실패한 경우
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) #api key오류, 네트워크 단절 등


#대답
def answer(input_text):
    user_content = input_text
    messages.append({"role" : "user", "content" : f"{user_content}"})
    chat_completion = openai.ChatCompletion.create(model=model, messages=messages)

    assistant_content = chat_completion.choices[0].message.content.strip()

    messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

    speak(assistant_content)

#소리내어 읽기(TTS)
def speak(text):
    print("[인공지능]" + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): #mp3파일 삭제 안하면 퍼미션 디나이
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) #더 이상 듣지 않음

while(True):
    time.sleep(0.1)


