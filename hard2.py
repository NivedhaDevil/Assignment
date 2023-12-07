def shortestPalindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    if i == len(s):
        return s

    suffix = s[i:]
    return suffix[::-1] + shortestPalindrome(s[:i]) + suffix

user_input = input("Enter a string: ")

if user_input.isalpha():
    result = shortestPalindrome(user_input)
    print(result)
else:
    print("Invalid input. Please enter a string consisting of lowercase English letters only.")
