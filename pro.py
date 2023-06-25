import random


MAX_LINES=3
MAX = 1000
MIN= 10

ROWS = 3
COLS = 3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def checkwinnings(columns,lines,bet,values):
    winnings = 0
    winningslines =[]
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winnings += values[symbol] * bet
                winningslines.append(line +1)

    return winnings,winningslines




def slotspin (rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column =[]
        current_symbols = all_symbols[:] # :- pass by copy 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def printslotvalues(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],"|",end="  ")
            else:
                print(column[row],end="")

        print()





def deposit():
    while True:
        amount = input("how much would you like to deposit?")
        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a number\n")
    return amount

def getnumberoflines():
    while True:
        lines = input('enter the number of lines(1-'+str(MAX_LINES)+')?\n')
        if lines.isdigit():
            lines=int(lines)
            if 0< lines <(MAX_LINES+1):
                break
            else:
                print("enter valid number.")
        else:
            print("Please enter a number")
    return lines

def getbet():
    while True:
        a = input('how much would you like to bet on each line\n')
        if a.isdigit():
            a=int(a)
            if MIN<= a <=MAX:
                break
            else:
                print(f"Amount must be between {MIN}-{MAX}.")
        else:
            print("Please enter a number")
    return a
def spin(balance):
    lines= getnumberoflines()
    while True:
        bet=getbet()
        total= bet*lines

        if total>balance:
            print(f'You do not have enough amount to bet, your current balance is{balance}')
        else:
            break
    print(f"you are betting {bet} on {lines} lines, Total bet :{total}")
    slots = slotspin (ROWS,COLS,symbol_count)
    printslotvalues(slots)
    winnings,winningslines =checkwinnings(slots,lines,bet,symbol_value)
    print (f"you won {winnings}.")
    print(f"you won on lines :",*winningslines)
    if winningslines == "1,2,3":
        print("jackpot")
    return winnings- total

def main():
    balance = deposit()
    while True:
        print(f'current balance is{balance} ')
        b = input("press enter to play.(q to quit)")
        if b=="q":
            break
        balance += spin(balance)
    

    print(f"you left with {balance}")

    
main()        