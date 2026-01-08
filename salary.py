basic=float(input("enter basic salary:"))

hra=0.20*basic
da=0.10*basic
gross=basic+hra+da
tax=0.05*gross
net_salary=gross-tax
print("HRA:",hra)
print("DA:",da)
print("Tax:",tax)
print("next salary:",net_salary)
