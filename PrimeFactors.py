

def prime_factors_of(n: int) -> list[int]:
    if n == 1:
        return []

    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
                break

    return factors
