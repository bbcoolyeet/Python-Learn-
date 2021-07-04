def ispalindrome(word):
    if len(word) <= 1: 
        return True
    if word[0] != word[-1]: 
        return False
    return ispalindrome(word[1:-1])
word = "aba"
print(ispalindrome(word))
