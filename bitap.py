def bitap(pattern, text, k=2):  # k = max errors allowed
    m, n = len(pattern), len(text)
    state = 1 << m  # Bitmask for pattern matches
    for i in range(n):
        word = 0
        for j in range(m + 1):
            if (state & (1 << j)) and (j == m or text[i] == pattern[j]):
                word |= (1 << j)
        state = ((state << 1) | 1) & word
        if state & (1 << m):
            return i - m + 1  # Approximate match found
    return -1