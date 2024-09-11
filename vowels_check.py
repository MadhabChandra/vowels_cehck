

def is_vowels(text):
    vowels = ['a','e', 'i', 'o','u','A','E','I','O','U']
    result = list(filter(lambda get_vowels: ([filter_vowels for filter_vowels  in vowels if filter_vowels == get_vowels ]), text))
    return result

text =input("Input Some Text: ")
vowel = is_vowels(text)
print(vowel)