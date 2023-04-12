def is_palindrom(word):
    return word==word[::-1]
print(is_palindrom("madam"))
print(is_palindrom("horse"))
