a=input("Enter your letter:\n")
vowell=["a","e","i","o","u"]
count=0
for i in a:
    if i not in vowell:
        count=count+1
print(count)