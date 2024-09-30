import pyttsx3
import subprocess
import webbrowser
import smtplib
import json
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import time
import sys
from playsound import playsound
from urllib.request import urlopen
from googlesearch import search
import os
import smtplib
from testing2 import email_func,email_pass

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Waiting For a Command from You")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio)
        print('User: ' + cmd + '\n')
    except sr.UnknownValueError:
        speak('Sorry  i did not get that , do you mind typing your command')
        cmd = str(input('User: '))
    return cmd
name = 'Lexin'

engine = pyttsx3.init()

client = wolframalpha.Client('5V2PPK-YUPUP6AW6Q')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(name.upper() +':' + audio.upper())
    engine.say(audio)
    engine.runAndWait()

def Welcome():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

Welcome()
spk = ['how can i help you','do you need any help','hey do u need some help','Hi Lexin here , Ready to help you']
speak(random.choice(spk))
speak("I can help you with your Homeworks, you can use me to send a mail to your friends, playing songs, you can ask me to make a txt file, i can help you to buy your products and foods")

if __name__ == '__main__':

    while True:
        cmd = Command();
        cmd = cmd.lower()
        if 'open youtube' in cmd or'lexin open youtube' in cmd:
            speak('okay,opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'i am fine how are you' in cmd or 'i am fine' in cmd or 'i am good' in cmd:
            speak("good , im too fine")
        elif 'lexin laugh' in cmd or 'lexin laugh once more' in cmd or 'lexin lol' in cmd or 'lol' in cmd or 'giggle' in cmd or 'laugh' in cmd or 'lol' in cmd  or 'laugh again' in cmd or 'laugh once again' in cmd or 'can you laugh again' in cmd or 'laugh once more' in cmd or 'entertain me' in cmd :
            speak("hahahahahaha")

        elif 'search google' in cmd or 'browse' in cmd or 'lexin search' in cmd or 'What is' in cmd:
              speak("alright,what should i search for")
              search= Command()
              speak("ok searching for "+search)
              webbrowser.open("https://www.google.com/search?client=firefox-b-d&q= "+search)

        elif 'open google'in cmd or 'google' in cmd or 'lexin open google' in cmd:
            speak('okay,opening google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in cmd or 'gmail' in cmd or 'lexin open gmail' in cmd:
            speak('okay,opening gmail')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in cmd or 'how are you' in cmd or 'hi lexin , how are you' in cmd:
            stMsgs = ['i am good as always','i am fine , thanks for asking' ,'it depends on your internet connection' , 'i am good']
            speak(random.choice(stMsgs))

        elif 'nothing' in cmd or 'die' in cmd or 'abort' in cmd or 'stop' in cmd or 'lexin stop' in cmd or 'close' in cmd or 'lexin close' in cmd or 'quit' in cmd:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()
            
        elif 'bye' in cmd or 'good bye' in cmd or 'tata' in cmd or 'bruh bye' in cmd or 'bye lexin' in cmd:
            speak('Bye, have a good day.')
            sys.exit()

        elif 'hey lexin how are you' in cmd   or 'lexin how was your day' in cmd or 'how was your day' in cmd or 'how is your day going' in cmd or 'how are you' in cmd:
            opt=[' i\'m good ','fine','good','i had a fine day']
            speak(random.choice(opt))

        elif "who created you" in cmd or "who is your creator" in cmd or "who was your creator" in cmd or "who is the owner of lexin" in cmd or 'by whom were you created' in cmd or 'who owns you' in cmd :
            speak('I am created by a group of inventors ')#You can change someone. to something you wish


        elif "what is your name" in cmd or "can i know your name please " in cmd or "Hey lexin what is your name" in cmd or 'hi  what is your name' in cmd or ' can i know your name' in cmd or ' hey what is your name' in cmd:
               speak('MY name is lexin')
        elif"What is your age " in cmd or "can i know your age please " in cmd or "Hey lexin what is your age" in cmd or 'age' in cmd or 'can i know your age' in cmd or ' hi can i know your age' in cmd or ' hey what is your age' in cmd:
                speak(" i was just born")

        elif "where is your home" in cmd or "where were you born " in cmd or "where do you live " in cmd or 'where is your house' in cmd or  'in which place do you live' in cmd or 'where is your house located in ' in cmd or ' where is your home located in' in cmd or 'what is your address' in cmd or ' what is your house address' in cmd or 'what is your home addess' in cmd:
               speak("i Live in your internet connection")

        elif 'what is your job' in cmd or 'what is the job you are doing' in cmd or 'can i what work are you doing' in cmd or 'can you tell me what\'s your work' in cmd or 'are you carrying on any job' in cmd :
                sts=['i\'m working as a voice assistant to you ' , 'i\'m commited to job as a assistant to help you']#you can also change these statements if it's not good
                speak(random.choice(sts))

        elif 'who are you'in cmd or 'who the heck are you'in cmd:
            speak("I am Lexin , your voice assistant here to assist you")

        elif 'hey ,whats up' in cmd or 'how are you' in cmd:
            speak("i am good as always")

        elif "how do i change your voice" in cmd or "change your voice" in cmd or "change voice" in cmd or "voice change in cmd" in cmd:
             speak(" i am sorry about it , but my voice is fine")

        elif 'are you married' in cmd or 'do you have a girlfriend' in cmd:
            speak(" i am married to my work")

        elif "can you get me to instagram" in cmd or "i want to make a post in my instagram account" in cmd or "lexin take me to instagram" in cmd or "can you please take me to instagram" in cmd:
            speak("OK, taking you to instagram.com")
            speak("Please wait for seconds")
            webbrowser.open_new_tab("https://www.instagram.com/")

        elif "can you take me to facebook" in cmd or "i want to make a status in facebook" in cmd or "lexin take me to facebook" in cmd :
            speak("opening facebook.com")
            speak("Please wait for seconds")
            webbrowser.open_new_tab("https://www.facebook.com/")

        elif "can you recommend the best programming language to be learnt" in cmd or "can you guide me which is the best programming language" in cmd or "which is the best programming language " in cmd or "Trending programming languages" in cmd:
            speak("i will recommend you to learn Python as it is the most user friendly and easiest programming language which gives more job oppurtunities")
            speak("or else you can learn java script, swift, java, c, c++ or php")

        elif"search youtube" in cmd or "play a  song on youtube"in cmd or "play a song in youtube" in cmd or"search youtube" in cmd or "search for a video in youtube" in cmd or "search a video"  in cmd or "play a video on youtube" in cmd:
            speak("alright what  do i need to search for")
            song = Command()
            webbrowser.open("https://www.youtube.com/results?search_query="+song)

        elif"play another music" in cmd or "i want to hear some music" in cmd or "play some songs" in cmd or "play a song" in cmd or "sing a song" in cmd:
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=b08bf9b6431949af")

        elif "open whatsapp" in cmd or  "whatsapp" in cmd:
            speak("alright opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")

        elif "tell me a joke" in cmd or  "please tell me a joke" in cmd or  "crack a joke" in cmd:
            joke = ["Hey Rachyl, do you remember me? Person 2: Wrong number. Person 1: What’s your number then?","Mom: How make chicken Daughter: What? Mom: Where buy chicken Daughter: Mom, this isn’t Google. Mom: Avocado"]
            speak(random.choice(joke))

        elif 'wikipedia' in cmd:
            speak('Searching Wikipedia...')
            cmd = cmd.replace("wikipedia", "")
            results = wikipedia.summary(cmd, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open stackoverflow' in cmd:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")
        elif "what's your name" in cmd or "What is your name" in cmd:
            speak("My friends call me")
            speak("Lexin")
            print("My friends call me Lexin")
        elif "calculate" in cmd:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = cmd.lower().split().index('calculate')
            cmd = cmd.split()[indx + 1:]
            res = client.cmd(' '.join(cmd))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "who i am" in cmd or "who am i" in cmd:
            speak("If you are talking  then definately your human.")

        elif "why you came to world" in cmd:
            speak("Thanks to those who invented me , further it is a secret")

        elif 'shutdown system' in cmd or "shut down my laptop" in cmd :
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "don't listen" in cmd or "stop listening" in cmd or "pause" in cmd :
            speak("for how much time you want to stop Lexinfrom listening commands")
            a = int(Command())
            time.sleep(a)
            print(a)
        elif "restart" in cmd or "restart my laptop" in cmd:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in cmd or "sleep" in cmd:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in cmd or "sign out" in cmd:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in cmd:
            speak("What should i write")
            note = input()
            file = open('lexin.txt', 'a')
            speak("Should i include date and time")
            snfm = input()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                file.write("\n"+strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write("\n"+note)
            print("The file is saved You can access it from the location "+os.getcwd()+"\\lexin.txt")
        elif "show note" in cmd or "show the note" in cmd:
            speak("Showing Notes")
            file = open("lexin.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "take me to twitter" in cmd or "can you take me to twitter" in cmd or "please get me to twitter" in cmd :
           speak("Ok taking you to twitter.com")
           webbrowser.open_new_tab("https://twitter.com/login?lang=en")

        elif "please take me to google" in cmd or "can you take me to google" in cmd or "i want to browse in google" in cmd:
            speak("Taking you to google.com")
            webbrowser.open_new_tab("https://www.google.com/")
        elif "i want to buy something" in cmd  or "i want to buy things in online" in cmd or "i want to buy things in online" in cmd or "i want to buy a" in cmd or "order in online" in cmd :
            speak('Do you want me to open in amazon or flipkart or snapdeal')
            choice = input()
            if choice.lower()!="amazon" and choice.lower()!="flipkart" and choice.lower()!="snapdeal":
                speak("That Was an Invalid Choice Choose Either Amazon or Flipkart or Snapdeal")
                choice = input()
            if choice.lower() == 'amazon':
                speak('What Do You Want To Buy :')
                obj = Command()
                webbrowser.open_new_tab('https://www.amazon.in/s?k=%s&ref=nb_sb_noss' % obj)
                speak('A New Tab Of Amazon With The Search Result Of Object You Have To Buy')
            elif choice.lower()=='flipkart':
                speak('What Do You Want To Buy :')
                obj = Command()
                webbrowser.open_new_tab('https://www.flipkart.com/search?q=%s&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off' % obj)
                speak('A New Tab Of Flipkart With The Search Result Of Object You Have To Buy')
            elif choice.lower()=='snapdeal':
                webbrowser.open_new_tab('http:\\www.snapdeal.com')
                speak('A New Tab Of Snapdeal With The Search Result Of Object You Have To Buy')
        elif 'i want to eat something' in cmd or 'i\'m hungry' in cmd or 'i want some food' in cmd:
            speak("What food you Want?")
            food = input()
            speak("What's Your Choice for Food Delivery (Swiggy/Zomato)?")
            domain = input()
            if domain.lower()!="swiggy" and domain.lower()!="zomato":
                speak("That Was an Invalid Choice Choose Either Zomato or Swiggy")
                domain = input()
            if "swiggy" in domain.lower():
                webbrowser.open_new_tab("https://www.swiggy.com/search?q="+food)
            elif "zomato" in domain.lower():
                speak('Please Specify your City?')
                place = input()
                webbrowser.open_new_tab("https://www.zomato.com/"+place.lower()+"/restaurants/"+food.lower()+"?category=1")
        elif 'hello' in cmd or 'hey there' in cmd or 'whats up' in cmd or 'hlo' in cmd or 'hello lexin' in cmd or 'hi lexin' in cmd or 'hi' in cmd or 'hola' in cmd or 'namaste' in cmd or'hai' in cmd or 'vanakkam' in cmd or 'vanakkam lexin' in cmd or 'hola lexin' in cmd:
            speak('Hello User')
        elif "send a email" in cmd or "send email" in cmd or "send a mail" in cmd or "send mail" in cmd or "send an email" in cmd or "send a gmail" in cmd or "send gmail" in cmd:
            gmail_user = email_func()
            gmail_password = email_pass()
            speak("Please enter to whom I should send a mail\n")
            to=input("TO:")
            
            speak("Enter the body of the email\n")
            body = input("BODY:")
            
            try:  
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(gmail_user, to, body)
                server.close()
                speak ('Email sent!')
            except:
                speak("Sorry something went wrong, make sure you enter the correct receiver's email address")


        else:
            cmd = cmd
            try:
                try:
                    res = client.query(cmd)
                    results = next(res.results).text
                    speak(results)
                except:
                    results = wikipedia.summary(cmd, sentences=2)
                    speak(results)
            except:
                speak("Sorry i am not sure about it , i am still in  developing stage ")
