def is_balanced(brackets):
    stack = []

    matching_bracket = {')' : '(' , '}' : '{', ']' : '['}

    for char in brackets: 
        if char in "({[" :
            stack.append(char)

        elif char in ")}]":
            if not stack or stack[-1] != matching_bracket[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

brackets = input("masukkan striong tanda kurung: ").replace(" ", "")

print(is_balanced(brackets))