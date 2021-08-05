def sum(a,b):
    return a+b;
def avg(a,b):
    return (a+b)/2;
def armstrong(n):
    sum=0;
    order = len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if sum == copy_n:
        print(n+"is a armstrong number")
        return True
    else :
        print(n+"Is not an armstrong number")
        return False
