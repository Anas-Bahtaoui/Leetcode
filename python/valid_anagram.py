from collections import Counter

def valid_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    s_counter = Counter(s)
    t_counter = Counter(t)

    for key, value in s_counter.items():
        if key not in t_counter:
            return False
        if value != t_counter[key]:
            return False

    return True

if __name__ == '__main__':

    s = "anagram"
    t = "nagaram"
    print(valid_anagram(s, t))

    s = "rat"
    t = "car"
    print(valid_anagram(s, t))