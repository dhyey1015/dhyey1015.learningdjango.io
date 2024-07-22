
#function call without parameters
def hi():
    print("hi there")
    print("how are you?")
    
hi()

#function call with parameters

def hi(name):
    if name == 'ola':
        print("hey Ola")
    
    elif name == 'gala':
        print("hey Gala")
        
    else:
        print("hey anonymous")
        
hi('ola')

def hi(name):
    print("hi there", name)
    
hi('Rachel')