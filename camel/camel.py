# invert camel case to snake case
def main():
    camelCase=input()
    for i in len(camelCase):
        if i >= 0x41 & i <=0x5A:
            print(i)
main()
