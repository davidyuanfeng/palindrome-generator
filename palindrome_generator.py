import math

def base_palindrome(k):
    """Returns the (k)th digit integer list."""
    base_palindrome_list = []
    for i in range(10**(k-1),10**(k)):
        base_palindrome_list.append(i)
    return base_palindrome_list

def even_palindrome(n):
    """Returns the n = (2k)th digit palindrome list by concatenating the string of a (k)th digit integer with its reverse string."""
    base_palindrome_list = base_palindrome(int(n/2))
    even_palindrome_list = []
    for i in base_palindrome_list:
        palindrome = str(i)+str(i)[::-1]
        even_palindrome_list.append(int(palindrome))
    return even_palindrome_list

def odd_palindrome(n):
    """Returns the n = (2k+1)th digit palindrome list by concatenating the string of a (k+1)th digit integer with its reverse slice string."""
    base_palindrome_list = base_palindrome(math.floor(n/2)+1)
    odd_palindrome_list = []
    for i in base_palindrome_list:
            palindrome = str(i)+str(i)[:len(str(i))-1][::-1]
            odd_palindrome_list.append(int(palindrome))
    return odd_palindrome_list

def palindromes(n):
    """Returns the (n)th digit palindrome list."""
    if n % 2 == 0:
        palindrome_list = even_palindrome(n)
    else:
        palindrome_list = odd_palindrome(n)
    return palindrome_list

def total_palindromes(n):
    """Returns the palindrome list up to the (n)th digit."""
    total_palindrome_list = []
    for k in range(1,n+1):
        total_palindrome_list.extend(palindromes(k))
    return total_palindrome_list

def prime_test(n):
    """Tests if the number is prime."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def palindrome_prime(n):
    """Returns a list of prime palindromes up to the (n)th digit."""
    total_palindrome_list = total_palindromes(n)
    prime_palindrome_list = []

    for p in total_palindrome_list:
        if prime_test(p):
            prime_palindrome_list.append(p)
    return prime_palindrome_list
