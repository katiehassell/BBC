
# coding: utf-8

# In[1]:


import numpy as np
#We assume that we are given a finite matrix for our initial state.


# In[2]:


#we create a function for adding 2 rows and columns of zeros at the edges of the grid. This will give the sense of an infinite grid. 
def add_rows(matrix):
    x=np.zeros((1,len(matrix[0])),dtype=int)
    matrix = np.insert(matrix,0,x,axis=0) #add row of zeros at the top
    matrix = np.insert(matrix,0,x,axis=0) #add row of zeros at the top
    matrix = np.insert(matrix,int(len(matrix)),x,axis=0) #add row of zeros at the bottom
    matrix = np.insert(matrix,int(len(matrix)),x,axis=0) #add row of zeros at the bottom
    return matrix
    
def add_cols(matrix):
    y=np.zeros((1,len(matrix)),dtype=int)
    matrix = np.insert(matrix,0,y,axis=1) #add column of zeros at the beginning
    matrix = np.insert(matrix,0,y,axis=1) #add column of zeros at the beginning
    matrix = np.insert(matrix,int(len(matrix[0])),y,axis=1) #add column of zeros at the end
    matrix = np.insert(matrix,int(len(matrix[0])),y,axis=1) #add column of zeros at the end
    return matrix


# In[3]:


#function to find the neighbours of a cell (the cells horizontally, vertically or diagonally adjacent).
#We don't check the border of the grid as we know no activity will happen here. This means we avoid the problem of finding neighbours on the edges.
def neighbours(matrix,i,j):
    neighbours = [matrix[i+1][j],matrix[i-1][j],matrix[i][j+1],matrix[i][j-1],matrix[i+1][j+1],matrix[i-1][j-1],matrix[i+1][j-1],matrix[i-1][j+1]]
    return neighbours
            


# In[4]:


#function to find how many neighbours that are live cells a cell has
def live_neighbours(matrix,i,j):
    live_neighbours = 0
    for x in (neighbours(matrix,i,j)):
              live_neighbours += x #We do this by adding the value of the neighbours as live cells are given value 1 and dead cells 0 
    return live_neighbours


# In[5]:


#function to make a cell live
def live_cells(matrix,i,j):
    matrix[i][j]=1
    return matrix


# In[6]:


#function to kill a cell
def kill_cells(matrix,i,j):
    matrix[i][j]=0
    return matrix


# In[7]:


#function for the scenarios
def scenarios(matrix,d,l):
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1): #iterate over all cells
            if matrix[i][j]==1: #if the cell is alive,
                if int(live_neighbours(matrix,i,j))<2: #scenario 1
                    d.append((i,j)) #add cells to list of cells to die
                elif int(live_neighbours(matrix,i,j))>3: #scenario 2
                    d.append((i,j)) #add cells to list of cells to die
                elif int(live_neighbours(matrix,i,j))==2 or int(live_neighbours(matrix,i,j))==3: #scenario 3
                    l.append((i,j)) #add cells to list of cells to live
            elif matrix[i][j]==0: #if the cell is dead
                if int(live_neighbours(matrix,i,j))==3:  #scenario 4
                    l.append((i,j)) #add cells to list of cells to live
                    #we don't need to include anything for scenario 0 as this is a given
   


# In[8]:


def play(t):
    s = t
    cells_to_die = [] #create an empty list for cells to die
    cells_to_live = [] #create an empty list for cells to live
    s = add_rows(s) #add rows to our initial matrix to make the grid "infinite". We add 2 rows so we know no activity will happen on the edges
    s = add_cols(s) #add cols to our initial matrix to make the grid "infinite". We add 2 cols so we know no activity will happen on the edges
    scenarios(s,cells_to_die,cells_to_live) #call scenario function to find which cells will live and die after this turn
    for x in cells_to_die:
        s = kill_cells(s,x[0],x[1]) #call kill cells function to kill these cells
    for x in cells_to_live:
        s = live_cells(s,x[0],x[1]) #call live cells function to show still living/created cells
    return s


# In[9]:


a=np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
a


# In[10]:


a=play(a)
a


# In[ ]:



    

