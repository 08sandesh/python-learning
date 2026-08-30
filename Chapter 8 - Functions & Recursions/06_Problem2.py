#  Write a python program using function to convert celsius to fahrenheit.

cel = float(input("Enter temperature in celcius : "))

def cel_to_fah(cel):
    fah = ((cel / 5) * 9) + 32
    return fah

fah = cel_to_fah(cel)
print(f"Temperature in fahrenheit is {round(fah,2)}")