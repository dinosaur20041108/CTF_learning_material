import sys
def recurse(count):
    if count<=0:
        return
    print(f"Recursion{10-count+1}",end=" ")
    recurse(count-1)

recurse(10)