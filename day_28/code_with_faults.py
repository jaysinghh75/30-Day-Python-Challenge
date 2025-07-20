class d:
 def __init__(self,x =5,y =10 ):
  self.x= x
  self.y =y
 def a(self):
  return self.x+self.y
 def b(self):return self.x*self.y

def main():
    data = d( )
    sum = data.a( ) ;prod=data.b()
    print("sum:",sum) ;print( "product: ",prod)


def greet( name ):
 print("Hello,",name)

def agecheck( age ):
 if age <18:
  print("Minor" )
 elif age>=18 and age <=60:
  print( "Adult" )
 else:print("Senior")

greet(" virat") ;agecheck(25)
main()