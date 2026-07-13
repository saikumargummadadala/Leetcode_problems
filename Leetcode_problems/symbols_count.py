arr=input()
#arr="###***"
hash=arr.count("#")
star=arr.count("*")
if hash-star==0:
    print("0")
elif hash-star>0:
    print("positive")
else:
    print("negative")