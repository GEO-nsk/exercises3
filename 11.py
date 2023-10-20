N = int(input())

def simple_numbers(N):

    for itr in range(1,N):
        Flag = True
        for x in range(2,itr):
            if itr % x == 0:
                Flag = False
        if Flag:
            print(itr)

simple_numbers(N)