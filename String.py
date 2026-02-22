def removeOuterParentheses(self, s: str) -> str:
    result = []
    count = 0
    for char in s:
        if char == '(':
            if count > 0 :
                result.append(char)
            count += 1
        else: #if chat =')'
            count -=1
            if count > 0:
                result.append(char)
    return "".join(result)


def reverseWords(self, s: str) -> str:
    words = s.split()
    return " ".join(words[::-1])  #reversed(words)


def largestOddNumber(self, num: str) -> str:
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""


def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    
    for i in range(len(strs[0])):  # iterate over first word
        for s in strs[1:]:         # compare with rest
            # if index out of range OR mismatch
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0]