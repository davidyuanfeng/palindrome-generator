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
        even_palindrome = str(i)+str(i)[::-1]
        even_palindrome_list.append(int(even_palindrome))
    return even_palindrome_list

def odd_palindrome(n):
    """Returns the n = (2k+1)th digit palindrome list by concatenating the string of a (k+1)th digit integer with its reverse slice string."""
    base_palindrome_list = base_palindrome(math.floor(n/2)+1)
    odd_palindrome_list = []
    for i in base_palindrome_list:
            odd_palindrome = str(i)+str(i)[:len(str(i))-1][::-1]
            odd_palindrome_list.append(int(odd_palindrome))
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

