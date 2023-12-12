
"""
graph TD
    a[Load valid emails from a file]
    b[Split valid emails to lines]

    c[Checking email address]
    d[Split by @]
    e[Check domain in secure]
    f[Check name]
    g[Find two letter combinations]
    h[Create a dictionary of occourances]
    z[Check length]

    a-->b

    c-->d
    c-->e
    c-->z

    c-->f
    f-->g
    f-->h


https://mermaid.liv
"""

import json
import string
import random
# List of lowercase letters
lowercase_letters = list(string.ascii_lowercase)


# Specify the filename
filename = 'PROBABILITIES.json'


# Reading JSON data
with open(filename, 'r') as f:
    PROBABILITIES = json.load(f)


SECURE_DOMAINS = ['gmail.com', 'hotmail.com', 'yahoo.com', 'ymail.com', 'mail.ru', 'yandex.com']


def isEmailRandom( email: str ) -> int:
    
    parts = email.split("@")
    # Rule1: The domain must be a secure domain
    if not parts[1] in SECURE_DOMAINS: return False
    # Rule2: Length
    if len(parts[0]) > 40: return False
    

    total = 0
    for spiderman in range(len(parts[0])-1):
        twoletter = parts[0][spiderman] + parts[0][spiderman+1]
        if twoletter in PROBABILITIES:
            prob = PROBABILITIES[ twoletter ]
            total = total + prob

    return total


print( isEmailRandom('johnsmith@gmail.com') )
print( isEmailRandom('fasjdsofa@gmail.com') )


# print(lowercase_letters)
# print(random.choice(lowercase_letters))


def createRandomCharacter() -> str:
    return random.choice(lowercase_letters)

def createRandomEmailAddress(length: int) -> str:
    text = ""
    for i in range(length):
        text = text + createRandomCharacter()

    return text



def sigma( items:list ) -> int:
    total = 0
    for i in items:
        total = total + i
    return total



scores = []
for i in range(50000):
    randomgenerated = createRandomEmailAddress(9) + '@gmail.com'
    score = isEmailRandom( randomgenerated )
    scores.append( score )


print(scores)
print("toplam", sigma( scores ))
print("average", sigma( scores ) / len( scores ))


print( "scores", sum(scores) / len(scores) )

mx = 0
mi = None
for k in PROBABILITIES:
    if PROBABILITIES[k] > mx:
        mx = PROBABILITIES[k]
        mi = k

print(mx, mi)


# Sorting the dictionary by values in descending order
sorted_dict = {k: v for k, v in sorted(PROBABILITIES.items(), key=lambda item: item[1], reverse=True)}


# Reading a file from a text file
fname = 'validemail.txt'
# Open the file in read mode
with open(fname, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
#: Split the "HUGE email text into LINES"

# Print the contents of the file
validemails = file_contents.split('\n')


valid_scores = []
for i in range(10000):
    validemails[i] = validemails[i].lower()
    if len(validemails[i].split('@')[0]) == 9:
        score = isEmailRandom( validemails[i].split('@')[0] + '@gmail.com' )
        valid_scores.append( score )

print( "valid_scores", sum(valid_scores) / len(valid_scores) )