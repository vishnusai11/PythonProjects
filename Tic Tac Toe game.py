#!/usr/bin/env python
# coding: utf-8

# Tic Tac Toe / XO Game

# In[1]:


#Function1- To print out a 3 by 3 board
from IPython.display import clear_output

def display_board(board):
    #To clear the screen between moves
    clear_output()  
    print(f"{' '}{board[7]}|{board[8]}|{board[9]}")
    print(f"{' '}{board[4]}|{board[5]}|{board[6]}")
    print(f"{' '}{board[1]}|{board[2]}|{board[3]}")


# In[2]:


#Function2- To ask the 1st player if they want 'X' or 'O'
def player_input():
    print("Usually the 1st player gets to choose 'X' or 'O'")
    #marker
    player1=''  
    
    while player1 not in ['X','O']:
        
        player1=input("Which one would you like? 'X' or 'O': ").upper()
        
        
    if player1=='X':
        return('X','O')
    elif player1=='O':
        return('O','X')


# In[3]:


#Function3- To take in the board, the marker ('X' or 'O'), and the position in which the marker should be printed
def place_marker(board,marker,position):
    board[position]=marker


# In[4]:


#Function4- To take in a board and a marker of a player to check if the player has won
def win_check(board,marker):
    return((board[7]==marker and board[4]==marker and board[1]==marker)#checking for column1
            or(board[8]==marker and board[5]==marker and board[2]==marker)#checking for column2 
            or(board[9]==marker and board[6]==marker and board[3]==marker)#checking for column3 
            or(board[7]==marker and board[8]==marker and board[9]==marker)#checking for row1
            or(board[4]==marker and board[5]==marker and board[6]==marker)#checking fow row2
            or(board[1]==marker and board[2]==marker and board[3]==marker)#checking for row3
            or(board[7]==marker and board[5]==marker and board[3]==marker)#checking for diagonal1
            or(board[1]==marker and board[5]==marker and board[9]==marker))#checking for diagonal2


# In[5]:


#Function5- To decide which player goes first
from random import randint

def choose_first():
    print("Let's see who goes first")
    play=randint(1,2)
    return play


# In[6]:


#Function6- To check if the given position is free
def space_check(board, position):
    return board[position]==' '


# In[7]:


#Function7- To check if the board is full, return True if full, False otherwise
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[8]:


#Function8- To ask for a player's next position where he wants to use X/O and checks if its a free position
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input("What is your next position: "))
    return position


# In[9]:


#Function9- To ask the player at the beginning if the game can be started
def play():
    b=input('Shall we start (Y/N)').upper()
    return b


# In[10]:


#Function10- To ask the player at the end if they want another match
def replay():
    a=input('Do you want to continue (Y/N)').upper()
    return a


# In[11]:


#Main function to run the game
def tic_tac_toe():
    print('Welcome to Tic Tac Toe / XO Game')
    while True:
        #setting up the empty board
        play_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        #Assigning the X and the O
        player1,player2=player_input()
        #Printing out the Players and their respective markers
        print(f"Player 1 is {player1} and player 2 is {player2}")
        #Deciding who gets the first move
        who_plays_first=choose_first()
        #Printing out who gets the first move
        print(f"player{who_plays_first} will play first")
        #Checking if the game can be started
        playfn=play()
        if playfn=='Y':
            play1=True
        elif playfn=='N':
            play1=False
        #Game is started if the player says Y(yes)
        while play1:
            #checks if player1 is the chosen player who gets the first move
            if who_plays_first==1:
                display_board(play_board)
                position=player_choice(play_board)
                place_marker(play_board,player1,position)
                
                #Checks if player1 won
                if win_check(play_board,player1):
                    display_board(play_board)
                    print('Player 1 You Won!')
                    play1=False
                else:
                    if full_board_check(play_board):
                        display_board(play_board)
                        print('It is a draw!')
                        break
                    else:
                        who_plays_first=2
                    
            #if player2 is the chosen player who gets the first move
            else:
                display_board(play_board)
                position=player_choice(play_board)
                place_marker(play_board,player2,position)
                
                #Checks if player2 won
                if win_check(play_board,player2):
                    display_board(play_board)
                    print('Player 2 You Won!')
                    play1=False
                else:
                    if full_board_check(play_board):
                        display_board(play_board)
                        print('It is a draw!')
                        break
                    else:
                        who_plays_first=1
        replayfn=replay()
        #checking if the game can be played once again
        if replayfn=='N':
            break


# In[13]:


tic_tac_toe()


# In[ ]:




