latter=0
words=0
digit=0

text= input("Enter your text=")

for x in text:
    if x>='a' and 'z'>=x :
        latter = latter + 1

    elif x>='1' and x<='9':
        digit=digit + 1
    elif x==" ":
        words=words +1

print(latter)
print(words+1)
print(digit)