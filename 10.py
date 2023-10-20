A = int(input())
B = int(input())

def counter(A,B):

    Flag = True

    if A < B:
        start = A
        end = B
    else:
        start = B
        end = A

    for itr in range(start,end+1):
        itr = str(itr)
        Flag = True
        for number in itr:
            if number == '2' or number == '5' or number == '6' or number == '7' or number == '0':
                Flag = False
        if Flag:
            print(itr)
counter(A,B)