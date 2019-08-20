class Board:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        print('initial position is ',self.x,self.y)
        
    def pownloc(self,x,y):
        self.locX=x
        self.locY=y
        

        
    def customtravertion(self):
        self.customlocX=int(input("enter custom location for X "))
        self.customlocY=int(input("enter custom location for Y "))
        
        count=0
        if self.customlocX !=0 and self.customlocY !=0:
            slop= 8 - self.customlocY // 8 - self.customlocX

            if self.customlocY < slop:
                if self.customlocX != 8 and self.customlocY != 8:
                    print("path of moving")
                    while True:
                        self.customlocX+=1
                        self.customlocY=self.customlocY
                        print(self.customlocX, self.customlocY)
                        count+=1
                        if self.customlocX == 8 or self.customlocY == 8:
                            break

            if self.customlocY > slop:
                if self.customlocX != 8 and self.customlocY != 8:
                    print("path of moving")
                    while True:
                        self.customlocX+=1
                        self.customlocY+=1
                        print(self.customlocX, self.customlocY)
                        count+=1
                        if self.customlocX == 8 or self.customlocY == 8:
                            break
        else:
            if self.x != 8 and self.y != 8:
                print("path of moving")
                while True:
                    self.x+=1
                    self.y+=1
                    print('[',self.x,self.y,']')
                    count+=1
                    if self.x == 8 and self.y == 8:
                        break
        print("shotest move count",count)    
        

px=int(input('input pown location of x: '))
py=int(input('input pown location of y: '))

BO=Board()

    

BO.pownloc(px,py)
BO.customtravertion()

    

    
    

            
                    
                    
