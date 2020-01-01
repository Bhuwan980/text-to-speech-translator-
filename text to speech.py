# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:18:31 2019

@author: cousi
"""
import os
import gtts

data = input("enter text to conver into audio: ")
audio = gtts.gTTS(data,lang="en",slow=False)
audio.save("name.wav")
os.system("name.wav")