#The Recursion is supposed to be the way which allows us to solve problems that can be broken down into multiple subtasks.
def removeOuterParentheses(self, s: str) -> str:
    result = []
    count = 0
    for char in s:
        if char == '(':
            if count > 0:
                result.append(char)
            count += 1
        else:
            count -= 1
            if count >0:
                result.append(char)
    return "".join(result)





