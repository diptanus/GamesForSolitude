#### Define Functions ####
import random

#Print board
def print_board(tic,player):
    if(player==True):
        print('------Player: Updated board-----')
    elif(player==False):
        print('------Computer: Updated board-----')
    else:
        print('------Initial board-----')
    for row in tic:
        print(row)


#End criteria: If all values are non-empty OR if any row/column/diagonal has same value
def end_criteria(tic):
    criteria = False
    #check rows
    for row in tic:
        if all(item == 'X' for item in row):
            criteria = True
            
        elif all(item == '0' for item in row):
            criteria = True
            
    #check columns
    if not criteria:
        if(tic[0][0]==tic[1][0]==tic[2][0]!=' '):
           criteria = True
        elif(tic[0][1]==tic[1][1]==tic[2][1]!=' '):
            criteria = True
        elif(tic[0][2]==tic[1][2]==tic[2][2]!=' '):
            criteria = True
    #check diags
    if not criteria:
        if(tic[0][0]==tic[1][1]==tic[2][2]!=' '):
            criteria=True
        elif(tic[2][0]==tic[1][1]==tic[0][2]!=' '):
            criteria = True

    #check if all cells are filled
    if not criteria:
        criteria = True
        for row in tic:
            for item in row:
                if item==' ':
                    criteria = False
                    break      
        
    #return bool
    return criteria

#Handle player input
def handle_player_input(tic_tac_toe):   
    rows=len(tic_tac_toe)
    columns = len(tic_tac_toe[0])
    #Prompt player for input
    row_in_str = input('Enter row# for your input (between 1,2,3):\n')  
    col_in_str = input('Enter column# for your input (between 1,2,3):\n')

    while not(row_in_str in ['1','2','3']):
        row_in_str = input('Enter row# FROM (1,2,3):\n')
    while not(col_in_str in ['1','2','3']):
        col_in_str = input('Enter column# FROM (1,2,3):\n')

    row_in = int(row_in_str)
    col_in = int(col_in_str)

    if (tic_tac_toe[row_in-1][col_in-1]==' '):
        #Update board with player input
        tic_tac_toe[row_in-1][col_in-1] = 'X'
    else:
        print(f'The cell [{row_in_str},{col_in_str}] has an entry already. Enter correct value again')
        handle_player_input(tic_tac_toe)
                
