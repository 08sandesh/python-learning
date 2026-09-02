#  Check whether a year is a leap year or not.

year = int(input("Enter year : "))

if year<0:
    print("Enter valid year")
elif year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
