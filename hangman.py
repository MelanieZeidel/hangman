import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]


WORDS = ['casa','perro','gato','automovil','computadora','python']

class Hangman():
    
    
    def __init__(self, word):
        self.failed_attempts = 0
        self.word = word
        self.game_progress = list('_' * len(self.word))
     
    #character_input by user
    def get_user_input(self):
        user_input = input('\nPlease, enter a letter: ')
        #return user_input
        return user_input.lower()
    
    def find_indexes(self,letter):
        return [i for i, char in enumerate(self.word) if letter == char]

    def is_invalid_letter(self,input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)
    
    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(''.join(self.game_progress))
        
    def update_progress(self,letter,indexes):
        for index in indexes:
            self.game_progress[index] = letter

        
    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            
            if self.is_invalid_letter(user_input):
                print('The input is not a letter. Type the input again')
                continue
            
            if user_input in self.game_progress:
                print('You already have guessed the letter')
                continue
    
            if user_input in self.word:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input,indexes)
                
                if self.game_progress.count('_') == 0:
                    print(f'You win!!\nThe word is: {self.word}')
                    quit()
            
            else:
                self.failed_attempts += 1
            
        print('Oh! you lost')
        
if __name__ == '__main__':
    word = random.choice(WORDS)
    hangman = Hangman(word)
    hangman.play()
        
    
    
    
    
    