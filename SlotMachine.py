import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbols_count = {
    'A':2,
    'B':4,
    'C':5,
    'D':8
}
symbols_values ={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if(amount>0):
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount
def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount= int(amount)
            if(MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount
def get_slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column=[]
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value= random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def slot_machine(columns):
      for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:     
                print(column[row],end=" | " )
            else:
                print(column[row])  
        print()  

def check_win(columns,lines,bet,values):
    win=0
    win_lines=[]
    for line in range(lines) :
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            win += values[symbol]*bet
            win_lines.append(line+1)
    return win,win_lines    

def spin(bal):    
    lines= get_no_of_lines()
    while True:
        bet = get_bet()
        Total_bet = bet*lines
        if Total_bet>bal:
            print(f"You do not have enough balace. Your current balance is ${bal}")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is {Total_bet}. ")
    slots= get_slot_spin(ROWS,COLS, symbols_count)
    slot_machine(slots)
    win,win_lines = check_win(slots, lines, bet, symbols_count)
    print(f"You won{win}.")
    print("You won on: ", *win_lines)
    return win - Total_bet           
def main():
    bal=deposit()
    while True:
        print(f"Current balance is ${bal}.")
        answer=input("Press enter to play (q to quit).")
        if answer=="q":
            break
        bal += spin(bal)
    print(f"You left with ${bal}")  
     
main()
