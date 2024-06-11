import string
import random
from words import words
from hangman_visual import lives_visual_dict 

def get_valid_word():
    
    word = random.choice(words)
    return word.upper()   

def hangman():
    alphabets = set(string.ascii_uppercase) 
    word = get_valid_word()
    print("The random word",word)
    word_letters = set(word)
    used_letter = set()
    lives =6
    
   # print("Current word ",' '.join(word))
    while len(word_letters) > 0 and lives >0:
      userinput = input("Enter a character ").upper()

      word_list = [letter if letter in used_letter else '-' for letter in word]
      print("Current word is ",' '.join(word_list)) 
      print(lives)
      print(lives_visual_dict[lives])
      if userinput in alphabets - used_letter:
        used_letter.add(userinput)
        
        if userinput in word_letters:
            word_letters.remove(userinput)
        else:
            lives = lives -1    
          #print("Current word ",' '.join(word_letters))
            
        print ("You have ",lives," left and Used charcters  :",' '.join(used_letter))  
           
      elif userinput in used_letter:
        print("The character is already used")
      else:
        print("Invalid character!!")

    if lives ==0:
       print(lives_visual_dict[lives])
       print("You died, The correct word was ",word)
    else:
       print("You guessed the correct word ,",word," !!")   


      

hangman()       