#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    if len(sys.argv) > 1:
        for i in (sys.argv[1:]):
            sum += int(i)
    print(sum)
