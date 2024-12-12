import re
import sys


#embed_code = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=3gFhPlkne8Ps5wz9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
def main():
    print(parse(input("HTML: ")))


def parse(s):
    #matches = re.search(r'^(?:<iframe)+.?scr="(.+)".*(?:</iframe>)&', s.strip())
    matches = re.search(r'src="(.)', s.strip())
    if matches:
        return matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
