#!/usr/bin/env python
# coding: utf-8

# In[2]:


import librosa
import numpy as np
from time import strftime
from datetime import datetime
from IPython.display import Audio
import speech_recognition as sr 


def get_audio():
    """it goes through the recording and find the corresponding file, 
    then bind them together as numpy array"""
    
    curtime =  datetime.now().time().strftime("%I/%M /%S")
    split_time = curtime.split('/')
    hours, minutes,seconds = int(split_time[0]), int(split_time[1].split(' ')[0]),int(split_time[2].split(' ')[0])
    #give us the int type output of hour minute second
    
    start, sr = librosa.load("sounds/the_current_time_is.wav")
    hour_wav, sr = librosa.load(f"sounds/{hours}.wav")
    am_wav, sr = librosa.load(f"sounds/am.wav")
    pm_wav, sr = librosa.load(f"sounds/pm.wav")
    minute_wav, sr =  librosa.load(f"sounds/{minutes}.wav")  #this one is to avoid a error message of ealier reference
    
    if hours < 13:              #different binding pattern for different case
        if minutes == 0:
            ouput = np.concatenate((start, hour_wav,pm_wav))
        else:
            if seconds == 0:
                minute_wav,sr =  librosa.load(f"sounds/{minutes}.wav")
                output = np.concatenate((start, hour_wav, minute_wav, pm_wav))
            else:
                andwav,sr =  librosa.load(f"sounds/and.wav")
                second_wav, sr = librosa.load(f"sounds/{seconds}.wav")
                output = np.concatenate((start, hour_wav, minute_wav,andwav, second_wav, pm_wav))
    else:
        if minutes == 0:
            ouput = np.concatenate((start, hour_wav,am_wav))
        else:
            if seconds == 0:
                minute_wav ,sr =  librosa.load(f"sounds/{minutes}.wav")
                output = np.concatenate((start, hour_wav, minute_wav, am_wav))
            else:
                andwav,sr =  librosa.load(f"sounds/and.wav")
                second_wav,sr = librosa.load(f"sounds/{seconds}.wav")
                output = np.concatenate((start, hour_wav, minute_wav,andwav, second_wav, am_wav))
    return sr, output

r = sr.Recognizer()    #got the recognize function
m = sr.Microphone()    #activate the microphone

start = True
while(start):
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("please start speaking")
        audio = r.listen(source)
        Mytext = r.recognize_google(audio)
        Mytext = Mytext.lower()
        print(Mytext)
        if("time" in Mytext):
            sr, output = get_audio()
            start = False

Audio(output, rate=sr,autoplay=True)


# In[ ]:




