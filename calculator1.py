#!/usr/bin/env python3
import sys

def calculator(x):
    if 0 >= x:
        tax_value = 0
        print("you dont't to pay the tax")
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 4500:
        tax_value = x * 0.10 - 105
    elif x <= 9000:
        tax_value = x * 0.20 - 555
    elif x <= 35000:
        tax_value = x * 0.25 - 1005
    elif x <= 55000:
        tax_value = x * 0.30 - 2755
    elif x <= 80000:
        tax_value = x * 0.45 - 5505
    else:
        tax_value = x * 0.45 - 13505
    return tax_value

if __name__ == "__main__":
    try:
        Salary = int(sys.argv[1])
        x = Salary - 3500
        tax_value = calculator(x)
        print("{:.2f}".format(tax_value))
    except Exception:
        print("Parameter Error")

