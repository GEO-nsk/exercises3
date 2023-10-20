A = int(input())
B = int(input())
N = int(input())

def devide(A,B,N):
    for itr in range(1,N+1):
        if A % itr == 0 and B % itr == 0:
            print(itr)

devide(A,B,N)