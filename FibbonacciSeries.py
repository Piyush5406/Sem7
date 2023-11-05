def non_recursive(n):
    first=0
    second=1
    print(first)
    print(second)
    while n-2> 0:
        third=first+second
        first=second
        second=third
        print(third)
        n=n-1
n=10
print("-------Recursive----------")
def recursive(n):
    if n<=1:
        return n
    else:
        return recursive(n-1)+recursive(n-2)

for i in range(n):
    print(recursive(i))
print("-------Non Recursive------")
non_recursive(n)
