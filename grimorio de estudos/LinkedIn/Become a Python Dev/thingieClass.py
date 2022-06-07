# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

# Create a example class
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
    
    def __str__(self):
        return f"The thingie is called {self._title}"
        
# TODO: create instances of the class
th = Thingie(title="Crosscode", description="amazing game", release="2018")


# TODO: print the class and property
print(th.getRelease())
print(th.getDesc())
print(th)