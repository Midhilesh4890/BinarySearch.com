def solve(ops):
        stack = []
        try:
            for i in ops:
                if i == "DUP":
                    stack.append(stack[-1])

                elif i == "-":
                    stack.append(stack.pop() - stack.pop())

                elif i == "+":
                    stack.append(stack.pop() + stack.pop())

                elif i == "POP":
                    stack.pop()

                else:
                    stack.append(int(i))
        except IndexError:
            return -1
        return stack[-1]

ops1 = ["1", "5", "DUP", "3", "-"]
ops2 = ["1", "5", "DUP", "3", "-","1", "5", "DUP", "3", "-","-"]
print(solve(ops1))
print(solve(ops2))
