def isPalindrome(s):
    s = s.lower()

    s = ''.join(x for x in s if x.isalnum())

    return s == s[::-1]