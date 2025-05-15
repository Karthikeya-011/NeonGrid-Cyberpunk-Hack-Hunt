import time
import random

def delay_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

def intro():
    delay_print("Welcome to NeonGrid: The Cyberpunk City Hack Treasure Hunt.")
    delay_print("The year is 2125. Megacities are ruled by data.")
    delay_print("Your mission: Infiltrate the encrypted layers of NeonGrid and retrieve the lost treasure of the old net.")
    input("\nPress Enter to jack in...\n")

def clue_one():
    delay_print("CLUE 1: A signal bounces off three towers every 5 seconds.")
    delay_print("Tower A hears it at 0s, Tower B at 5s, and Tower C at 10s.")
    ans = input("Which tower is the source of the signal? (A/B/C): ").strip().upper()
    return ans == 'C'

def clue_two():
    delay_print("\nCLUE 2: You're in the codebase. You see this encrypted hint: 'H@ck3r_4L1v3'.")
    delay_print("Translate the leetspeak to normal English.")
    ans = input("Your answer: ").strip().lower()
    return ans == "hacker_alive"

def clue_three():
    delay_print("\nCLUE 3: A terminal asks you to guess the right keycode between 1000-1010. You have 3 tries.")
    keycode = random.randint(1000, 1010)
    for i in range(3):
        try:
            guess = int(input(f"Attempt {i+1}: Enter keycode: "))
        except ValueError:
            delay_print("Invalid input. Please enter a number.")
            continue
        if guess == keycode:
            return True
        elif guess < keycode:
            delay_print("Access Denied. Hint: Higher.")
        else:
            delay_print("Access Denied. Hint: Lower.")
    return False

def clue_four():
    delay_print("\nCLUE 4: A firewall presents a riddle:")
    delay_print("'I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?'")
    ans = input("Your answer: ").strip().lower()
    return ans == "echo"

def clue_five():
    delay_print("\nCLUE 5: A Python script flashes on the screen:")
    delay_print('>>> print("2" + "2")')
    delay_print("What is the output of this code?")
    ans = input("Your answer: ").strip()
    return ans == "22"

def clue_six():
    delay_print("\nCLUE 6: An AI bot challenges you with code logic.")
    delay_print("You see this Python line: >>> print(bool('False'))")
    delay_print("What is the output?")
    ans = input("Your answer: ").strip().lower()
    return ans == "true"

def clue_seven():
    delay_print("\nCLUE 7: You enter a data maze and find this line:")
    delay_print(">>> x = [0, 1, 2, 3]; print(x[::-1])")
    delay_print("What will be printed?")
    ans = input("Your answer: ").strip()
    return ans.replace(" ", "") in ["[3,2,1,0]", "[3, 2, 1, 0]"]

def clue_eight():
    delay_print("\nCLUE 8: You stumble upon a corrupted terminal running this:")
    delay_print(">>> a = 'cyber'\n>>> b = 'punk'\n>>> print(a + b)")
    delay_print("What is the output?")
    ans = input("Your answer: ").strip().lower()
    return ans == "cyberpunk"

def end_game(score):
    delay_print(f"\nYou solved {score} out of 8 clues.")
    if score >= 5:
        delay_print("\nACCESS GRANTED: You’ve hacked into the deepest vault of NeonGrid.")
        delay_print("You found the lost crypto-treasure: a digital relic worth billions.")
        delay_print("Congratulations, NetRunner!")
    else:
        delay_print("\nACCESS DENIED: Your hack attempt failed.")
        delay_print("The treasure remains hidden in the shadows of NeonGrid...")

def main():
    intro()
    score = 0

    if clue_one():
        delay_print("Correct! Tower C is the last to hear it, so it's the source.")
        score += 1
    else:
        delay_print("Incorrect. Think in reverse-time next time.")

    if clue_two():
        delay_print("Correct! You decoded the hacker tag.")
        score += 1
    else:
        delay_print("Incorrect. The old net isn’t forgiving.")

    if clue_three():
        delay_print("Correct Keycode! The vault door opens...")
        score += 1
    else:
        delay_print("Wrong keycode. Security protocols activated.")

    if clue_four():
        delay_print("Correct! The firewall lets you pass.")
        score += 1
    else:
        delay_print("Incorrect. The system grows suspicious.")

    if clue_five():
        delay_print("Correct! You understood how Python handles strings.")
        score += 1
    else:
        delay_print("Incorrect. Python isn’t always about math.")

    if clue_six():
        delay_print("Correct! You cracked the logic gate.")
        score += 1
    else:
        delay_print("Incorrect. Remember, even 'False' as a string is something.")

    if clue_seven():
        delay_print("Correct! You reversed the list like a pro.")
        score += 1
    else:
        delay_print("Incorrect. Check your slicing skills.")

    if clue_eight():
        delay_print("Correct! You joined the fragments flawlessly.")
        score += 1
    else:
        delay_print("Incorrect. Think simple string concatenation.")

    end_game(score)

if __name__== "__main__":
    main()