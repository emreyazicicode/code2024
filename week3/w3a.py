import datetime
Average = lambda Values: sum(Values) / len(Values)



#* class


#* to store something in memory ==> use a variable

firstname = "Ahmet"
dob = datetime.date(1990, 5, 4)
lastname = "Yildiz"

#! firstname, lastname, dob ==> belongs to "SAME PERSON"

motorcc = 1600
maxspeed = 220 # KM
gender = 'male'

# THE VARIABLES ARE INDEPENDED!!!

#! THERE IS NO CONNECTION WHICH BINDS firstname, lastname and dob [tie them up]

# SIMPLE
a = 3 # DECLARATION 
b = "selam"
c = True
d = 3.4



# COMPLEX
e = {'name': 'Ahmet'}
f = [1,2,3]
g = {'name': 'Ahmet', 'classes': ['Data Science']}

# MORE COMPLEX - MORE DETAILED

#! TEMPLATE - STRUCTURE

# STRUCTURE, TEMPLATE
# We can trust, it is not modified easily
# Advantage: MORE FIXED format, template, CONSTANT
class Student:
    firstname: str = None
    lastname: str = None
    dob: datetime.date = None

#* Those are VARIABLES BUT THEY CANNOT STORE ANYTHING YET!

print(firstname)
print(lastname)
print(dob)


s1 = Student() # CREATES A COPY!! photocopy [this copy is called "object"] product
s2 = Student() # CREATES A COPY!! photocopy
s3 = Student()
# ....
#! s1 is a variable of "A COPY OF STUDENT"
#! s1 and s2 are independed


s1.firstname = 'Ahmet'
s1.lastname = 'Yildiz'
s1.dob = datetime.date(1990, 5, 4)

#* DOT refers to genitive "nin, nin, nun"
# s1.firstname "s1'in"

s2.firstname = 'Ayse'
s2.lastname = 'Kaya'
s2.dob = datetime.date(2000, 1, 2)



print("s1.firstname", s1.firstname) # firstname in here belongs to "s1 object"
print("s1.lastname", s1.lastname)
print("s1.dob", s1.dob)

print("s2.firstname", s2.firstname)
print("s2.lastname", s2.lastname)
print("s2.dob", s2.dob)


# DICTIONARIES ARE ELASTIC
# CAN BE CHANGED EASILY
# SOMETIMES IT IS OUT OF CONTROL
# MORE FLEXIBLE
ss1 = {
    'firstname': 'Ahmet',
    'lastname': 'Yildiz',
    'dob': datetime.date(1999,5,4),
    'xx': 'yy',
    'xzdafs': 'afddsfsd'
}


class Talebe:
    #: Properties/Fields of Talebe
    isim: str = None
    soyisim: str = None
    dogum: datetime.date = None
    notlar: dict = {}

    #* The first argument in function (which are defined in classes) is "itself" ==> self
    def passedGrades( self ) -> bool:
        #passedGrades ==> belongs to class Talebe
        return Average(self.notlar.values()) > 80


def passedGradesX( t: Talebe ) -> bool:
    return Average(t.notlar.values()) > 80


spiderman = Talebe() # produced item
spiderman.isim = 'Spider'
spiderman.soyisim = 'Man'
spiderman.dogum = datetime.date(2000, 1, 1)
spiderman.notlar = {
    'maths': 78,
    'physics': 95,
    'chemistry': 67,
    'grammer': 90,
}

print("spiderman.passedGrades()", spiderman.passedGrades( ))

print( "Talebe.passedGrades( spiderman )", Talebe.passedGrades( spiderman ) )


#! SAME  spiderman.passedGrades() ==> Talebe.passedGrades( spiderman )

# When you call a function inside a class, the first argument is automatically passed
# spiderman'in passed fonksiyonunu cagir


#for i in range(500):
#    print(i)
    # burasini sonra yazacagim
    # pass # SYNTACTIC OLARAK HATA VERMESIN DIYE 
    # NO MEANING



#print////////

print("spiderman.isim", spiderman.isim)

# class veya nesnelerde, alt item'a field'a ulasmak icin, "."

