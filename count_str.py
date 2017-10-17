#!/usr/bin/env python3
import time

start = time.clock()

if __name__ == "__main__":
    
    s = list(input("Enter a String: "))
    s_count = dict((i,s.count(i)) for i in s)
    print(s_count)

end = (time.clock() - start)
print("time used:{:}".format(end))
