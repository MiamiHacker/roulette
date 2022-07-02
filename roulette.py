#!/usr/bin/env python3
help = f'''
Coded by MiamiHacker version 0.5
[+] set autoplay to False to play it yourself 
[+] set autoplay to True for automated playing
'''
autoplay = False

import random
import sys
import signal
import time
from colorama import init, Fore
from pathlib import Path
import os.path

#colors
init()
GREEN = Fore.GREEN
RED   = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

gameinfo = f'''
It's possible to bet on Black or {RED}Red{RESET}!
    Red or Black pays even money.
    Odd or Even bets pay even money.
    Single number bet pays 35 to 1.
'''

black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
zero = [0, -1]
credits = 500
n = 0

def recursionlimit():
    if autoplay == True:
        sys.setrecursionlimit(100000)
    else:
        sys.setrecursionlimit(2500)

def creditsfile():
    if os.path.isfile('credits.txt'):
        pass
    else:
        file = Path('credits.txt')
        file.touch(exist_ok=True)
        bet_credits = str(credits)
        open("credits.txt", "w").write(bet_credits)

def bet_question():
        i = 0
        while i < 2:
            if autoplay == True:
                want_to_bet = "yes"
            else:
                want_to_bet = input("Do you want to make a bet?\n")
            
            if any(want_to_bet.lower() == f for f in ["yes", 'y', '1', 'ye']):
                bet_credits = open("credits.txt", "r").read()
                print(f"\n{GREEN}You have {bet_credits} credits\n{RESET}")
                break
            elif any(want_to_bet.lower() == f for f in ['no', 'n', '0', '']):
                print("Program closed.")
                sys.exit()
            else:
                i += 1
                if i < 2:
                    print('Please enter yes or no')
                else:
                    print("Program closed incorrect input.")
                    sys.exit()

def write_credits(bet_credits):
            # print(f"{GREEN}You have {bet_credits} credits\n{RESET}")
            bet_credits = str(bet_credits)
            open("credits.txt", "w").write(bet_credits)
            return bet_credits

def keyboard_interrupt(signal, frame):
    print ('\nThanks for playing the game!')
    sys.exit(0)
signal.signal(signal.SIGINT, keyboard_interrupt)

def exit_game():
    print ('\nThanks for playing the game!')
    sys.exit(0)

def credit_check():
    bet_credits = open("credits.txt", "r").read()
    bet_credits = int(bet_credits)
    if bet_credits < 1:
        print(f"\n{RED}GAME OVER{RESET} - No credits left")
        print(f"You will get {credits} free credits!")
        bet_credits = credits
        write_credits(bet_credits)
        exit_game()

