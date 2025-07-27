#generate the color
import random

COLORS = ["R", "G", "B", "Y", "W", "O"] #color and tries are variables
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range (CODE_LENGTH):
        color = random.choice(COLORS) #randomly sleect color
        code.append(color)
        
    return code

#code=generate_code()

#allow user to guess the code

def guess_code():
    while True:
        guess = input("guess the color: ").upper().split(" ")  #split vitra space vaneko input ma aako colors jastai G G G G lai list ma convert gardinxa like ["G", "G"

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.") 
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"invalid color: {color}. Try again!")
                break
            
        else:
            break
        
    return guess

#aba color codecheck garne

def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position == real_color
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position +=1
            color_counts[guess_color] -= 1
            
    return correct_position, incorrect_position

#linking mathi ko 3  parts

def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code.")
    print("the valid colors are" , COLORS)
    
    code = generate_code()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)
        
        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"correct positions: {correct_position} | incorrect_positions: {incorrect_position}")
        
    else:
        print("You ran out of tries, the code was:", code)
        
if __name__ == "__main__":
    game()

    
    

