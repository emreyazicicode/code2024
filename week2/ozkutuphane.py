import re

swapped_datetime_regexes = {
    r"(\d{4})-(\d{2})-(\d{2})": "%Y-%m-%d",                      
    r"(\d{4})\.(\d{2})\.(\d{2})": "%Y.%m.%d",                      
    r"(\d{2})\.(\d{2})\.(\d{4})": "%d.%m.%Y",
    r"(\d{2})\-(\d{2})\-(\d{4})": "%d-%m-%Y",
    r"(\d{1,2})\/(\d{1,2})\/(\d{4})": "%d/%m/%Y",
    r"(\d{2})/(\d{2})/(\d{4})": "%d/%m/%Y",                      
    r"(\d{2})/(\d{2})/(\d{4})": "%m/%d/%Y",                      
    r"(\d{4})(\d{2})(\d{2})": "%Y%m%d",                          
    r"(\w+) (\d{2}), (\d{4})": "%B %d, %Y",                      
    r"(\d{2}) (\w+) (\d{4})": "%d %b %Y",                        
    r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})": "%Y-%m-%dT%H:%M:%S", 
    r"(\d{2}):(\d{2}):(\d{2})": "%H:%M:%S",                      
    r"(\d{2}):(\d{2}) ([AP]M)": "%I:%M %p",                      
    r"(\w+), (\d{2}) (\w+) (\d{4}) (\d{2}):(\d{2}):(\d{2})": "%a, %d %b %Y %H:%M:%S"
}


def findMatchingDatePattern( given: str ) -> str:
    for r in swapped_datetime_regexes:
        if re.match(r, given):
            return r
    return None


Average = lambda Values: sum(Values) / len(Values)
unique = lambda lst: list(set(lst))

def flatten(xss):
    return [x for xs in xss for x in xs]


GRAVITY = 9.8

def mToCm( m ):
    return m * 100

# method: velocity
# Calculates the velocity of an object
# @distance, float: The distance travelled
# @time, float: The time passed
# @unit, str: The unit of the calculation
# @return, float: The result of the calculation (speed)
# @completed
def velocity( distance: float, time: float, unit: str = 'm/s' ) -> float:
    #* Check the arguments
    if unit not in ['km/h', 'm/s']: # if the unit is not any of them!
        return 'ERROR'
    if not (type(distance) is float or type(distance) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    if not (type(time) is float or type(time) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    #* Check if the time is zero
    if time == 0: 
        return 0
    #* Check if the unit is km/h
    if unit == 'km/h':
        distance = distance / 1000.0
        time = time / 3600.0
    #* Make the calculation and return result
    return distance / time
