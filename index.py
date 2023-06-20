import random
import hangman_words

lives=6 
end_of_game=False

word=random.choice(hangman_words.words_list)
display=[]
                  
length_word=len(word)
for i in range(length_word):
  display+="_"
print(display)

while not end_of_game :
  
  choosen_letter=input("Choose any Letter :")
  
  choosen_letter.lower()

  
  for i in range(length_word):
      letter=word[i]
      if letter==choosen_letter:
        display[i]=letter
        
  if choosen_letter not in word:

    print("your guess is wrong,lives remaing",lives)
    lives=lives-1
    if lives==0:
      print("You Loose the Game")
    
  
  print(display)
  if "_" not in display :
    end_of_game=True
    print("You win the Game")
  print(hangman_words.stages[lives])

print("The word was", word)
