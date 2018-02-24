import random

def helloworld(emotion = None, howold = None):

    print("hello world!")
    
    if emotion:
        feeling = ['happy', 'sad', 'stressed', 'excited', 'shy']
        print("I'm feeling {} right now...".format(random.choice(feeling)))
        
    if howold:
        age = random.randint(1, 10)
        if age == 1:
            print("I'm {} year old.".format(age))
        else:
            print("I'm {} years old.".format(age))
