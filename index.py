def add (a,b):
    return a + b 

def sub (a,b) :
    return a-b

def div (a,b) :
    return a/b
    print()
def mul (a,b) :
    return a * b
    

print ( "select Operation")

Choice = input ("Enter operation (Add,sub,div,mul): ")



c = int(input("select your first number: "))
d = int(input("select you second number: "))

result = mul(c,d)

if Choice == "mul" :

    print (result)
    print  (mul(c,d))