#Strategy for computer input at every pass
#Bool as 2nd argument denotes whether the strategy is simple or complex
def decide_computer_input(tic_tac_toe, isSimple):
    if(isSimple == 'dumb'):
        i=0
        for row in tic_tac_toe:
            j=0
            for cell in row:            
                if(cell ==' '):
                    tic_tac_toe[i][j]='0'
                    return
                else:
                    j+=1
            i+=1
    elif(isSimple == 'random'):
        #Random strategy with some intelligence
        
        #0. If any row/col/diag has 2 '0' and one empty cell, fill the empty cell
        if check_and_updateEmptyCell(tic_tac_toe,'0'):
            return
        #1. Check for rows, columns and diags: if any of them has 2 Xs and an empty cell,
        #   fill the empty cell and return
        if check_and_updateEmptyCell(tic_tac_toe,'X'):
            return
        #2. Randomly fill cells if it is empty
        while True:
            r=random.randint(0,2)
            c=random.randint(0,2)
            if(tic_tac_toe[r][c]==' '):
                tic_tac_toe[r][c] = '0'                
                return
        
    else:
        #logical_Strategy(tic_tac_toe)
        #0. If any row/col/diag has 2 '0' and one empty cell, fill the empty cell
        if check_and_updateEmptyCell(tic_tac_toe,'0'):
            return
        #1. Check for rows, columns and diags: if any of them has 2 Xs and an empty cell,
        #   fill the empty cell and return
        if check_and_updateEmptyCell(tic_tac_toe,'X'):
            return
        #2. If middle is empty fill it
        if tic_tac_toe[1][1] == ' ':
            tic_tac_toe[1][1]='0'
            
        
        #3. If middle is 'X':
        #   Iterate through the corners and fill one of the corners if it's empty and return
        elif tic_tac_toe[1][1]=='X':
            if tic_tac_toe[0][0] == ' ':
                tic_tac_toe[0][0]='0'
            elif tic_tac_toe[0][2] ==' ':
                tic_tac_toe[0][2] = '0'
            elif tic_tac_toe[2][0] ==' ':
                tic_tac_toe[2][0] = '0'
            elif tic_tac_toe[2][2] ==' ':
                tic_tac_toe[2][2] = '0'
        #4. If middle is '0' and at least one corner is 'X':
        #   Iterate through the middle element in rows and columns,
        #   fill the first empty one and return
        elif tic_tac_toe[1][1]=='0':
            if (tic_tac_toe[0][0]=='X' or tic_tac_toe[0][2]=='X' or tic_tac_toe[2][0]=='X' or tic_tac_toe[2][2]=='X'):
                if tic_tac_toe[0][1] == ' ':
                    tic_tac_toe[0][1]='0'
                elif tic_tac_toe[1][0] ==' ':
                    tic_tac_toe[1][0] = '0'
                elif tic_tac_toe[1][2] ==' ':
                    tic_tac_toe[1][2] = '0'
                elif tic_tac_toe[2][1] ==' ':
                    tic_tac_toe[2][1] = '0'
        #5. If middle is '0' and at least one middle is 'X':
        #   fill one of the corners and return
            elif(tic_tac_toe[0][1]=='X' or tic_tac_toe[1][0]=='X' or tic_tac_toe[1][2]=='X' or tic_tac_toe[2][1]=='X'):
                if tic_tac_toe[0][0] == ' ':
                    tic_tac_toe[0][0]='0'
                elif tic_tac_toe[0][2] ==' ':
                    tic_tac_toe[0][2] = '0'
                elif tic_tac_toe[2][0] ==' ':
                    tic_tac_toe[2][0] = '0'
                elif tic_tac_toe[2][2] ==' ':
                    tic_tac_toe[2][2] = '0'
        
        
    
#Check if 2 cells in a row/col/diag have the same value and the 3rd one is empty.
#Update the 3rd empty cell with '0'
def check_and_updateEmptyCell(tic_tac_toe,value):
    #check rows:
    i=0
    for row in tic_tac_toe:
        if row.count(value)==2 and (' ' in row):
            j = row.index(' ')
            tic_tac_toe[i][j] = '0'
            return True
        i+=1
    #check columns
    tansposed_tic=list(zip(*tic_tac_toe))
    i=0
    for row in tansposed_tic:
        if row.count(value)==2 and (' ' in row):
            j = row.index(' ')
            tic_tac_toe[j][i] = '0'
            return True
        i+=1
    #check diagonals
    diag1 = [tic_tac_toe[0][0],tic_tac_toe[1][1],tic_tac_toe[2][2]]
    if diag1.count(value)==2 and (' ' in diag1):
        j = diag1.index(' ')
        tic_tac_toe[j][j] = '0'
        return True     
    diag2 = [tic_tac_toe[2][0],tic_tac_toe[1][1],tic_tac_toe[0][2]]
    if diag2.count(value)==2 and (' ' in diag2):
        j = diag2.index(' ')
        i=2
        if j==1:
            i=1
        elif j==2:
            i=0
        tic_tac_toe[i][j] = '0'
        return True
    return False




##### Main Program #####

#Initialize board
rows, cols = (3, 3)
tic_tac_toe = [[' ']*cols for _ in range(rows)]
itr = 1
print_board(tic_tac_toe,' ')
while not end_criteria(tic_tac_toe):
    print('Pass: ', itr)
    itr+=1

    handle_player_input(tic_tac_toe)        

    #Print board
    print_board(tic_tac_toe,True)        

    #Update board with computer input
    if not end_criteria(tic_tac_toe):
        decide_computer_input(tic_tac_toe,'random')

        #Print board
        print_board(tic_tac_toe,False)
    
print('Game over')







