import numpy as np
def printBoard(arr):  #function for printing Board
    
    print(arr[0],"\t|",arr[1],"\t|",arr[2])
    print("\t|\t|")
    print("--------------------------")
    print(arr[3],"\t|",arr[4],"\t|",arr[5])
    print("\t|\t|")
    print("\t|\t|")
    print("--------------------------")
    print(arr[6],"\t|",arr[7],"\t|",arr[8])
    print("\t|\t|")
    print("\t|\t|")
    print("--------------------------")
def Turn1(player1,pos,count,turn):
 
 print(player1, "Turn\n")
 #turn=player1
 print("Enter move 0-8")
 pos=int(input())
 count=count+1
 if pos>8 or pos<0:
   print("Illegal Position")
   print("Enter move 0-8")
   pos=int(input())
 elif arr[pos]=='X' or arr[pos]=='O':
   print("Position Occupied")
 elif count>8:
   print("No more moves left")
 return pos
def Turn2(player2,pos,count,turn):
   print(player2, "Turn\n")
   #turn=player2
   print("Enter move 0-8")
   pos=int(input())
   count=count+1
   if pos>8 or pos<0:
    print("Illegal Position")
    print("Enter move 0-8")
    pos=int(input())
   elif arr[pos]=='X' or arr[pos]=='O':
    print("Position Occupied")
   elif count>8:
    print("No more moves left")
   return pos
def checkWin(arr,player1,player2):
    if arr[0] and arr[1] and arr[2]=='X':
        print(player1,"Wins")
    elif arr[0] and arr[3] and arr[6]=='X':
        print(player1,"Wins")
    elif arr[1] and arr[4] and arr[7]=='X':
        print(player1,"Wins")
    elif arr[2] and arr[5] and arr[8]=='X':
        print(player1,"Wins")
    elif arr[3] and arr[4] and arr[5]=='X':
        print(player1,"Wins")
    elif arr[6] and arr[7] and arr[8]=='X':
        print(player1,"Wins")
    elif arr[1] and arr[4] and arr[8]=='X':
        print(player1,"Wins")
    elif arr[2] and arr[4] and arr[6]=='X':
        print(player1,"Wins")
    elif arr[0] and arr[1] and arr[2]=='O':
        print(player2,"Wins")
    elif arr[0] and arr[3] and arr[6]=='O':
        print(player2,"Wins")
    elif arr[1] and arr[4] and arr[7]=='O':
        print(player2,"Wins")
    elif arr[2] and arr[5] and arr[8]=='O':
        print(player2,"Wins")
    elif arr[3] and arr[4] and arr[5]=='O':
        print(player2,"Wins")
    elif arr[6] and arr[7] and arr[8]=='O':
        print(player2,"Wins")
    elif arr[1] and arr[4] and arr[8]=='O':
        print(player2,"Wins")
    elif arr[2] and arr[4] and arr[6]=='O':
        print(player2,"Wins")
    




import numpy
arr = numpy.array(['0','1', '2', '3', '4','5','6','7','8'])
turn=''
pos=0
count=0
position=0
print("Select Player by entering input")
user_input=input("Enter the player  X or O\n")
if user_input=='X':
    player1='X'
    player2='O'
    turn=player1
    print("Player1 is", player1)
    print("Player2 is", player2)
else:
    player1='O'
    player2='X'
    turn=player1
    print("Player1 is", player1)
    print("Player2 is", player2)
printBoard(arr)
print("Enter positions on your turn\n")
inc=0
while(1):
 if turn==player1:
  position=Turn1(player1,pos,count,turn)
  arr[position]=player1
  printBoard(arr)
  checkWin(arr,player1,player2)
  turn=player2
 else:
  position=Turn2(player2,pos,count,turn)
  arr[position]=player2
  printBoard(arr)
  checkWin(arr,player1,player2)
  turn=player1
 inc=inc+1
 if inc>7:
     break

    
    

      

