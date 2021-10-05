class Parent:

    def __init__(self, fName, lName, age, gender, height, eyeColor, hairColor, talents1, talents2, talents3): 
        self.fName = fName 
        self.lName = lName 
        self.age = age 
        self.gender = gender 
        self.height = height 
        self.eyeColor = eyeColor 
        self.hairColor = hairColor 
        self.talents1 = talents1 
        self.talents2 = talents2 
        self.talents3 = talents3 

dad = Parent("Bob", "Smith", 40, "Male", 6.9, "brown", "rainbow", "basket ball", "freestyling", "crochet") 

mom = Parent("Linda", "Smith", 28, "female", 4.20, "blue", "green", "tap dancing", "racing", "singing") 

parentz = [mom, dad] 

def greetParents(): 
    for parents in parentz: 
        print("Hello, my name is " + parents.fName + " " +  parents.lName + ". I am " + str(parents.age) + " years old, I have " + parents.eyeColor + " eyes, my height is " + str(parents.height) + ", I have " + parents.hairColor + " colored hair, and " + parents.hairColor + " colored hair. My 3 main talents are " + parents.talents1 + ", " + parents.talents2 + ", and " + parents.talents3) 

greetParents() 

import random 

momTalents = ["Tap dancing", "racing", "singing"] 
dadTalents = ["basket ball", "freestyling", "crochet"] 
parentsGender = ["Female", "Male"] 
momHeight = [4.20] 
dadHeight = [6.9] 
momEyeColor = ["Blue"] 
dadEyeColor = ["Brown"] 
momHairColor = ["Green"] 
dadHairColor = ["Rainbow"] 

childTalents = random.choice(momTalents) 
childTalents2 = random.choice(dadTalents) 
childGender = random.choice(parentsGender) 
childHeight = random.choice(momHeight) 
childHeight2 = random.choice(dadHeight) 
childEyeColor = random.choice(momEyeColor) 
childEyeColor2 = random.choice(dadEyeColor) 
childHairColor = random.choice(momHairColor) 
childHairColor2 = random.choice(dadHairColor)  

print("My name is Jesse smith, I'm a", childGender,  "and I'm good at", childTalents + ",", childTalents2 + ", and") 