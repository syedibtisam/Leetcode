
def isPalindrome(s: str) -> bool:
    length = len(s)
    right = length - 1
    left = 0
    while True:
        if left == right or left > right:
            break
        if s[left].isalnum():
            if s[right].isalnum():
                left_char = s[left].lower()
                right_char = s[right].lower()
                if left_char!=right_char:
                    return False
                else:
                    right -= 1
                    left +=1
            else:
                right -= 1
        else:
            left +=1
        print(left, right)
    return True
    


s = "aa"
print(isPalindrome(s))
