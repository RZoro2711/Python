name = 'Khunn Satt Ko Ko'
def sayName() :
    print(name)
    
sayName()
print(name)


myname = 'Khunn Satt Ko Ko'
def sayName() :
    global myname
    myname = "Khunn Satt"
    print(name)

sayName()
print(myname)