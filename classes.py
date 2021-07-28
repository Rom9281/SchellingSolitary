class box():    
    def __init__(self):
        self.__inhabited = False
        self.__white = True
        self.__happy = True
        self.__canvas_body = False

        self.__aff_process  = -1
        self.__neighbors = []
    
    def is_full(self):
        return self.__inhabited

    def is_white(self):
        return self.__white
    
    def is_happy(self):
        return self.__happy

    def set_empty(self):
        self.__inhabited = False
    
    def set_full(self):
        self.__inhabited = True
    
    def set_black(self):
        self.__white = False
    
    def set_white(self):
        self.__white = True
    
    def set_happy(self):
        self.__happy = True
    
    def set_angry(self):
        self.__happy = False
    
    def set_process_id(self,num):
        self.__aff_process = num
    
    def aff_process(self):
        return self.__aff_process
    
    def add_neighbors(self,nei_tupple):
        self.__neighbors.append(nei_tupple)

    