# FirstProjectInPython
<h6>Dice Simulator for Learning Python</6>

<h1>Objective</h1>

Although the objective of the video lesson is to develop a dice simulator, my goal was to have a first contact with the python language, and even start to understand github by bringing this project here, this project does not mean that I already know how to create a data simulator, but it is the record of my first experience.

<h1>Process</h1>

I followed the video lesson available on Youtube, https://www.youtube.com/watch?v=7U3-pJZkN-o&list=PLJCanhYtZATJGhVdK8MZ0PZj_IA3uz3d9&index=3&t=65s
the challenge is to create 8 projects in Python, the first one is a dice simulator.

Throughout the process I researched each function and why it was being used, I was also modifying information and adding lines of code that I knew to further customize this learning experience.




<h1>My History</h1>

I have been working as a graphic designer for over 10 years, i am brazilian and i live in brazil, I have a degree in business administration and in 2018 I opened my company, in that period I already had 3 years of experience in remote work as a designer within an advertising agency where I interned for 6 months in face-to-face work. 

4 years ago I started taking on international projects and I've been working for an agency in China for 3 years now. (even though I'm not fluent in English, I can understand the team's requests)

in 2021 a feeling of dissatisfaction began to emerge. I tried to understand and deal with it until this year 2023 when I came to the conclusion that the time for a transition has come, I want new challenges and to learn something totally new and different from my area.



~~~python
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





