class zone():
    def __init__(self):
        self.__inhabited = False
        self.__white = True
        self.__happy = True
    
    def is_full(self):
        return self.__inhabited

    def is_white(self):
        return self.__white
    
    def is_happy(self):
        return self.__happy