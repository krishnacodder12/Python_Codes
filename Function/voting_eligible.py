def voting_eligibility(a):
    if a>=18:
        print("You are eligible")
    else:
        print("You are not eligible")
age=int(input("Enter your age"))
voting_eligibility(age)
