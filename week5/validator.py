def check_p(p):
    return len(p) >= 8 and any(x.isupper() for x in p)
print("Password is good" if check_p("Pass1234") else "Too weak")
