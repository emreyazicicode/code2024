
import datetime
import logging
logging.basicConfig(filename='week3.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a', datefmt='%H:%M:%S', level=logging.DEBUG)

logging.info('Application started')


class Talebe:
    number: int = 0
    dob: datetime.date = None
    name: str = None

    def __init__( self, givendob: datetime.date ):
        self.dob = givendob

    def age( self ) -> int:
        now_year = datetime.date.today().year
        return now_year - self.dob.year

    def canJoinToMasterDegree( self ) -> bool:
        return self.age() > 22

    def __str__( self ):
        return f"{self.name}, {self.number}"


t = Talebe( datetime.date(2002, 1,1) )
print("t.dob", t.dob)
t.number = 123
t.name = "Ahmet Yildiz"

logging.info(f"Talebe olustu:{t}")

print( "t.canJoinToMasterDegree()", t.canJoinToMasterDegree() )

#: program calisitigi anda, bir tane mesaj yazalim

a = 3
c = 0

try:
    b = a / c
except Exception as e:
    logging.error(f'Burada bir kere hata olustu: {e}, a = {a}, c = {c}')

#* FINDEKS ==> bankacilik kredi skoru
#* age = 0
#* age = -1
