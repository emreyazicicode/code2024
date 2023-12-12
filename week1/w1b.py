import sys
# week1.b


# operations

# accesing a character in a string
isim = "Ahmet"
print(isim[0])
print(isim[1])

# How to split a string
isim = "Ahmet Yildiz"
parts = isim.split(" ")

# How to join two strings
name = "Ahmet"
surname = "Yildiz"
fullname = name + " " + surname
print(fullname)

# Reading a file from a text file
fname = 'validemail.txt'
# Open the file in read mode
with open(fname, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
#: Split the "HUGE email text into LINES"

# Print the contents of the file
validemails = file_contents.split('\n')


SECURE_DOMAINS = ['gmail.com', 'hotmail.com', 'yahoo.com', 'ymail.com', 'mail.ru', 'yandex.com']

#: Declare the probabilities
PROBABILITIES = {}


def isEmailRandom( email: str ) -> bool:
    
    parts = email.split("@")
    # Rule1: The domain must be a secure domain
    if not parts[1] in SECURE_DOMAINS: return False
    # Rule2: Length
    if len(parts[0]) > 40: return False
    
    for spiderman in range(len(parts[0])-1):
        print(spiderman, parts[0][spiderman] + parts[0][spiderman+1])







"""
emails_to_test = ['ereasfddsa@hotmail.com','yaziciemre@gmail.com', 'eafdjaoidsjfq@casda.com']

for email in emails_to_test:
    print(email, isEmailRandom(email))
"""



# conversions

# application / function writing

# students.json

