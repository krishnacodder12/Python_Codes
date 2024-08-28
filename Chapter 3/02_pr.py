letter=''' Dear <|Name|>,
Greeting From DSCET. I am happy to tell you about your selection.
You Are Selected!
<|Date|>'''
name=input("Enter Your Name\n")
date=input("Enter your Date\n")
letter = letter.replace("|Name|" ,name)
letter = letter.replace("|Date|" ,date)
print(letter)