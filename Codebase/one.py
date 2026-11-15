import re
def check_password(password):
    if password=="":
        print("Password cannot be empty.")
        return
    if " " in password:
        print("Password must not contain spaces.")
        return
    score=0
    suggestions=[]
    if len(password)>=8:
        score+=1
    else:
        suggestions.append("use at least 8 characters")
    if re.search(r"[A-Z]", password):
        score+=1
    else:
        suggestions.append("add an uppercase letter")
    if re.search(r"[a-z]", password):
        score+=1
    else:
        suggestions.append("add a lowercase letter")
    if re.search(r"[0-9]", password):
        score+=1
    else:
        suggestions.append("add a digit")
    if re.search(r"[@#$%&*!]", password):
        score+=1
    else:
        suggestions.append("add a special character")
    if score<=2:
        strength="Weak"
    elif score<=4:
        strength="Medium"
    else:
        strength="Strong"
    print("Strength:",strength,"("+str(score)+"/5)")
    if len(suggestions)==0:
        print("No suggestions. Your password is secure.")
    else:
        print("Suggestions:", ", ".join(suggestions))
print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")
password=input("Enter your password: ")
check_password(password)
