class schmitt():
    def __init__(self,lowerv,upperv,startv=0):
        self.currentv=startv
        self.upperv=upperv
        self.lowerv=lowerv
#        
    def next(self, v):
        if self.currentv == 0:
            if v > self.upperv:
                self.currentv=1
            #end if
        else:
            if v < self.lowerv:
                self.currentv=0
            #end if
        #end else - if
        return self.currentv
#    
    def reinit(self,startv=0):
        self.currentv=startv
# end class

