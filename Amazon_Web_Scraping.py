#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
import pandas as pd
import requests


# In[2]:


URL = "https://www.amazon.com/s?k=mini+pc&ref=nb_sb_ss_ts-doa-p_1_6"


# In[3]:


# Header for Requests 
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})


# In[4]:


# HTTP Request
webpage = requests.get(URL, headers=HEADERS)


# In[5]:


webpage


# In[7]:


type(webpage.content)


# In[8]:


soup = BeautifulSoup(webpage.content, "html.parser")


# In[9]:


# fetch links as a list of tag objects 
links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})


# In[13]:


link = links[0].get('href')


# In[14]:


product_list = "https://amazon.com" + link


# In[15]:


product_list


# In[16]:


new_webpage = requests.get(URL, headers=HEADERS)


# In[17]:


new_webpage


# In[18]:


new_soup = BeautifulSoup(webpage.content, "html.parser")


# In[19]:


new_soup


# In[27]:


new_soup.find("span", attrs={"id":"productTitle"})


# In[25]:


new_soup.find("span", attrs={"class":"a-price a-text-price a-size-medium"}).find("span", attrs={"class":"a-offscreen"}.text)


# In[28]:


new_soup.find("span", attrs={"id":"a-icon-alt"})


# In[ ]:




