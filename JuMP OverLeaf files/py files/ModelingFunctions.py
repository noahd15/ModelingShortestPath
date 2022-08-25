#!/usr/bin/env python
# coding: utf-8

# In[1]:


def explain():
    String = print('IMPORTED FUNCTIONS: \n\n times(start, stop): creates list of times to record data for input has all nodes and their edges \n\n edgeslist(input1): outputs the edge labels as seen in the Labeled Map of Knoxville\n\n traffic(times, edges): allows user to input traffic conditions and outputs as a list\n\n trafficTxt(times, edges, filename="TrafficConditions.txt", accessmode="w+") saves as file\n\n timeEachNode (distances, trafficConditions, timeOfDay, Day="Sun") outputs a list of weights of each edge\n\n timeEachNodeTxt (distances, trafficConditions, timeOfDay, Day="Sun", filename = "NodeWeights.txt", \n accessmode = "w+") saves as file')
    return String
explain()


# In[2]:


import math


# ### Times Function
# ##### creates a vector of the times I get data from traffic simulator. See example output. 

# In[3]:


def times(start, stop):
    times = []
    ran = int( 4*(stop - start)/100 + 1 )
    for i in range(0, ran): 
        if (start % 100) == 60: 
            start += 40
        times.append(start)
        start += 15
    return times


# In[4]:


#creates vector of times from 6:00 am to 7:00 am 
extimes = times(600, 700)


# In[5]:


# nodes with each possible edge
input1 = [('1', 'A', 'B'), ('2', 'B', 'D'), ('3', 'B', 'E'), ('4', 'A', 'C'), ('5', 'D', 'M'), ('6', 'C', 'F'), ('7', 'F', 'G'), ('8', 'G', 'H'), ('9', 'H', 'I'), ('10', 'I', 'J'), ('11', 'I', 'K'), ('12', 'J', 'L'), ('13', 'D', 'K'), ('14', 'K', 'L'), ('15', 'L', 'M'), ('16', 'M', 'N'), ('17', 'E', 'N'), ('18', 'N', 'O'), ('19', 'D', 'F'), ('20', 'G', 'K')]


# ### Edges Function
# ##### given a list of nodes with each possible edge, prints out the edge labels as seen in the Labeled Map of Knoxville below

# In[6]:


def edgeslist(input1):
    out=[]
    length = len(input1)
    for i in range(0, 2*length):
        out.append(input1[math.floor(i/2)][0]+input1[math.floor(i/2)][(i%2) + 1])
    return out


# In[7]:


exinput = [('1', 'A', 'B'), ('2', 'B', 'C'), ('3', 'A', 'C')]
edgeslist(exinput)


# ## insert HodgesNeyland image here. 

# ### Traffic Conditions Function
# ##### given the times and edges from the previous 2 functions, allows the user to input the traffic conditions for each edge, and saves and outputs those conditions into a list. 

# In[8]:


def traffic(times, edges):
    output = []
    for j in range(len(times)):
        print("You are entering conditions for {0}. Or enter 'Q' to quit. Your progress will be saved and returned.".format(times[j]))
        for i in range(len(edges)):
            condition = input("Enter the traffic condition for edge "+ edges[i]+ ": ")
            while condition != "G" and condition != "O" and condition!="R" and condition!="B" and condition!="NA":
                if condition == "Q":
                    print("Quitting program.")
                    return output
                print("Invalid input. Enter G for green, O for orange, R for red, B for brown, and NA if not available.")
                condition = input("\n Enter the traffic condition for edge " + edges[i]+ ": ")
            element = [times[j], edges[i], condition]
            output.append(element)
    return output


# In[9]:


# traffic(extimes, exedges)


# In[10]:


def trafficTxt (times, edges, filename="TrafficConditions.txt", accessmode="w+"):
    file = open(filename, accessmode)
    for j in range(len(times)):
        print("You are entering conditions for {0}. Or enter 'Q' to quit. Your progress will be saved.".format(times[j]))
        for i in range(len(edges)):
            condition = input("Enter the traffic condition for edge "+ edges[i]+ ": ")
            while condition != "G" and condition != "O" and condition!="R" and condition!="B" and condition!="NA":
                if condition == "Q":
                    print("Quitting program.")
                    file.close()
                    return
                print("Invalid input. Enter G for green, O for orange, R for red, B for brown, and NA if not available.")
                condition = input("\n Enter the traffic condition for edge " + edges[i]+ ": ")
            element = "%s %s %s \n" %(times[j], edges[i], condition)
            file.write(element)
    file.close()   


# In[11]:


# trafficTxt(extimes, exedges, "exTrafficConditions.txt")


# In[12]:


## list of all distances of edges in feet

distancesDict = dict([('1A', 377), ('1B', 377), ('2B', 528), ('2D', 528), ('3B', 1056), ('3E', 1056), ('4A', 367), ('5D', 528), ('5M', 528), ('6C', 430), ('6F', 430), ('7F', 400), ('7G', 400), ('8G', 302), ('8H', 302), ('9H', 528), ('9I', 528), ('10I', 528), ('10J', 528), ('11I', 300), ('11K', 300), ('12J', 318), ('12L', 318), ('13K', 350), ('13D', 350), ('14K', 528), ('15L', 400), ('15M', 400), ('16M', 2112), ('16N', 2112), ('17E', 528), ('17N', 528), ('18N', 528), ('18O', 528), ('19D', 528), ('19F', 528), ('20K', 528)])
distancesList = [('1A', 377), ('1B', 377), ('2B', 528), ('2D', 528), ('3B', 1056), ('3E', 1056), ('4A', 367), ('5D', 528), ('5M', 528), ('6C', 430), ('6F', 430), ('7F', 400), ('7G', 400), ('8G', 302), ('8H', 302), ('9H', 528), ('9I', 528), ('10I', 528), ('10J', 528), ('11I', 300), ('11K', 300), ('12J', 318), ('12L', 318), ('13K', 350), ('13D', 350), ('14K', 528), ('15L', 400), ('15M', 400), ('16M', 2112), ('16N', 2112), ('17E', 528), ('17N', 528), ('18N', 528), ('18O', 528), ('19D', 528), ('19F', 528), ('20K', 528)]


# ### timeEachNode Function
# ##### Outputs a list of edges and their travel times, given the information from the traffic function. 

# In[13]:


def timeEachNode (distances, trafficConditions, timeOfDay, Day='Sun'): 
    length = len(distances)
    travelTimes = []
    test = []
    ctr = 0 
    for i in range(length):
        edge = distances[i][0]
        dist = distances[i][1]
        mint = timeOfDay % 100
        index = int (mint / 15 + ( (timeOfDay - mint) - 600 ) / 25 * 40 ) + ctr
        thisCond = trafficConditions[index][2]
        test.append([index, thisCond])
        Time = dist / 44
        traffic = trafficFunction(thisCond, Time)
        thisTravelTime = '{0}'.format(Time + traffic)
            # speed limit in Knoxville ~ 30 mph is 44 ft/s 
        travelTimes.append([edge, thisTravelTime])
        ctr += 1
    return(travelTimes)


# In[14]:


def timeEachNodeTxt (distances, trafficConditions, timeOfDay, Day='Sun', filename = "NodeWeights.txt", accessmode = "w+"):
    length = len(distances)
    ctr = 0 
    file = open(filename, accessmode)
    for i in range(length):
        edge = distances[i][0]
        dist = distances[i][1]
        mint = timeOfDay % 100
        index = int (mint / 15 + ( (timeOfDay - mint) - 600 ) / 25 * 40 ) + ctr
        thisCond = trafficConditions[index][2]
        Time = dist / 44
        traffic = trafficFunction(thisCond, Time)
        thisTravelTime = '{0}'.format(Time + traffic)
            # speed limit in Knoxville ~ 30 mph is 44 ft/s 
        file.write("%s %s" %(edge, thisTravelTime))
        ctr += 1


# In[15]:


def trafficFunction(trafficCond, Time):
    if trafficCond == 'G':
        traffic = 1.1*Time
    elif trafficCond == 'O':
        traffic = 1.25*Time
    elif trafficCond == 'R':
        traffic = 2*Time
    elif trafficCond == 'B':
        traffic = 3*Time
    elif trafficCond == 'NA': 
        traffic = 0
    return traffic 
# These are test numbers to see if the function works. 
# I will study the google maps times later to get more accurate functions