def possible_bets():
    print(gameinfo)
    recursionlimit()
    creditsfile()
    bet_question()

    def bet_again_question():
        credit_check()
        bet_question()
        amount()

    def amount():
        if autoplay == True:
            bet_amount = 1
        else:
            bet_amount = input("How mutch you want to bet?\n")

        while True:
            try:
                val = int(bet_amount)
                # print("Input is a integer", bet_amount)
                bet_amount = int(bet_amount)
                if bet_amount > 0:
                    bet_credits = open("credits.txt", "r").read()
                    bet_credits = int(bet_credits)
                    if bet_amount > bet_credits:
                        print("Let's go Allin!!")
                        bet_amount = bet_credits
                    break
                elif bet_amount == 0:
                    print("You can't make a bet with nothing!")
                    amount()
                else:
                    print(f"Your input {bet_amount} is a negative number")
                    amount()
            except ValueError:
                    print(f"Your input {bet_amount} is not a whole positive number")
                    exit_game()
        credit_check()    
        bet_amount = int(bet_amount)
                
        if autoplay == True:
            random_game = random.randint(1,3)
            pick_game = random_game
            pick_game = int(pick_game)
            # print(f"Game: {pick_game}")
            if pick_game == 1 or pick_game == 2:
                if bet_credits <= credits * 1:
                    low_bets = [3, 5, 10]
                    autoplay_betamount = random.choice(low_bets)
                    # print(autoplay_betamount)
                elif bet_credits > credits * 1:
                    high_bets = [5, 10, 15, 20, 25, 40]
                    autoplay_betamount = random.choice(high_bets)
                    # print(autoplay_betamount)
            else:
                if bet_credits <= credits * 1:
                    low_num_bets = [1, 3, 5]
                    autoplay_betamount = random.choice(low_num_bets)
                else:
                    high_num_bets = [3, 5, 10, 15, 20]
                    autoplay_betamount = random.choice(high_num_bets)
                    # print(autoplay_betamount)
            bet_credits = open("credits.txt", "r").read()
            bet_credits = int(bet_credits)
            if autoplay_betamount > bet_credits:
                print("Let's go Allin!!")
                bet_amount = bet_credits
            else:
                bet_amount = autoplay_betamount
                print(f"{YELLOW}Your bet is {bet_amount} credits{RESET}")
        else:
            print(f"{YELLOW}Your bet is {bet_amount} credits{RESET}")
            pick_game = input("What game: [1]Black\Red [2]Odd\Even [3]Number")
            pick_game = int(pick_game)

        if pick_game == 1:
            print("You are playing Black or Red")
            if autoplay == True:
                random_color = random.randint(1,2)
                color_bet = random_color
                color_bet = int(color_bet)
            else:
                color_bet = input("What color: [1]Black - [2]Red?")
                color_bet = int(color_bet)
            
            n = random.randint(-1,36)
            print("The winning number is", n)
            if n in black and color_bet == 1 and pick_game == 1:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits + bet_amount
                print(f"You won {GREEN}{bet_amount}{RESET}, it's Black:")
                write_credits(bet_credits)
                bet_again_question()
            elif n in red and color_bet == 2 and pick_game == 1:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits + bet_amount
                print(f"You won {GREEN}{bet_amount}{RESET}, it's Red:")
                write_credits(bet_credits)
                bet_again_question()
            elif n in zero and pick_game == 1:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits - (bet_amount / 2)
                bet_credits = int(bet_credits)
                print(f"You lost 50%: {YELLOW}{bet_amount / 2}{RESET}")
                write_credits(bet_credits)
                bet_again_question()
            else:
                if pick_game == 1:
                    if n in black: 
                        color = "Black"
                    else:
                        color = "Red"
                    bet_credits = open("credits.txt", "r").read()
                    bet_credits = int(bet_credits)
                    bet_credits = bet_credits - bet_amount
                    print(f"You lost: {RED}{bet_amount}{RESET}, it's {color}")
                    write_credits(bet_credits)
                    bet_again_question()
                else:
                    pass
                return bet_credits

        if pick_game == 2:
            print("You are playing Odd or Even")
            if autoplay == True:
                random_odd_even = random.randint(1,2)
                odd_even_bet = random_odd_even
                odd_even_bet = int(odd_even_bet)
            else:
                odd_even_bet = input("What color: [1]Odd - [2]Even?")
                odd_even_bet = int(odd_even_bet)
                
            n = random.randint(-1,36)
            print("The winning number is", n)
            if n in odd and odd_even_bet == 1 and pick_game == 2:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits + bet_amount
                print(f"You won {GREEN}{bet_amount}{RESET}, it's Odd:")
                write_credits(bet_credits)
                bet_again_question()
            elif n in even and odd_even_bet == 2 and pick_game == 2:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits + bet_amount
                print(f"You won {GREEN}{bet_amount}{RESET}, it's Even:")
                write_credits(bet_credits)
                bet_again_question()
            elif n in zero and pick_game == 2:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits - (bet_amount / 2)
                bet_credits = int(bet_credits)
                print(f"You lost 50%: {YELLOW}{bet_amount / 2}{RESET}")
                write_credits(bet_credits)
                bet_again_question()
            else:
                if pick_game == 2:
                    if n in odd: 
                        type = "Odd"
                    else:
                        type = "Even"
                    bet_credits = open("credits.txt", "r").read()
                    bet_credits = int(bet_credits)
                    bet_credits = bet_credits - bet_amount
                    print(f"You lost: {RED}{bet_amount}{RESET}, it's {type}")
                    write_credits(bet_credits)
                    bet_again_question()
                else:
                    pass
                return bet_credits
        
        if pick_game == 3:
            print("You are playing for 1 number")
            if autoplay == True:
                time.sleep(0.1)
                bet_number = random.randint(-1,36)
                bet_number = int(bet_number)
            else:
                bet_number = input("Call your lucky number:")
                bet_number = int(bet_number)            

            print(f"You pick number {bet_number}")
            n = random.randint(-1,36)
            if n == bet_number:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits + (bet_amount * 35)
                print(f"You won {GREEN}{bet_amount * 35}{RESET}, it's {n}")
                write_credits(bet_credits)
                bet_again_question()
            else:
                bet_credits = open("credits.txt", "r").read()
                bet_credits = int(bet_credits)
                bet_credits = bet_credits - bet_amount
                print(f"You lost: {RED}{bet_amount}{RESET}, it's number {n}")
                write_credits(bet_credits)
                bet_again_question()                
            return bet_credits
    amount()
possible_bets()
