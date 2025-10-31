def is_palindrome(s):
    return s == s[::-1]

def palindrome_partition(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                path.append(prefix)
                backtrack(end, path)
                path.pop()  

    backtrack(0, [])
    return result

if __name__ == "__main__":
    s = "aab"
    partitions = palindrome_partition(s)
    print("All palindrome partitions:")
    for p in partitions:
        print(p)
