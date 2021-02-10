def solve(ops):
    stack = []
    for i in ops:
        if i=='DUP':
            if stack:
                stack.append(stack[-1])
            else:
                return -1
        elif i == '-':
            if len(stack)>=2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a-b)
            else:
                return -1

        elif i == '+':
            if len(stack)>=2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            else:
                return -1

        elif i == 'POP':
            if stack:
                stack.pop()
            else:
                return -1

        else:
            stack.append(int(i))

    return stack[-1]

ops = [""1", "5", "DUP", "3", "-""]
print(solve(ops))
