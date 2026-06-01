def PalindromeNo(i,s):
    if(i>=len(s)//2):
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return PalindromeNo(i+1,s)

if __name__ == "__main__":
    s="madam"
    if (PalindromeNo(0,s)):
        print (" is palindrome")
    else:
        print(" is not palindrome")

    