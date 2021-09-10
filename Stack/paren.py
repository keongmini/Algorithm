paren = input()
stack = []

paren_dict = {"{" : "}", "(" : ")", "[" : "]"}

stack.append(paren[0])

idx = 1

while True:
    item = paren[idx]

    if paren[0] in paren_dict.values():
        print("error")
        break

    if item in paren_dict.keys():
        stack.append(item)
    else:
        if paren_dict[stack[-1]] != paren[idx]:
            print("error")
            break
        else:
            stack.pop()

    idx += 1

    if idx >= len(paren):
        break

if len(stack) != 0:
    print("error")
else:
    print("success")





