
#if ---------------------------------------------------------------------------
if 3 > 2:
    print("it works")


#if else part ---------------------------------------------------------------------    
if 5>2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")


#elif part-------------------------------------------------------------------------
name = "xyz"

if name == "abc":
    print("hello, abc")
    
elif name == "xyz":
    print("hello, xyz")
    
else:
    print("hey anonymous")
    
#more elif-------------------------------------------------------------
    
volume = 57

if volume < 20:
    print("Its equivalent to quiet.")

elif volume < 40:
    print("Its nice for backgroung music.")
    
elif volume < 60:
    print("Perfect! i can hear all the details.") 

elif volume < 80:
    print("Nice for parties")
    
elif 80<= volume < 100:
    print("A bit loud")
    
else:
    print("My ears are hurting :(")
    
    
    