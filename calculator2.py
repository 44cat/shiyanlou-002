#!/usr/bin/env python3
import sys

def calculator(x):
    if 0 >= x:
        tax_value = 0
        #print("you dont't to pay the tax")
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

def main():
	try:
		for i in (sys.argv[1:]):
			work_number = int(i.split(':')[0])
			#print(work_number)
		#print(type(work_number))
			Salary = int(i.split(':')[1])
		#print(Salary)
		#print(type(Salary))
			Five_found = Salary * 0.165
		#print(Five_found)
			taxable_income = Salary - 3500 - Five_found
			x = taxable_income
		#print(x)
			tax_value = calculator(x)
		#print(tax_value)
			real_income = Salary - Five_found - tax_value
		#print(real_income)
			Real_income = "{:.2f}".format(real_income)
		#print(real_income)
			L = str(work_number) + ':' + str(Real_income)
			print(L)
		#x = Salary - 3500
		#tax_value = calculator(x)
		#print("{:.2f}".format(tax_value))
	except Exception:
		print("Parameter Error")

if __name__ == "__main__":
	main()
