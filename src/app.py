import sys
import os

def palindrome(s):
    #remove all spaces and make uppercase
    new_s = (s.replace(' ','')).upper()
    #iterate to check if first half is the same as second half of input
    for i in range(int(len(new_s)/2)):
        if new_s[i] != new_s[len(new_s)-1-i]:
            return False
    return True

def solution(s):
    return palindrome(s)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))