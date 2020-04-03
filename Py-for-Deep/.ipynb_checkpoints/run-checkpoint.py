# run.py
import sys

def openurl(url):
    # ..본문 생략..
    print(url)

print(sys.argv[1])

if __name__ == '__main__':
    openurl(sys.argv[1])