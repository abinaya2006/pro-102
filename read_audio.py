from gtts import gTTS

import os

path=input("Enter the file you want to hear: ")
a=open(path,"r")

read_text=a.read()

language="en"

output=gTTS(text=read_text, lang=language,slow=False)

output.save("audio.mp3")
os.system("start audio.mp3")