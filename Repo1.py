#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyttsx3
from time import sleep

b = open("demo.txt", "r")
book = b.readlines()
engine = pyttsx3.init()

for i in book:
    engine.say(i)
    engine.runAndWait()
    sleep(2)

b.close()  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




