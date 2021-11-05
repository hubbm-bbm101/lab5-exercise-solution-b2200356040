e_mail = str(input("please enter an e-mail"))
if "@" not in e_mail:
    print("e-mail must include @ sign")
else:
    if "." not in e_mail:
        print("e-mail must include . sign")
    else:
        print("Valid e-mail, thank you.")

