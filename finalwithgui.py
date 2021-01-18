import pyttsx3
#import PIL.Image,PIL.ImageTk
import datetime
from tkinter import  *
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import pyautogui
import time
#from PIL import Image
import pyautogui
import mysql.connector


#for import voice of computer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


global root
root=Tk()
global var
var=StringVar()

#function for speak a string
def speak(audio):
    """This function is use to speak by the pc"""
    engine.say(audio)
    engine.runAndWait()

#funtion for stating(wish)
def wishme():
    """This is use to wish when you open the voice assistant"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<16:
        speak('good afternoon')
        
    else:
        speak('good evening')
    speak('I am jarvis, how I can Help You?')

#function for take command
def take_command():
    """ This is use to take command from the user"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        var.set('Listining...')
        root.update()
        print('listining...')
        r.energy_threshold=500
        #r.pause_threshold=0.5    
        audio=r.listen(source)
    try:
        print('recognising...')
        var.set('Recognising...')
        root.update()
        quary=r.recognize_google(audio,language='en-in')
        var.set('User Said: '+quary)
        root.update()
        print('User Said:',quary)
        time.sleep(1)
    except Exception as e :
        #print(e)
        var.set('Please say that again..')
        root.update()
        speak('i can not understand, please ,say that again')
        
        print('say again..')
        return 'None'
    return quary


#path of chrome for open in chrome
#it should be of your computer
browser=webbrowser.get('C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s')
#browser=webbrowser.get("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox %s")

def exit():
    

    """This is use to exist the pogram"""
    speak('bye, see you again')
    root.destroy()
    quit() 




def play():
    """This contain all condition for voice assistant"""
    while True:
        quary= take_command().lower()


                    
                    
#if not recognize
        if 'none'== quary:

            pass
                              

#for wikipedia
        elif 'wikipedia' in quary:
                try:
                    quary=quary.replace('wikipedia','')
                    result=wikipedia.summary(quary, sentences=2)                          
                    print(result)
                              
                    speak(f'according to wikipedia:{result}')
                    break
                except Exception as e :
                    #print(e)
                    speak('can not find please retry it')
                    var.set('can not find')
                    root.update()

#for opening youtube
        elif quary=='open youtube':
            var.set('Opening YouTube...')
            root.update()
            speak("opening youtube")                        
            browser.open('youtube.com')
            break

#for search on youtube
        elif 'on youtube' in quary:
            var.set('searching on YouTube...')
            root.update()
            speak("opening on youtube")
            quary=quary.replace('on youtube','')
            browser.open('https://www.youtube.com/results?search_query='+quary)
            break

#for opening google.com
        elif quary=='open google':
            var.set('Opening Google...')
            root.update()
            speak('opening google')                              
            browser.open('google.com')
            break

#for opening gmail
        elif 'open gmail' in quary:
            var.set('Opening Gmail...')
            root.update()
            speak('opening gmail')
            browser.open('gmail.com')
            break
#for usual talk
        elif 'how are you' in quary:
            var.set('I am Fine.')
            root.update()
            speak('i am fine, thank you')
            speak("what's about you?")
        elif 'i am fine' in quary:
            speak('okk')
            var.set('How can I help??')
            root.update()
            speak('how i can help you?')
        elif 'what you can do' in quary:
            speak('i can open youtube,i can search on wikipedia')
            speak('and if you are ofline then i can play downloaded song')
            speak('what you want')


#for exit from proggram
        elif 'exit' in quary:
            var.set('Bye, see you again.')
            root.update()
            time.sleep(1)
            exit()
            break
        
#for sleep the program
        elif 'sleep' in quary:
            var.set('To wakeup me press "PLAY"')
            root.update()
            break
                                


#for playing new gujarati song
        elif'play new gujarati' in quary:
            var.set('Playing new Gujarati song...')
            root.update()
            ran_guj_song = random.choice(range(1,5))
            new_guj_music_dir='E:\\new gujrati song'
            #here should be the path where the your download song save
            song=os.listdir(new_guj_music_dir)
            speak('playing new gujarati song') 
            print(song[ran_guj_song])
            os.startfile(os.path.join(new_guj_music_dir,song[ran_guj_song]))
            break
#for taking screenshoot
                    
        elif 'screenshot' in quary:
            var.set('Taking ScreenShort....')
            root.update()
            pyautogui.hotkey('win', 'prtsc')
            speak('screen shot taken succesfully')
            break

                      
#fro adding task in todo list             
        elif 'to do' in quary:
            var.set('what s the task?')
            root.update()
            mydb=mysql.connector.connect(host='127.1.0.0', user='root', password='passs', db='database', auth_plugin='mysql_native_password')
            mycur=mydb.cursor()
            while True:
                var.set('Whats the task?')
                speak('whats the task')
                quary= take_command().lower()
                if quary!= 'none':
                    re=(quary,)
                    sql='insert into task(task) values (%s)'
                    mycur.execute(sql,re)
                    mydb.commit()
                    var.set('Task added successfully')
                    root.update()
                    speak('task added successfully')

                    break
            break

# for opening python
        elif "coding" in quary:
            var.set("Opening python.")
            root.update()
            speak("let's do coding with python")
            py_dir="C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw"
            os.startfile(os.path.join(py_dir))
            break


#for the current time            
        elif 'the time' in quary:
            curtime=datetime.datetime.now().strftime("%H%M")
            var.set("It's...")
            root.update()
            speak(f'the time is:{curtime}')
            break

#for opening mozilla firefox
        elif "open firefox" in quary:
            var.set("Opening firefox..")
            root.update()
            speak("openig, mozilla firefox")
            firefox_dir='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox'
            os.startfile(os.path.join(firefox_dir))
            break
#for opening microsoft word
        elif 'open microsoft word' in quary:
            var.set("Opening Word..")
            root.update()
            speak('opening, microsoft word')
            word_dir='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007'
            
            os.startfile(os.path.join(word_dir))
            break
#for search  on google
        elif 'on google' in quary:
            var.set('Searching on google.com')
            x= quary.replace('on google', '')
            q='https://www.google.com/search?q='+x
            browser.open(q)
            break
#if no condition match then
        elif '' in quary:
            var.set('I can not do that')
            root.update()
            speak("I can't do that...")
            speak("if you want to search on google then, add on google in the quary")
            break
        

def play_again():
    """This is use to rerun program upon click the button """
    while True:
        speak('i am listing what you want?')
        play()

        break

def main_gui():

    """This is the main GUI of pogram"""
    
    root.title('Jarvis')

    
    
    
  

    def update(ind):
        """This is use to run GIF"""
        frame = frames[(ind)%35]
        ind += 1
        labelgif.configure(image=frame)
        root.after(100, update, ind)
    frames = [PhotoImage(file='C:\\Users\\Admin\\Desktop\\.py file\\jarvis with gui\\jarvis.gif',format = 'gif -index %i' %(i)) for i in range(35)]
#here the path should be of your computer where the gif is store

    label = Label(root, textvariable =var,fg='white' ,bg='black',font=('Helvetica',35))
    var.set('Welcome')
    label.pack()

    labelgif = Label()
    labelgif.config(bg='black')
    labelgif.pack()



    btna=Button(text='PLAY', width=30, command=play_again, fg='white',bg='black')
    btna.config(font=('Courier',20))


    btnb=Button(text='EXIT', width=30, command=exit,  fg='red',bg='black')
    btnb.config(font=('Courier',20))

    btna.pack()

    btnb.pack()

    root.after(1000,wishme)
    root.after(1001,play)


    root.config(bg='black')


    root.after(0, update, 0)
    root.mainloop()

main_gui()

