N = int(input())
s = [1,1]

def fibonachi(N):
    for itr in range(N-2):
        number = s[-1] + s[-2]
        s.append(number)
    for itr in s:
        print(itr)

fibonachi(N)