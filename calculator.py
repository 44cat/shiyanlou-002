#!/usr/bin/env/ python

def calculator():
    global x
    if 0>= x:
        tax_value = 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    elif x <= 1500:
        tax_value = x * 0.03 - 0
    else:
        tax_value = x * 0.45 - 13505
    return tax_value

def show():
    tax = calculator()
    real_income = int(Salary - tax)
    print('您本月应缴个人所得税:{:.2f}元'.format(tax))
    print('税后收入为:{:.2f}元'.format(real_income))

if __name__ == "__main__":
    Salary = int(intput("亲输入您这个月总收入:"))
    x = Salary - 3500
    show()