"""
def talebePassed( t: Talebe ) -> bool: # input ==> talebe, output ==> fail/pass
    #* TUM NOTLARIN ORTALAMASI 80'den buyuk olacak
    if Average(t.notlar.values()) > 80: # HIDDEN  == True
        return True # Passed
    else:
        return False

def talebePassed2( t: Talebe ) -> bool: # input ==> talebe, output ==> fail/pass
    #* TUM NOTLARIN ORTALAMASI 80'den buyuk olacak
    return Average(t.notlar.values()) > 80

talebePassed3 = lambda t: Average(t.notlar.values()) > 80


print( "Average", Average(spiderman.notlar.values()))
print( "TalebePassed", talebePassed( spiderman ))
print( "TalebePassed2", talebePassed2( spiderman) )
print( "TalebePassed3", talebePassed3( spiderman) )
"""

"""
if Nigar Baku'de yasiyor ise: # SART, KOSUL, CONDITION, CHECK !!
if nigar.city == 'Baku':
if nigar.age > 18: # if nigar'in yasi 18 den buyuk ise
"""


class Department:
    name: str = None
    manager: str = None
    employees = []
    howManyProjects: int = 0
    charges: int = 0 #* TRAVEL, MEMBERSHIP, INVITATION, CONSULTING

    # SPECIAL, MAGIC FUNCTION
    # __asdsafdsfsfs__
    #* BIRISI, DEPARTMENT CLASSINA AIT OLAN BIR OBJECT'I STRING E CEVIRMEK ISTERSE
    def __str__( self ):
        return f"{self.name}: {self.manager}, HMP: {self.howManyProjects}"

    # INDEPENDED FROM THE BELOW CODE
    def departmentCount( self ) -> int:  # HOW MANY PEOPLE WORKING ON A DEPARTMENT
        return len(self.employees) + 1
    
    def efficiency( self ) -> float: # KPI
        emp_cnt = len(self.employees)
        myeff1 = self.howManyProjects / emp_cnt #! BIR EMPLOYEE'YE DUSEN DENK GELEN KARSILIK GELEN PROJE SAYISI
        myeff2 = self.charges / self.howManyProjects #! BIR PROJE BASINA DUSEN, DENK GELEN, KARSILIK GELEN, MASRAF (CHARGE) MIKTARI

        #: Return two or more items from a function
        return myeff1, myeff2 # ==> TUPLE
        # return variable1, variable2, .....

    def finalefficiency( self ) -> float: # KPI
        emp_cnt = len(self.employees)
        myeff1 = self.howManyProjects / emp_cnt #! BIR EMPLOYEE'YE DUSEN DENK GELEN KARSILIK GELEN PROJE SAYISI
        myeff2 = self.charges / self.howManyProjects #! BIR PROJE BASINA DUSEN, DENK GELEN, KARSILIK GELEN, MASRAF (CHARGE) MIKTARI

        return myeff1 / myeff2
        # return myeff1 - myeff2 / 1000.0
    



d1 = Department()
d1.name = 'R&D'
d1.howManyProjects = 16
d1.manager = 'Polat Alemdar'
d1.employees.append( 'Memati' )
d1.employees.append( 'Abdulhey' )
d1.employees.append( 'Erhan' )
d1.charges = 13000

d2 = Department()
d2.name = 'Purchasing'
d2.howManyProjects = 19
d2.manager = 'Unal Kaplan'
d2.employees.append( 'Ilyas' )
d2.employees.append( 'Alparslan' )
d2.employees.append( 'Hizir' )
d2.employees.append( 'Eniste' )
d2.charges = 17000


# MULTIPLE ASSIGNMENT
e1, e2 = d1.efficiency()
e3 = d1.efficiency()

e0 = "test"

print(f"e1: {e1}, e2: {e2}")
print("e3", e3, type(e3))


print(d1.efficiency())  #* Department.efficiency( d1 )
print(d2.efficiency())  #* Department.efficiency( d2 )



firstname, lastname = "Ahmet", "Yildiz"



f1, f2 = 3, 5
print(f"f1: {f1}, f2: {f2}")



print( d1.finalefficiency(), d2.finalefficiency())
print(d1.finalefficiency() > d2.finalefficiency())


#* Assignment:
#* Write a class of a department
#* Create at least 2 "more" KPI for calculating efficiency
#* Merge them somehow and give us a "final efficiency"



print("d1", d1)  #* __str__
#* <__main__.Department object at 0x7f8876305af0>

# BANA DEPARTMANI SOYLE, ANLAT, IFADE ET


age = 35

print(age)
print("age")
print("35")


print(3)
print("3")
print(True)
print("True")



