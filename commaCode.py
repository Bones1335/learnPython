spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(list):
    newString = ''
    for i in list:
        newString += str(i)
        if i == list[-2]:
            newString += ', and '
        elif i == list[-1]:
            newString = newString
        else:
            newString += ', '

    return newString

print(commaCode(spam))
print(commaCode([]))
print(commaCode(['George', 'Alice', 'Bob', 'Katy', 'Juniper', 'Stacy']))
