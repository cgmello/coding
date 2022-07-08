from numpy.lib.scimath import sqrt
import math as m


class Solution(object):
    # Sieve of Eratosthenes
    def countPrimes(self, n):
        if n < 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(m.ceil(m.sqrt(n)))):
            if isPrime[i]:
                # set all multiples as not prime too
                for multiples in range(i * i, n, i):
                    isPrime[multiples] = False

        return sum(isPrime)

    """
    # Brute Force
    def countPrimes(self, n):
        total = 0
        last_prime = 2
        for i in range(2, n):
            if self.isPrime(i, last_prime):
                print(f"{i} is prime")
                i += 2
                last_prime = i
                total += 1
        return total

    def isPrime(self, num, last_prime):
        for i in range(2, num - 1):
            if num % i == 0:
                return False
        return True
    """


s = Solution()
print(s.countPrimes(499979))
