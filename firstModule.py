def puissance(n, i):
    return n**i;

def direBonjour(nom):
    print('Bonjour M./Mme /Mlle {}'.format(nom));
    
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)