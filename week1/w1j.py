










# string operations
# text(s) given text out
a = "b" + "c" # concat

# Text given, list out
parts = "emre@yazici.com".split("@")

text = "Hi Mustafa"
text = text.replace("Hi", "Hello")
print(text)

text = ""
text = '     baku        city   \n'.strip()
print(text)

text = '"Hello"     '.strip('" ')
print(text)


# string operations
#* a = "bc"
# TODO 
# NOTE xxx
#! hata WARNING


salary1 = "15000 AZN"
salary2 = 1200
salary3 = 1700.45

salary1 = str(salary1).replace('AZN', '').strip()
salary2 = str(salary2).replace('AZN', '').strip()
salary3 = str(salary3).replace('AZN', '').strip()

print(salary1)
print(salary2)
print(salary3)


