import pygame
import random 
import string
import time
easy =["cat", "dog"]
medium = ["street","python"]
hard = ["astronaut", "bookshelf"]
#start to copy here
pygame.init()
def print_to_screen(phrase):
  text = font.render(phrase, True, WHITE )
  text_rect = text.get_rect()
  text_x = screen.get_width() /2 - text_rect.width /2
  text_y = screen.get_height() /2 - text_rect.height /2
  screen.blit(text, [text_x,text_y])
  pygame.display.flip()

def clear_screen(color):
  screen.fill(color)

#end copying here



#choose colors
BLACK = (0,0,0)
WHITE = (255,255,255)
#choose screen size
size = [700,700]
screen = pygame.display.set_mode(size)
done = False
#font and font size 
font = pygame.font.Font(None, 30)

for event in pygame.event.get():
    #you could just do this with the while loop but you can add other things to end the game, like a certain key press and the for loop listens for those 
    #if you use the pygame events change the while to an elif 
    #within the while it's basically the same as the original code but instead of printing it in the terminal it prints the screen. You could just have the kids to the text on thursday and then add the graphics on friday 
  while not done:
    #clears the screen
    screen.fill(BLACK)
    #prints to the graphics screen
    print_to_screen("What level do you want to play?")
    #waits before advancing to the next screen
    time.sleep(1)
    clear_screen(BLACK)
    print_to_screen(" Level 1: easy Level 2: medium Level 3: hard")
    time.sleep(.25)
    clear_screen(BLACK)
    #takes input of what level, as a number or words
    level = str(input())
    level = level.lower() 

    #go_ahead = "Press enter to continue"
    
    #print_to_screen(go_ahead)
    #dead = input()
    
    clear_screen(BLACK)
    
    if level == "1": 
      secret_word = random.choice(easy)
      print_to_screen("easy")
      time.sleep(.5)
      clear_screen(BLACK)
      
    elif level == "2":
      secret_word = random.choice(medium)
      print_to_screen("medium")
      time.sleep(.5)
      clear_screen(BLACK)
    
    elif level == "3":
      secret_word = random.choice(hard)
      print_to_screen("hard")
      time.sleep(.5)
      clear_screen(BLACK)
      
    elif level ==  "easy":
      
      secret_word = random.choice(easy)
      
      print_to_screen("easy")
      time.sleep(.5)
      clear_screen(BLACK)
    elif level ==  "medium":
      secret_word = random.choice(medium)
      print_to_screen("medium")
      time.sleep(.5)
      clear_screen(BLACK)
      
    elif level ==  "hard":
      secret_word = random.choice(hard)
      print_to_screen("hard")
      time.sleep(.5)
      clear_screen(BLACK)
      
    else:
      secret_word = random.choice(easy)
      print_to_screen("easy")
      time.sleep(.5)
      clear_screen(BLACK)
    
    max_wrong_guesses =len(secret_word)
    num_wrong_guesses = 0
    wrong_guesses = []
    correct_guesses = []
    blank_spaces = ""
    num_spaces = len(secret_word)
    for i in range(num_spaces):
      blank_spaces = blank_spaces + "_ "
    
    intro = "Here is your word: " + blank_spaces 
    print_to_screen(intro)
    
    time.sleep(1)
    
    while True: 
      clear_screen(BLACK)
      guess_prompt = "Guess a letter"
      print_to_screen(guess_prompt)
      letter = input()
      
      if letter == "help":
        lowercase_letters ="abcdefghijklmnopqrstuvwxyz"
        random_num = random.randint(0,25)
        letter = lowercase_letters[random_num]
        random_letter = "Random letter is " + letter
        
        clear_screen(BLACK)
        print_to_screen(random_letter)
        time.sleep(1)

      if len(letter) > 1:
        you_cant_do_that = "You may only guess one letter at a time"
        clear_screen(BLACK)
        print_to_screen(you_cant_do_that)
        time.sleep(1)
        continue
      if letter in wrong_guesses or letter in correct_guesses:
        no_sorry = "You have already guessed " + letter
        clear_screen(BLACK)
        print_to_screen(no_sorry)
        time.sleep(1)
      elif letter in secret_word:
        good_guess = "good guess"
        clear_screen(BLACK)
        print_to_screen(good_guess)    
        correct_guesses.append(letter)
        
        time.sleep(1)
        
      else:
        incorrect = "No there isnt't a " + letter + " in the word"
        clear_screen(BLACK)
        print_to_screen(incorrect)
        wrong_guesses.append(letter)
        num_wrong_guesses += 1 
        time.sleep(.75)
        clear_screen(BLACK)
        num_wrong_words = "You have made " + str(num_wrong_guesses) + " wrong guesses"
        print_to_screen(num_wrong_words)
        time.sleep(1)
      blank_spaces = ""
      
      for letter in secret_word:
        if letter in correct_guesses:
          blank_spaces += letter
        else:
          blank_spaces += "_ "
      clear_screen(BLACK)
      print_to_screen(blank_spaces)
      time.sleep(1)
      
      if blank_spaces == secret_word:
        font = pygame.font.Font(None, 30)
        congrats = "You did it! You guessed the word! It was: " + secret_word
        clear_screen(BLACK)
        print_to_screen(congrats)
        time.sleep(1)
        done = True
      elif num_wrong_guesses == max_wrong_guesses:
        game_over = "Game over. The word was " + secret_word
        clear_screen(BLACK)
        print_to_screen(game_over)
        time.sleep(1)
        done = True
      else:
        done = False
      if done == True:
        play_again = "would you like to play again?"
        clear_screen(BLACK)
        print_to_screen(play_again)
        time.sleep(.5)
        options = "1. yes, or 2. no"
        clear_screen(BLACK)
        print_to_screen(options)
        user_input = input()
        if user_input =="1":
          
          clear_screen(BLACK)
          print_to_screen("Let's play again")
          time.sleep(.5)
          
          done = False
          break
        else:
          keep_playing = True
          clear_screen(BLACK)
          print_to_screen("Thank you for playing")
          time.sleep(.5)
          break

        



       
  

