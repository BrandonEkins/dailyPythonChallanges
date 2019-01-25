#!/usr/bin/python3
import fileinput
st = ""
def main():
    for line in fileinput.input():
        if (fileinput.isfirstline() or fileinput.isstdin()):
            st = line
    print(st)

if __name__ == '__main__':
    main()
