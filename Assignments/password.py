pwd=input("Enter your password:\n")
count=0
if len(pwd)>=8:
    for i in pwd:
        if i.isupper():
            count+=1
        if i.islower():
            count+=1
        if i.isdigit():
            count+=1
        if i!=" ":
            count+=1
    if count>=4:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")