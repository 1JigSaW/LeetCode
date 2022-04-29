def romanToInt(s):
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}
    out = 0
    for j, i in enumerate(s):
        if digits[s[j]] < digits[s[min(j+1, len(s)-1)]]:
            out -= digits[str(i)]
        else:
            out += digits[str(i)]
    return out

s = "MCMXCIV"
print(romanToInt(s))
