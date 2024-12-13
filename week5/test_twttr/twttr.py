def main():
    word = input("Input:")
    print(shorten(word))



def shorten(word):
    twttr =""
    for i in word:
        if i not in ['a', 'e', 'i' ,'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            twttr = twttr + i
    return twttr


if __name__ == "__main__":
    main()


