
# coding: utf-8

# In[1]:


print("hello python")


# In[2]:


#두 수를 더한다
x=4
y=5
z=x+y

print("Output #2: Four plus finve equals {0:d}.".format(z))


# In[3]:


#두 리스트를 더한다.
a=[1,2,3,4]
b=["first","second","third","fourth"]
c=a + b
print("output #3: {0},{1},{2}".format(a,b,c))


# In[1]:


x=9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))


# In[1]:


#3f는 소수점 셋째짜리까지 보여달라는 의미
print("Output #7:{0:.3f}".format(8.3/2.7))
y=2.5*4.8
print("Output #8:{0:.1f}".format(y))
#float 내장함수는 무엇인가 실수형을 강제하는 것이군
r=8/float(3)
print("Output #9:{0:.2f}".format(r))
print("Output #10:{0:.4f}".format(8.0/3))


# In[15]:


print("Output #9:{0:2f}".format(8/3))


# In[3]:


#!/usr/bin/env python3
from math import exp,log,sqrt
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))      
  


# In[4]:


print("Output #14:{0:s}".format('I\'m enjoying learning Python.'))


# In[5]:


print("Output #14:{0:s}".format("I'm enjoying learning Python."))


# In[9]:


print("Output #15:{0:s}".format("This is a long string. Without the backslashit would run off of the page on the right in the text editor and be verydifficult to read and edit.By using the backslash you can split the longstring into smaller strings on seperate lines so that the whole string is easyto view in the text editor."))                        


# In[11]:


print("Output #16:{0:s}".format('''you can use triple single quotes 
for multi-line comment strings.'''))


# In[14]:


print("Output #17:{0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))


# In[ ]:


string1="This is a"
string2="short string."
sentence=string1+string2
print("Output #18:{0:s}".format(sententce))

