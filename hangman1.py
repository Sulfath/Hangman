
import random
import string
from words import words
from hangman_visual import lives_visual_dict

def get_valid_word(words):
  word  = random.choice(words)

  return word.upper()


def hangman() :
  word = get_valid_word(words) 
  word_letters =set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  lives =6
  print("Random string is :" ,word) 
    

  while len(word_letters) > 0 and lives> 0 :
    userinput = input("Enter a letter").upper()
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_visual_dict[lives])
    print('Current word: ', ' '.join(word_list))
    if userinput in alphabet - used_letters:
        used_letters.add(userinput)
        if userinput in word_letters :
          word_letters.remove(userinput)
        else :
          lives =lives - 1          

    elif userinput in used_letters:
         print("you have already entered the lettter") 
    else :
         print("Invalid letter")

  if lives == 0:
     print(lives_visual_dict[lives])
     print("You died, the word was ",word)
  else :
   print("You guessed the word",word, "!!" )


hangman()