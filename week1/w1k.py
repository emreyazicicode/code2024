import random
















i1 = 3  # int
i2 = 3.5 # float
i3 = True # bool
i4 = 'Test' # str
i5 = ['a', 'b', 'c'] # list
i6 = {'age': 20} # dict
i7 = (3, 5) # tuple

print( i1, type(i1) )
print( i2, type(i2) )
print( i3, type(i3) )
print( i4, type(i4) )
print( i5, type(i5) )
print( i6, type(i6) )
print( i7, type(i7) )

# Convert
i = 14
if i == int(i / 2) * 2:
    print('even')
else:
    print('odd')


# remaining( 16 / 5 )  ==>  1
i = 13
if i % 2 == 0:
    print('even')
else:
    print('odd')


i1 = 15
i2 = i1 / 2
i3 = int(i2)
i4 = i3 * 2
i5 = i1 % 2
i6 = i4 + i5

print('i1', i1)
print('i2', i2)
print('i3', i3)
print('i4', i4)
print('i5', i5)
print('i6', i6)

i1 == int(i1 / 2) * 2 + i1 % 2

print("=" * 80)

toplam = 0
sayilar = [1,2,10,3]
toplam = sum(sayilar)

print("toplam", toplam)

# Faktoryel ( 5 ) = 5 x 4 x 3 x 2 x 1
#                   1 x 2 x 3 x 4 x 5


result = 1
N = 7
for i in range(1, N + 1):
    print("result =" , result, ", i =", i )
    result = result * i
    print(i, "! ==> durumunda,", result)
    print('------')


#* F(N) = N!
#* F(N) = 1 x 2 x 3 .... .x N
#* F(N) = N x F(N-1)


items = ['Rock', 'Paper', 'Scissors']
print( random.choice( items ), random.choice( items ) )
print( random.choice( items ) )

items = ['YAZI', 'TURA']

for i in range(10):
    print( i, random.choice( items ) )




yazilar = 0
turalar = 0

for i in range(1000000):
    if random.choice( items ) == 'YAZI':
        yazilar = yazilar + 1
    else:
        turalar = turalar + 1

print("yazilar", yazilar, "turalar", turalar)


# ===========================================

results = []
for i in range(1000):
    randomitem = random.choice( items )
    results.append( randomitem )


print( 'YAZILAR', results.count('YAZI'))
print( 'TURALAR', results.count('TURA'))

# ==========================


items = ['Rock', 'Paper', 'Scissors']

for i in range(10):
    sabina = random.choice( items )
    kamilla = random.choice( items )
    
    if sabina == 'Rock' and kamilla == 'Paper':
        print("kamilla won")
    elif sabina == 'Paper' and kamilla == 'Rock':
        print("sabina won")  
    elif sabina == 'Rock' and kamilla == 'Scissors':
        print("sabina won")
    elif sabina == 'Scissors' and kamilla == 'Rock':
        print("kamilla won")    
    elif sabina == 'Paper' and kamilla == 'Scissors':
        print("kamilla won")
    elif sabina == 'Scissors' and kamilla == 'Paper':
        print("sabina won")
    else:
        print('beraber, draw')