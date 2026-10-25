class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # calculate while iterating over tokens list, do one eval at the end


        numbers = []
        expression = ""

        for c in tokens:
            if c == '+':
                val2 = numbers.pop()
                val1 = numbers.pop()
                numbers.append(val1 + val2)
            elif c == "-":
                val2 = numbers.pop()
                val1 = numbers.pop()
                numbers.append(val1 - val2)
            elif c == "*":
                val2 = numbers.pop()
                val1 = numbers.pop()
                numbers.append(val1 * val2)
            elif c == "/":
                val2 = numbers.pop()
                val1 = numbers.pop()
                numbers.append(int(val1 / val2))
            else:
                numbers.append(int(c))
        return int(numbers.pop())

        # calculate while iterating over tokens list

        operations = {'+', '-', '*', '/'}

        values = []

        for token in tokens:
            if token not in operations:
                values.append(int(token))
            else:
                val2 = values.pop()
                val1 = values.pop()
                values.append(int(eval(f"{val1} {token} {val2}")))
        return values[0]