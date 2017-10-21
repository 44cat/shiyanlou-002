#!/usr/bin/env python3
import sys
import csv
import os

def calculator_tax(WorkerNumber,Salary,JiShuL,JiShuH,Jrate):
    lst = []
    tax_value = 0
    
    if Salary < JiShuL:
        FiveFound = JiShuL * Jrate
    elif Salary > JiShuH:
        FiveFound = JiShuH * Jrate
    else:
        FiveFound = Salary * Jrate

    taxable_income = Salary - FiveFound - 3500
    x = taxable_income

    def tax(x):
        if 0 > x:
            tax_value = 0
        elif x <= 1500:
            tax_value = x * 0.03 - 0
        elif x <= 4500:
            tax_value = x * 0.1 - 105
        elif x <= 9000:
            tax_value = x * 0.20 - 555
        elif x <= 35000:
            tax_value = x * 0.25 - 1005
        elif x <= 55000:
            tax_value = x * 0.30 - 2755
        elif x <= 80000:
            tax_value = x * 0.35 - 5505
        else:
            tax_value = x * 0.45 - 13505
        return tax_value
    
    TaxValue = tax(x)
    RealIncome = Salary - TaxValue - FiveFound
    lst = [WorkerNumber,Salary,format(FiveFound,'.2f'),format(TaxValue,'.2f'),format(RealIncome,'.2f')]
    
    return lst

class Config(object):
    def __init__(self,configfile):
        self.configfile = configfile
        self._configdict = {}

    def get_config(self):
        with open(self.configfile,'r') as f:
            for line in f.readlines():
                if line is not None:
                    config_key = line.split(" = ")[0].strip()
                    config_value = line.split(" = ")[1].strip(' \n')
                    #add to _configdict dict
                    self._configdict[config_key] = config_value

        return self._configdict

class UserData(object):
    def __init__(self,userdatafile):
        self.userdata = []
        self.userdatafile = userdatafile

    def get_userdata(self,JiShuL,JiShuH,Jrate):
        with open(self.userdatafile,'r') as f:
            for line in f.readlines():
                if line is not None:
                    k = line.split(',')[0].strip()
                    v = line.split(',')[1].strip(' \n')
                    v = float(v)
                    s = calculator_tax(k,v,JiShuL,JiShuH,Jrate)
                    self.userdata.append(s)

    def dumptofile(self,outputfile,default="csv"):
        with open(outputfile,"w",newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.userdata)

#def main():
if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        index = args.index
        configfile = args[index('-c')+1]
        userdatafile = args[index('-d')+1]
        outputfile = args[index('-o')+1]

        config = Config(configfile)
        userdata = UserData(userdatafile)

        JiShuL = float(config.get_config()['JiShuL'])
        JiShuH = float(config.get_config()['JiShuH'])
        YangLao = float(config.get_config()['YangLao'])
        YiLiao = float(config.get_config()['YiLiao'])
        ShiYe = float(config.get_config()['ShiYe'])
        GongShang = float(config.get_config()['GongShang'])
        ShengYu = float(config.get_config()['ShengYu'])
        GongJiJin = float(config.get_config()['GongJiJin'])

        Jrate = YangLao+ YiLiao+ ShiYe + GongShang + ShengYu + GongJiJin
        #print(Jrate)       
        userdata.get_userdata(JiShuL,JiShuH,Jrate)
        userdata.dumptofile(outputfile)

    except Exception as e:
        print(e)
        sys.exit()
    if os.path.isfile(configfile) == False or os.path.isfile(userdatafile) == False:
        print('Parameter Error')
        sys.exit()


#if __name__ == "__main__":
#    main()
