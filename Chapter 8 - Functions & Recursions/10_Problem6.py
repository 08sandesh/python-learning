#  Write a py function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter inches : "))
cm = inch_to_cm(inch)
print(f"{cm}")