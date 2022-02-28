#!/usr/bin/env python
# coding: utf-8

# In[72]:


import numpy as np
from sage.crypto.util import ascii_to_bin
from sage.crypto.util import bin_to_ascii
G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
C = LinearCode(G)
x = ascii_to_bin("timpil")
print("binary of input",x)
#y=bin_to_ascii(x)
#print(y)
timpil = [int(digit) for digit in str(x)]
print(timpil)


# In[73]:


length = len(timpil)
split = length / 4
splits = np.array_split(timpil, split)
output=[]
for i in splits:
    print(i)
    word = vector(GF(2), (i)) 
    E = codes.encoders.LinearCodeGeneratorMatrixEncoder(C)
    encoder = E.encode(word)
    output.append(encoder)
    print("encodeded",encoder)


# In[74]:


#decoder


# In[75]:


print(output)


# In[76]:


final=[]
for x in output:
    word = vector(GF(2), (x))
    #w_err = word + vector(GF(2), (1, 0, 0, 0, 0, 0, 0))
    D = C.decoder()
    last= (D.decode_to_message(word))
    print(last)
    final.append(last)


# In[77]:


print(timpil)
len(timpil)


# In[78]:


print(final)


# In[79]:


test=[]
for x in final:
    #print(x)
    for y in x:
        test.append(y)
        print(y)


# In[80]:


print(test)


# In[81]:


st = ''.join(str(e) for e in test)
print(st)
len(st)


# In[82]:


y= bin_to_ascii(st)
print(y)


# In[ ]:




