from functools import reduce
import itertools, math, operator as op


def is_prime(n):
    """Returns whether the given integer is prime"""
    
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    i = 6
    sqrt_n = int(math.ceil(math.sqrt(n)))
    
    while i <= sqrt_n + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    
    sieve = list(range(3, n + 1, 2))
    root_n = n**0.5
    mid = (n + 1) // 2 - 1
    i = 0
    m = 3
    
    while m <= root_n:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < mid:
                sieve[j] = 0
                j += m
        
        i += 1
        m = 2 * i + 3
    
    return [2] + [p for p in sieve if p]

def postponed_sieve():
    # http://stackoverflow.com/a/10733621/406772
    yield 2; yield 3; yield 5; yield 7;
    
    def add(D, x, s):
        while x in D:
            x += s
        D[x] = s
    
    # ActiveState Recipe 2002
    D = {}
    ps = (p for p in postponed_sieve())
    p = next(ps) and next(ps)
    q = p * p
    c = 9
    
    while True:
        if c not in D:
            if c < q:
                yield c
            else:
                add(D, c + 2 * p, 2 * p)
                p = next(ps)
                q = p * p
        else:
            s = D.pop(c)
            add(D, c + s, s)
        c += 2

def get_prime_factors(n):
    """
    Calculates the prime factorization of an integer, returning a dictionary of each prime factor
    and its frequency in the factorization.
    """
    factors = {}
    if n <= 1: return {}
    
    while n != 1:
        if is_prime(n):
            factors[n] = 1
            break
        
        i = 2
        while i <= n:
            j = 0
            while n % i == 0 and n != 1:
                j += 1
                n //= i
            
            if j > 0:
                factors[i] = j
                break
            i += 1
    
    return factors


def sigma(n):
    """
    Calculates the sum of the all divisors of an integer n.  
    If p and q are prime and n and m are any positive integers, then:
        sigma(p) = p - 1
        sigma(p^n) = (p^(n + 1) - 1) / (p - 1)
        sigma(p^n * q^m) = sigma(p^n) * sigma(q^m)
    """
    
    return reduce(op.mul, [(k**(v + 1) - 1) // (k - 1) for k, v in get_prime_factors(n).items()], 1)


def phi(n):
    """
    Euler's totient function, calculating the number of positive integers less
    than n that are coprime to n.  
    If p is prime and n is any positive integer, then:
        phi(p) = p - 1
        phi(p^n) = (p - 1) * p^(n - 1)
    If m and n are coprime, then:
        phi(m * n) = phi(m) * phi(n)
    """
    
    return reduce(op.mul, [(k - 1) * k**(v - 1) for k, v in get_prime_factors(n).items()], 1)


def tau(n):
    """
    The divisor function, calculating the number of divisors of any integer n.
    If n has k unique prime factors and e_i is the frequency of each prime
    factor, then:
        tau(n) = (e_1 + 1)(e_2 + 1)...(e_k + 1)
    """
    
    return reduce(op.mul, [v + 1 for k, v in get_prime_factors(n).items()], 1)

def gcd(n, m):
    """
    The greatest common divisor function, calculating the largest integer that
    divides both n and m.
    """
    
    d_n, d_m = get_prime_factors(n), get_prime_factors(m)
    
    return reduce(op.mul, [k * min(d_n[k], d_m[k]) for k in d_n if k in d_m], 1)


def factorial(n):
    if n == 0:
        return 1
    
    x = 1
    
    while n > 1:
        x *= n
        n -= 1
    
    return x

def choose(n, k):
    if k < 0 or k > n:
        return 0
    
    else:
         p, q = 1, 1
         
         for i in range(1, min(k, n - k) + 1):
            p *= n
            q *= i
            n -= 1
         
         return p // q

def is_palindrome(s):
    return s == s[::-1]

def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


# Base conversions

def dec2bin(n):
    s = ''
    while n > 0:
        s = str(n & 1) + s
        n >>= 1
    return s
