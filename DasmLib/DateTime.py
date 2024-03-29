from enum import Enum

class WeekDay(Enum):
        MONDAY = 1,
        TUESDAY = 2,
        WEDNESDAY = 3,
        THURDAY = 4,
        FRIDAY = 5,
        SATURDAY = 6,
        SUNDAY = 7
    
class Month(Enum):
    JANUARY = 1,
    FEBRUARY = 2,
    MARCH = 3,
    APRIL = 4,
    MAY = 5,
    JUNE = 6,
    JULY = 7,
    AUGUST = 8,
    SEPTEMBER = 9,
    OCTOBER = 10,
    NOVEMBER = 11,
    DECEMBER = 12

class Date:
    year = 0
    month = 1
    day = 1
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.year = year
    
    
    
