
def calc_area(input1, input2): 
    return input1*input2

def calc_per(coso1, coso2):
    return "Perimetro: " + str((2*coso1)+(2*coso2))

val1 = float(input("dame el primer valor: "))
val2 = float(input("dame el segundo valor: "))

print(calc_area(val1,val2))
print(calc_per(val1,val2))


