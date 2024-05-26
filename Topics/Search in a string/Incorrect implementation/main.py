def contains(text, pattern):
    for i in range(len(text) - len(pattern)):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False

print(contains("0110110","111"))   # Output: False
print(contains("1001011","011"))   # Output: True
print(contains("0111011","011"))   # Output: True
print(contains("00100111","111"))  # Output: True

