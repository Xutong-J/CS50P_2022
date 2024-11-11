def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) > 6 or len(s) < 2:
        return False
    #“All vanity plates must start with at least two letters.”
    for i in s[0: 2]:
        if i.isdigit():
            return False
    #“No periods, spaces, or punctuation marks are allowed.”
    if not s.isalnum():
        return False
    #“Numbers cannot be used in the middle of a plate; they must come at the end.
    #For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    cout = 0
    if s.isalpha():
        return True
    for j in s:
        cout += 1
        if j.isdigit():
            if j == "0":
                return False
            elif s[cout:].isdigit():
                return True
            else:
                return False

main()
