# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:34:35 2020

@author: prana
"""
import numpy as np
def puzzle():
    maze= np.array([[1,2,3],[4,0,5],[6,7,8]])
    
   
    return maze

def checkifSolvable(maze):
     maze_=np.resize(maze,(1,9))
    
     inv_count=0
     
     for i in range(len(maze)*len(maze)):
         for j in range(i+1,9):
             if maze_[0][i]!=0  and  maze_[0][j]!=0   and   maze_[0][i]>maze_[0][j]:
                 inv_count=inv_count+1
     #print(inv_count) 
     if inv_count%2==0:
         return True
     else:
         return False
     
def checkSolved(maze):
    maze_=np.resize(maze,(1,9))
    #print(maze_)
    maze_=maze_[maze_!=0]
    #print(maze_)
    #maze_1=np.sort(maze_)
    maze_2=np.array([1,2,3,4,5,6,7,8])
    #print(maze_1)
    if np.array_equal(maze_,maze_2)==True:
        return True
    else:
        return False
    
def check_list(lists,instance):
    instance=np.resize(np.asarray(instance),(1,9))
    for i in range(len(lists)):
        if np.array_equal(instance,lists[i])==True:
            return True
    return False
                 
                 
    
            
def bfs_solver(maze):
    if checkifSolvable(maze)==False:
        print("Not Solvable")
        return False
    
    print(maze)
    maze_=np.resize(maze,(1,9))
    maze_size=np.array([])
    
    queue=[]
    path=[]
    visited=[]
    queue.append(maze_)
    counter=0
    parents=[]
    prev_maze_=queue[0]
    visited_dash=[]
    while len(queue)!=0:
        flag=0
        
        #print((np.shape(queue)))
        #current_maze_=queue[len(queue)-1]
                
        current_maze_=queue.pop(0)
        #print("Currentmaze")
        #print(np.resize(current_maze_,(3,3)))
        #print(" ")
        #print("Currentmaze")
       
        path.append([current_maze_,prev_maze_])
        
        #print("queue")
        #print(current_maze_)
        #queue.pop(0)
        #print(np.shape(queue))
        #print("queue")
        if check_list(visited,current_maze_)!=True:
            visited.append(current_maze_)
            visited_dash.append([current_maze_,prev_maze_])
        
        if checkSolved(current_maze_)==True:
            print("break1")
            break
        neighbours=[]
        current_maze__npa=np.asarray(current_maze_)
        current_maze=list(np.resize(current_maze__npa,(3,3)))
        zero_index=[]
        for i in range(3):
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
                
            
        for c in neighbours:
            queue.append(c)
            visited.append(c)
            visited_dash.append([c,current_maze_])
            #print((np.resize(np.asarray(c),(3,3))))
            if checkSolved(c)==True:
                path.append([c,current_maze_])
                #print("break2")
                flag=1
                break
            
        if flag==1:
            break
        prev_maze_=current_maze_
    print(len(path))
    for c in path:
        print(np.resize(c,(3,3)))
        d=1
    if len(queue)!=0:  
        print("done")
    else:
        print("Could not solve")
    start=len(visited_dash)-1
    real_path=[]
    while 1:
        #print(path[start])
        real_path.append(visited_dash[start][0])
        start=SearchParent(visited_dash,start)
        if start==0:
            break
    
    print(visited_dash[len(path)-1][0])
    print("real path is")
    
    #print(path)
    real_path=real_path[:: -1]
    for c in real_path:
        print(np.resize(c,(3,3)))
                
        
    
def SearchParent(path,start):
    start_parent=path[start][1]
    #print(start_parent)
    for c in range(len(path)-1):
        if np.array_equal(path[c][0],start_parent):
            return c
        
    

    
    
         



    



maze_1=np.array([[8,6,7],
                 [2,5,4],
                 [3,0,1]]) 
##maze_1=np.array([[0,1,2],
#                 [3,4,5],
#                 [6,7,8]]) 
print(checkifSolvable(maze_1))
print(checkSolved(maze_1)) 
bfs_solver(maze_1) 
  
#maze=puzzle()
#bfs_solver(maze)
#print(checkifSolvable(maze)) 
#print(checkifSolvable(maze_1))   
#print(checkSolved(maze))     