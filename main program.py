listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1] .id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone()as source:
            talk("Hii I am your voice assistant")
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if'alexa' in command:
                command = command.replace("alexa", " ")
                print(command)
    except:
        pass
    return command



def run_alexa():
    command = take_command()
    print(command)
    print(command)
    if "hello" in command:
        talk("Hello! How can I assist you?")
    elif "goodbye" in command:
        talk("Goodbye!")
    elif "play" in command:
        song = command.replace("play", " ")
        talk("Playing"+song)
        pywhatkit.playonyt(song)

    elif"date" in command:
        today = datetime.date.today()
        print(today)
        talk(today)

    elif"time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("The current time is "+time)
    elif 'what is ' in command:
        person = command.replace('what is ','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif "send message to" in command:
        message = command.replace("send message to",' ')
        pywhatkit.sendwhatmsg(message,"Happy birthday",10,51)
        talk(message)
    elif"search for" in command:
        message = command.replace("search for"," ")
        talk("Searching...."+message)
        pywhatkit.search(message)

run_alexa()
