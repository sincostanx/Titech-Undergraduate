"""
In the enc(k,x), the lower case alphabets in string x is shifted 'forward' by k. 
Therefore, in order to decode the encoded string, what dec(k,x) has to do is obvious;
shift the letters 'backward' by k. In other words, dec(k,x) is equivalent to enc(-k,x).
The out of interval value x i.e. x < 0 or x > 25 is handled by using modulo operator as 
previously done in the encoding function.
"""
import sys
def enc(k,x):
    l=list(x.encode("ascii"))
    for i in range(len(l)): 
        if 97<=l[i]<=122: l[i]=(l[i]-97+k)%26+97
    return bytes(l).decode("ascii")
def dec(k,x):
    return enc(-k,x)
mode=sys.argv[1] if len(sys.argv)>1 else "enc"
if len(sys.argv)>2:
    try: k=int(sys.argv[2])
    except ValueError: print("ERROR: key must be an integer in range [0,25].");sys.exit(1)
else: k=3
s=[x.rstrip() for x in sys.stdin]
if mode=="help":
    print("python caesar.py <command> <key>")
    print(" command: enc | dec\n key: integer in range [0,25]")
elif mode=="enc" or mode=="dec":
    for x in s: print(enc(k,x) if mode=="enc" else dec(k,x))
else: print("ERROR: unknown command")