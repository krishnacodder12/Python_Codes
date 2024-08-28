sub1 = int(input("Enter first syubject marks\n"))
sub2 = int(input("Enter second syubject marks\n"))
sub3 = int(input("Enter third syubject marks\n"))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subject")
elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total persantage less than 40")
else:
    print("Congratulation! You passed the exam")