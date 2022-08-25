#!/usr/bin/env python
# coding: utf-8

# In[10]:


import math


# ### Times Function

# In[11]:


def times(start, stop):
    times = []
    ran = int( 4*(stop - start)/100 + 1 )
    print(ran)
    for i in range(0, ran): 
        if (start % 100) == 60: 
            start += 40
        times.append(start)
        start += 15
    return times


# In[13]:


input1 = [('1', 'A', 'B'), ('2', 'B', 'D'), ('3', 'B', 'E'), ('4', 'A', 'C'), ('5', 'D', 'M'), ('6', 'C', 'F'), ('7', 'F', 'G'), ('8', 'G', 'H'), ('9', 'H', 'I'), ('10', 'I', 'J'), ('11', 'I', 'K'), ('12', 'J', 'L'), ('13', 'D', 'K'), ('14', 'K', 'L'), ('15', 'L', 'M'), ('16', 'M', 'N'), ('17', 'E', 'N'), ('18', 'N', 'O'), ('19', 'D', 'F'), ('20', 'G', 'K')]


# ### Edges Function

# In[14]:


def edgeslist(input):
    output=[]
    length = len(input)
    for i in range(0, 2*length):
        output.append(input[math.floor(i/2)][0]+input[math.floor(i/2)][(i%2) + 1])
    return output


# ### Traffic Conditions Function

# In[15]:


def traffic(times, edges):
    output = []
    for j in range(len(times)):
        print('You are entering conditions for', times[j])
        for i in range(len(edges)):
            condition = input("Enter the traffic condition for edge "+ edges[i]+ ": ")
            element = [600, edges[i], condition]
            output.append(element)
    return output

