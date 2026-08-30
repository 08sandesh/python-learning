#  Repeat Program4 for a list of such words to be censored

words = ["Donkey" , "ganda" , "bad"]

for word in words:
    with open("Donkey.txt") as f:
        data = f.read()
        newdata = data.replace(word,"#"*len(word))
        with open("Donkey.txt","w") as f:
            f.write(newdata)