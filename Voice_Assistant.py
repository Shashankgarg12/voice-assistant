import pyttsx3
import time 
import pyjokes
import requests
import json
import speech_recognition as sr

date=time.strftime('%D')
tim=time.strftime('%T')

engine = pyttsx3.init()
def listen():
    """Listen to audio from the microphone and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            speak("There was a problem with the speech recognition service.")
        return ""
    
        
def speak(xyz):
    print(xyz)
    engine.say(xyz)
    engine.runAndWait()
def jok():
    jok=pyjokes.get_joke()
    speak(jok)
def ret_news(news,x):
    a3=news['articles'][x]
    speak(a3['title'])
    speak(a3['description'])

def again(new,a2):
    speak("""what you want
    more news for same topic :- one more
    other topic news :- other news
    for go to main program :- go back  """)
    x=listen()
    match x:
        case 'one more':
            a2+=1
            ret_news(new,a2)
            again(new,a2)
        case 'other news':
            news()
        case 'go back':
            run()


def news():
    a2=0
    m=int(time.strftime('%m'))-1
    date=time.strftime(f'%Y-{m}-%d')
    speak('enter the topic of news')
    a1=listen()
    a=requests.get(f'https://newsapi.org/v2/everything?q={a1}&from={date}&sortBy=publishedAt&apiKey=12ab853afc184767a2ced22221022ecf')
    news=json.loads(a.text)
    ret_news(news,a2)
    again(news,a2)

def weathr():
    speak('enter the city of india')
    city=listen()
    a=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},%20IN&appid=cd2870d58ff85291c9b749445e6d09c9')
    weather_api_data=json.loads(a.text)
    des=weather_api_data    [0]['description']
    temp=(int(weather_api_data['main']['temp']))-273.15
    hume=weather_api_data['main']['humidity']
    response=f'''temperature        :- {temp:.2f}
humidity           :- {hume}
weather conditions :- {des}'''
    speak(response)

def run():
    speak("""how can i help you
joke
news
time
date 
weather
exit""")
    a=listen()
    match a:
        case 'joke':
            jok()
            run()
        case 'news':
            news()
        case 'time':
            speak(f'time is {tim}')
            run()
        case 'date':
            speak(f'date is {date}')
            run()
        case 'weather':
            weathr()
            run()
        case 'exit':
            print('Bye...')
        case _:
            run()

x=f'''hello shashank
today\'s date is 
{date} 
and time is 
{tim} '''

def main(x):
    speak(x)
    run()

main(x)