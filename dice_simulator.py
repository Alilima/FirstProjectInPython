# Dice Simulator
# Simulate the generation of numbers from 1 to 6

import random

class DiceSimulator:
    def __init__(self):
        self.minimum = 1
        self.maximum = 6
        self.message = '''Let's Play!'''
        self.question = 'Generate Number?'

    def start(self):
        print(self.message)
        answer = input(self.question)
        try:
            if answer.lower() == 'yes':
                self.generate_number()              
            elif answer.lower() == 'no':
                print('Bye Bye!')    
            else:
                print('Yes or No')          
        except:
            print('Sorry, an error has occurred! Try Again')  


    def generate_number(self):
        print(random.randint(self.minimum, self.maximum))   

simulator = DiceSimulator()
simulator.start()


