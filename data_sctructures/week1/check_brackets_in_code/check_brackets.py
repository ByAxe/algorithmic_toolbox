# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []

    for i, p in enumerate(text):
        if p == '(' or p == '[' or p == '{':
            opening_brackets_stack.append(Bracket(p, i + 1))

        if p == ')' or p == ']' or p == '}':
            if len(opening_brackets_stack) != 0 and opening_brackets_stack[-1].match(p):
                del opening_brackets_stack[-1]
            else:
                opening_brackets_stack.append(Bracket(p, i + 1))
                break

    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack[-1].position)
