P = int(input())
def make_payment(P):
    if P <= 1000 and P >= 20:
        print('Успех')
    else:
        print('Повторить попытку')
make_payment(P)