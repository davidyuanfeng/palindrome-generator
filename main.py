import pandas as pd

from palindrome_generator import total_palindromes

n = 12

total_palindromes_list = total_palindromes(n)
total_palindromes_df = pd.DataFrame(total_palindromes_list, columns=["Palindromes"])
total_palindromes_df.to_csv("palindromes.csv")




