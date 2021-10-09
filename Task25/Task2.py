from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
  looking_str = looking_str.lower()
  if len(looking_str) <= 1:
    return True
  elif looking_str[index] == looking_str[index-1]:
    return is_palindrome(looking_str[index+1 : index-1])
  else:
    return False


print(is_palindrome('Sasas'))
print(is_palindrome('mom'))
print(is_palindrome(' '))
print(is_palindrome('k'))