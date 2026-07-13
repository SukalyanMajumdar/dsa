def facto(fact_val):
    if fact_val == 1 or 0:
        return fact_val
    else:
        return fact_val * (facto(fact_val - 1))

val1=int(input("Enter Number: "))

if val1 < 0:
    result = "Incorrect Input"
else:
    result = facto(val1)

print(result)