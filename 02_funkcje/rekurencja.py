# 3! = 3 * 2!
#
# n! == n * (n - 1)!
# 0! == 1
#
# def silnia(n):
#     if n == 0:
#         return 1
#     return n * silnia(n-1)
#
# silnia(3)
#
# 3 * silnia(2) -> 3 * 2 * silnia(1) = 3 * 2 * 1 * silnia(0)  = 3 * 2 * 1 * 1

def licznik(n):
    print(n)
    licznik(n+1)
    
licznik(5)