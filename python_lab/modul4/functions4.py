"""
Create app that is able to respond with the provided name:

Hi Bob,
My name is Jhon
Hi Jhon
How is the weather
The weather is cold
For Jhon weather is cold

All of this will be in a function . """

def robot():
    name = 'Bob'
    def functie():
        nonlocal name
        print('Hi', name)
        name = input('My name is ')
        print('Hi ', name)
    functie()
    def weather():
        vreme = input('How is the weather ')
        print("For ", name, "the weather is ", vreme.split()[-1])
    weather()

robot()