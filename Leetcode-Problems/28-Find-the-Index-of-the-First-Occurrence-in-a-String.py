# from typing import List

def hash(string):
    base = 37
    hashing = 0
    p = 1
    mod = 1_000_000_007
    for ch in string:
        val = ord(ch) - ord("a") + 1 # mapping of chars, a = 1, b = 2, ..., z = 26
        hashing = (hashing + val * p) % mod
        p = (p * base) % mod
    return hashing


def strStr(haystack: str, needle: str) -> int:
    mod = 1_000_000_007
    base = 37

    needle_hash = hash(needle)

    needle_length = len(needle)
    haystack_length = len(haystack)
    left = 0
    right = needle_length-1

    if haystack_length >= needle_length:
        sub_string = haystack[left:right+1]
        sub_string_hash = hash(sub_string)

        while right < haystack_length:
            print(haystack[left:right + 1])
            if sub_string_hash == needle_hash:
                sub_string = haystack[left:right + 1]
                if sub_string == needle:
                    return left
            hash_left_char_pointer = (ord(haystack[left]) - ord("a") + 1) * (pow(base,left) % mod)
            if not right+1 < haystack_length:
                return -1
            print("right: ", right, haystack[right+1])
            hash_right_char_pointer = (ord(haystack[right+1]) - ord("a") + 1) * (pow(base,right+1) % mod)
            sub_string_hash = hash_left_char_pointer - sub_string_hash + hash_right_char_pointer
            right += 1
            left += 1
    else:
        return -1
    return -1


haystack = "wleetco"
needle = "leetco"
print(strStr(haystack,needle))
