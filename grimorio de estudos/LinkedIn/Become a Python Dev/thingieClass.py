# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

# Create a example class
from dataclasses import dataclass


class Thingie():
    
    # Global class var
    BOOK_TYPES = ["HARDCOVER", "PAPER", "MANGA", "NOVEL", "GENERIC"]
    
    # The initial args on call
    def __init__(self, **kwargs):
        self._title = kwargs["title"] 
        self._description = kwargs["description"] if "description" in kwargs else "No description added."
        self._releasedate = kwargs["release"] if "release" in kwargs else "No release date added"
        
        '''         if not kwargs["type"] in Thingie.BOOK_TYPES:
            raise ValueError("Type value invalid.") '''
        
        self._type = kwargs["type"] if "type" in kwargs else "GENERIC"

    def addDesc(self, text):
        if text: 
            self._description = text
        return self._description
    
    def getDesc(self):
        return self._description
    
    def addRelease(self, date):
        if date:
            self._releasedate = date
        return self._releasedate
    
    def getRelease(self):
        return self._releasedate
    
    # Comparison 
    def __eq__(self, value):
        if not isinstance(value, Thingie):
            return ValueError("Can't compare object from different class.")
        return (self._title == value._title
                and self._type == value._type 
                and self._releasedate == value._releasedate)
        
    # >= function
    def __ge__(self, value):
        if not isinstance(value, Thingie):
            return ValueError("Can't compare object from different class.")
        return self._releasedate >= value._releasedate
    
    # < function
    def __lt__(self, value):
        if not isinstance(value, Thingie):
          return ValueError("Can't compare object from different class.")
        return self._releasedate < value._releasedate
    
    # Callabe object
    def __call__(self, **kwargs):
        self._title = kwargs["title"] 
        self._description = kwargs["description"] if "description" in kwargs else "No description added."
        self._releasedate = kwargs["release"] if "release" in kwargs else "No release date added"
        self._type = kwargs["type"] if "type" in kwargs else "GENERIC"
        
    # when the th = Thingie() is printed.
    def __str__(self):
        return f"The thingie is called {self._title}"
    
    # represents in messages and such
    def __repr__(self):
        return f"title={self._title}, releasedate={self._releasedate}, description={self._description}"
        
        
class childThingie(Thingie):
    def __init__(self):
        super().__init__

@dataclass
class gameTime:
    minutes : int
    hours : int
    days : int
    session : int
    eventTrigger : str
        
th = Thingie(title="Crosscode", description="amazing game", release="2018")
th2 = Thingie(title="Crosscode", description="amazing game", release="2018")
th3 = Thingie(title="V Rising", description="cool game", release="2022")

print(th.getRelease())
print(th.getDesc())
print(th)
print (th == th2)
print (th == th3)
print (th >= th2)
print(th < th2)

print("-------------")

thingies = [th, th2, th3]
thingies.sort()
print(thingies)

print("-------------")

gm = gameTime(1, 1, 1, 1, "laters")
gm2 = gameTime(1, 1, 1, 1, "laters")
gm3 = gameTime(2, 3, 4, 5, "lazers")

print(gm.days)
print(gm2.eventTrigger)
print(gm3)
print(gm2 == gm)