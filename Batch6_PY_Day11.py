#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Name:
    def createname(self,name):
        self.name = name
        
    def displayname(self):
        return self.name
    
    def saying(self):
        print(f"hello {self.name}")


# In[2]:


first = Name()


# In[3]:


first.createname('shareef')


# In[4]:


first.displayname()


# In[5]:


first.saying()


# In[6]:


second = Name()


# In[7]:


second.createname('vikrant')


# In[8]:


second.displayname()


# In[9]:


second.saying()


# In[10]:


class parentclass:
    var1 = 'Naveed'
    var2 = 'Rafeeq'
    
class childclass(parentclass):
    pass


# In[11]:


parobj = parentclass()


# In[12]:


parobj.var1


# In[15]:


parobj.var2


# In[17]:


choj = childclass()


# In[18]:


choj.var1


# In[19]:


class parent:
    std1 = 'Rohid'
    std2 = 'Kaleem'
    std3 = 'Majid'

class child(parent):
    std3 = 'Ahmed'


# In[20]:


pobj = parent()


# In[21]:


pobj.std3


# In[22]:


cobj = child()


# In[23]:


cobj.std1


# In[24]:


cobj.std2


# In[25]:


cobj.std3


# In[36]:


class Mom:
    var1 = 'hey i am Mom'
class Dad:
    var2 = 'hey i am Dad'
class child(Mom,Dad):
    var3 = 'hey i am your son'


# In[37]:


cobj = child()


# In[38]:


cobj.var1


# In[39]:


cobj.var2


# In[40]:


cobj.var3


# In[ ]:





# In[ ]:





# In[ ]:




