from validator_collection import checkers

if is_email_address := checkers.is_email(input("What's your email address?")):
    print("Valid")
else:
    print("Invalid")
