from validator_collection import checkers

if is_email_address := checkers.is_email('test@domain.dev'):
    print("Valid")
else:
    print("Invalid")
