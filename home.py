num1=int(input("Number: "))
name="Mcdonald"
names=["Charles", "Marvelos", "Mitchel", "Anesu", "Brighton"]
if num1>0:
    user=str(input("Input new Name: "))
    names.append(user)
    names.sort()
    print(names)
elif num1<0:
    print(name)
else:
    print(names[2])
