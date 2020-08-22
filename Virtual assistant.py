import pyttsx3
import webbrowser
import os

pyttsx3.speak("Welcome to the vitual assistant . I can help you out with your requirements ")


while True:
    s=input("What can I do for you:")
    print("=======================================================================================")
    if (("run" in s)or("start" in s )or("unlock" in s )or("execute" in s )or("play" in s )or("open" in s )or("unwrap" in s )or
                ("free" in s )or("show" in s )or("begin" in s )or("present" in s )or("produce" in s )or("launch" in s )or
                ("unveil" in s )or("turnon" in s )or("disclose" in s ))and(("app" in s)or("application" in s) ) :

        p=input("Which App do you want to open:")
        print("=======================================================================================")

        if (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )or
                ("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and(("chrome" in p)or("google chrome" in p) ) :
            pyttsx3.speak("Opening Google chrome")
            os.system("start chrome")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
            or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and(("notepad" in p) or("editor" in p) ) :
            pyttsx3.speak("Opening Google Notepad")
            os.system("start notepad")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and(("media" in p)or("player" in p)):
            pyttsx3.speak("Opening media player")
            os.system("start wmplayer")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and(("cmd" in p)or("command prompt" in p)):
            pyttsx3.speak("Opening command prompt")
            os.system("start cmd")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and("paint" in p):
            pyttsx3.speak("Opening microsoft paint")
            os.system("start mspaint")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("calculator" in p):
            pyttsx3.speak("Opening Claculator")
            os.system("start calc")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("internet explorer" in p):
            pyttsx3.speak("Opening Internet explorer")
            os.system("start iexplore")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("microsoft outlook" in p)or("outlook" in p)):
            pyttsx3.speak("Opening microsoft outlook")
            os.system("start outlook")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("microsoft powerpoint" in p)or("powerpoint" in p)):
            pyttsx3.speak("Opening microsoft powerpoint")
            os.system("start powerpnt")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("this pc" in p)or("pc" in p)):
            pyttsx3.speak("Opening This PC")
            os.system("start explorer")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("magnifier" in p)or("magnify" in p)):
            pyttsx3.speak("Opening magnifier")
            os.system("start magnify")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("wordpad" in p):
            pyttsx3.speak("Opening wordpad")
            os.system("start write")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("photoshop" in p):
                pyttsx3.speak("Opening photoshop")
                os.system("start photoshop")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("microsoft word" in p)or("word" in p)):
            pyttsx3.speak("Opening words")
            os.system("start winword ")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and (("excel" in p) or("microsoft excel" in p) ):
            pyttsx3.speak("Opening microsoft excel")
            os.system("start excel ")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("illustrator" in p):
                pyttsx3.speak("Opening illustrator")
                os.system("start Illustrator")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("adobe reader" in p):
            pyttsx3.speak("Opening acrobat")
            os.system("start acrobat")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("task manger" in p):
            pyttsx3.speak("Opening task manager")
            os.system("start taskmgr")

        elif (("run" in p)or("start" in p )or("unlock" in p )or("execute" in p )or("play" in p )or("open" in p )or("unwrap" in p )
                or("free" in p )or("show" in p )or("begin" in p )or("present" in p )or("produce" in p )or("launch" in p )or
                ("unveil" in p )or("turnon" in p )or("disclose" in p ))and ("camera" in p):
            pyttsx3.speak("Opening camera")
            os.system("start microsoft.windows.camera:")
        else:
            print("dont support")


    elif (("search" in s) or ("find" in s) or ("browse" in s))and(("keyword" in s) or ("word" in s) or ("something" in s) 
                                                                  or ("text" in s)):
        p=input("Enter the text/key word that you want to seach on web")
        print("=======================================================================================")
        pyttsx3.speak("Searcing the keyword on web:")
        url = "https://www.google.com.tr/search?q={}".format(p)
        webbrowser.open_new_tab(url)



    elif (("search" in s) or ("find" in s) or ("browse" in s))and(("url" in s) or ("address" in s)):

        p=input("enter the url you want to search on web:")
        print("=======================================================================================")
        pyttsx3.speak("Searcing the url on web")
        webbrowser.open_new_tab(p)


    elif (("exit" in s)or("close" in s)or("stop" in s)or("end" in s)or("abort" in s)or("conclude" in s)or 
            ("terminate" in s) or  ("wind-up" in s) or  ("finsih" in s) or  ("turn-off" in s) or("quit" in s)or
            ("withdraw" in s)or("leave" in s)or("escape" in s)or("halt" in s)or("break-down" in s)or("cease" in s)):
        pyttsx3.speak("Thank you so much for using me")
        break
        
    else:
        print("Sorry! I couldn't help out with that ... Please Try again")
