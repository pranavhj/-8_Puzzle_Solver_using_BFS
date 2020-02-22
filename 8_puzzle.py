# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:34:35 2020

@author: prana
"""
import numpy as np
def puzzle():
    maze= np.array([[1,2,3],[4,0,5],[6,7,8]])
    
   
    return maze

def checkifSolvable(maze):                         #Checks if the maze is solvable or not
     maze_=np.resize(maze,(1,9))
    
     inv_count=0
     
     for i in range(len(maze)*len(maze)):                 #iterate and check the inv count
         for j in range(i+1,9):
             if maze_[0][i]!=0  and  maze_[0][j]!=0   and   maze_[0][i]>maze_[0][j]:
                 inv_count=inv_count+1
     #print(inv_count) 
     if inv_count%2==0:
         return True
     else:
         return False
     
def checkSolved(maze):                                         #checks if the maze passed as argument is solved or not
    maze_=np.resize(maze,(1,9))
    #print(maze_)
    #maze_=maze_[maze_!=0]
    #print(maze_)
    #maze_1=np.sort(maze_)
    maze_2=np.array([[1,2,3,4,5,6,7,8,0]])
    #print(maze_1)
    if np.array_equal(maze_,maze_2)==True:
        return True
    else:
        return False
    
def check_list(lists,instance):                             #checks if the instance is present in lists
    instance=np.resize(np.asarray(instance),(1,9))
    for i in range(len(lists)):                             #iterate through the lists to check the elements
        if np.array_equal(instance,lists[i])==True:
            return True
    return False
                 
                 
    
            
def bfs_solver(maze):                                       #Function to solve the maze passed as argument
    
    if checkifSolvable(maze)==False:
        print("Not Solvable")
        return False
    
    print(maze)
    file1 = open("nodePath.txt","w")                       #Open the file nodePath
    file1.truncate()                                             #erase all the content in the file1
    file2 = open("Nodes.txt","w")                                 
    file2.truncate()                                    #erase all the content in the file1
    file3 = open("NodesInfo.txt","w")
    file3.truncate()
    maze_=np.resize(maze,(1,9))
    maze_size=np.array([])
    
    queue=[]                               
    path=[]
    visited=[]
    queue.append(maze_)
    counter=0                             #initialize a counter to count no of iterations
    parents=[]
    prev_maze_=queue[0]                                     #pass first element of queue into variable prev_maze
    visited_dash=[]
    Write(file1,np.resize(np.transpose(np.resize(maze_,(3,3))),(1,9)))                                 #write maze_ into file1
   
    while len(queue)!=0:
        flag=0
        
        #print((np.shape(queue)))
        #current_maze_=queue[len(queue)-1]
                
        current_maze_=queue.pop(0)                            #Pop the first value of the queue into current_maze_
        
        #print("Currentmaze")
        #print(np.resize(current_maze_,(3,3)))
        #print(" ")
        #print("Currentmaze")
       
        path.append([current_maze_,prev_maze_])               #add [current_maze_,prev_maze_] to path
        
        #print("queue")
        #print(current_maze_)
        #queue.pop(0)
        #print(np.shape(queue))
        #print("queue")
        if check_list(visited,current_maze_)!=True:                       #check if current maze is already visited
            visited.append(current_maze_)
            visited_dash.append([current_maze_,prev_maze_])
        
        if checkSolved(current_maze_)==True:                        #Check if the Maze is solved 
            print("break1")
            break
        neighbours=[]
        current_maze__npa=np.asarray(current_maze_)
        current_maze=list(np.resize(current_maze__npa,(3,3)))                 
        zero_index=[]
        for i in range(3):                                                #find the index of 0 in the current_maze
            for j in range(3):
                if current_maze[i][j]==0:
                    zero_index=[i,j]

        if zero_index[1]<2:                                                  #To go right
            #print("right")
            new_current_maze=list(np.resize(np.asarray(current_maze_),(3,3)))
            temp=new_current_maze[zero_index[0]][zero_index[1]+1]
            new_current_maze[zero_index[0]][zero_index[1]+1]=0
            new_current_maze[zero_index[0]][zero_index[1]]=temp       #check to see if we already played that move
            #print(new_current_maze)
            #print(current_maze)
            if check_list(visited,new_current_maze)==False:
                neighbours.append(list(np.resize(np.asarray(new_current_maze),(1,9))))
            #else:
                #print("#") 
 
       
        if zero_index[0]<2 :                                             #To go down
            #print("down")
            new_current_maze=current_maze
            #print(new_current_maze)
            temp=new_current_maze[zero_index[0]+1][zero_index[1]]            
            new_current_maze[zero_index[0]+1][zero_index[1]]=0
            new_current_maze[zero_index[0]][zero_index[1]]=temp       #check to see if we already played that move
            #print(new_current_maze)
            if check_list(visited,new_current_maze)==False:
                neighbours.append(list(np.resize(np.asarray(new_current_maze),(1,9))))
            #else:
                #print("#")        
        
        if zero_index[1]>0:                                                  #To go left
            #print("left")
            new_current_maze=list(np.resize(np.asarray(current_maze_),(3,3)))
            temp=current_maze[zero_index[0]][zero_index[1]-1]
            new_current_maze[zero_index[0]][zero_index[1]-1]=0
            new_current_maze[zero_index[0]][zero_index[1]]=temp       #check to see if we already played that move
            if check_list(visited,new_current_maze)==False:
                neighbours.append(list(np.resize(np.asarray(new_current_maze),(1,9))))
            #else:
                #print("#")        
                
        if zero_index[0]>0:                                                  #To go up
            #print("up")
            new_current_maze=list(np.resize(np.asarray(current_maze_),(3,3)))
            temp=new_current_maze[zero_index[0]-1][zero_index[1]]
            new_current_maze[zero_index[0]-1][zero_index[1]]=0
            new_current_maze[zero_index[0]][zero_index[1]]=temp       #check to see if we already played that move
            if check_list(visited,new_current_maze)==False:
                neighbours.append(list(np.resize(np.asarray(new_current_maze),(1,9))))
            #else:
                #print("#")
                
            
        for c in neighbours:                                        #iterate through all neighbours to check if solved
            queue.append(c)                                                #add to queue
            visited.append(c)                                               #add to visited
            visited_dash.append([c,current_maze_])                          #add to visited_dash(majorly for backtracking)
            #print((np.resize(np.asarray(c),(3,3))))
            if checkSolved(c)==True:
                path.append([c,current_maze_])
                #print("break2")
                flag=1
                break
            
        if flag==1:                                                     #if solution found break through the loop
            break
        prev_maze_=current_maze_
    print(len(path))
    for c in path:            
        #print(np.resize(c,(3,3)))
        d=1
    if len(queue)!=0:                                                 #if queue becomes empty the test case could not be solved
        print("done")
    else:
        print("Could not solve")
    start=len(visited_dash)-1
    real_path=[]
    while 1:                                                                 #find the real path using backtracking
        #print(path[start])
        real_path.append(visited_dash[start][0])
        
        start=SearchParent(visited_dash,start)
        if start==0:
            break
    
    #print(visited_dash[len(path)-1][0])                                       
    #print("real path is")
    
    #print(path)
    real_path=real_path[:: -1]                                                  #invert the list real path
    for c in real_path:
        print(np.resize(c,(3,3)))
        Write(file1,np.resize(np.transpose(np.resize(c,(3,3))),(1,9)))
        
    for c in range(len(path)):                                                          #add the lists generated to appropriate files
        if c==0:
            file3.write(' '.join(str(elem) for elem in [c,0]))
            file3.write("\n")
            lists=[c,0]
            #Write(file3,lists)
            Write(file2,np.resize(np.transpose(np.resize(path[c][0],(3,3))),(1,9)))
        else:
            lists=[c,SearchParent(path,c)]
            Write(file2,np.resize(np.transpose(np.resize(path[c][0],(3,3))),(1,9)))
            file3.write(' '.join(str(elem) for elem in [c, SearchParent(visited_dash,c)]))
            file3.write("\n")
            #Write(file3,lists)
        
                

def Write(file1,c1):                                                                        #function to write a list into a file
    for c in c1:
       file1.write(' '.join([str(elem) for elem in c])) 
       file1.write("\n") 
        
    
def SearchParent(path,start):                                                           #function to search parent of any element in list
    start_parent=path[start][1]
    #print(start_parent)
    for c in range(len(path)-1):
        if np.array_equal(path[c][0],start_parent):
            return c
        
    

    
    
         



    



#maze_1=np.array([[1,2,3],
#                 [5,6,0],
#                 [7,8,4]]) 
maze_1=np.array([[2,3,0],
                 [1,5,6],
                 [4,7,8]]) 

bfs_solver(maze_1) 
  
#maze=puzzle()
#bfs_solver(maze)
#print(checkifSolvable(maze)) 
#print(checkifSolvable(maze_1))   
#print(checkSolved(maze))     
