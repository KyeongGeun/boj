MOD = 1_000_000_007

def q_pow(a, n):

    if n == 0:
        return 1
    if n == 1:
        return a

    ans = q_pow(a, n//2) ** 2

    if n%2:
        ans = ans * a
    
    ans %= MOD

    return ans

def docagne(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    if n//2 not in memo.keys():
        memo[n//2] = docagne(n//2)
    if n//2+1 not in memo.keys():
        memo[n//2+1] = docagne(n//2+1)
    
    if n % 2:
        return ( q_pow( memo[n//2], 2 ) + q_pow( memo[n//2+1], 2 ) ) % MOD
    
    else:
        if n//2-1 not in memo.keys():
            memo[n//2-1] = docagne(n//2-1)
        return memo[n//2] * ( memo[n//2-1] + memo[n//2+1] ) % MOD

memo = {}

n = int(input())

print(docagne(n))