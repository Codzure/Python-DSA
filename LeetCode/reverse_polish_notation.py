#reverse polish notation

# Question: Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any divide by zero operation.

# You are given an array of strings tokens that represents a valid Reverse Polish Notation (RPN) expression.
# Return the value of the RPN expression.

# Example 1:
# Input: tokens = ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

def reverse_polish_notation(tokens): 
    stack = [] 
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]


# Time complexity: O(n)
# Space complexity: O(n)

print(reverse_polish_notation(["2", "1", "+", "3", "*"]))  # Output: 9



#The function initializes an empty list called stack to serve as the stack. It then iterates over each token in the input list. 
# If the token is an operator, the function pops the top two elements from the stack (these are the operands for the operator). 
# It then applies the operator to these operands and pushes the result back onto the stack. For example, 
# if the operator is +, it adds the two operands and pushes the sum onto the stack. If the token is an operand (a number), 
# it converts the token to an integer and pushes it onto the stack.

#Finally, the function returns the first element of the stack, which is the result of evaluating the expression.



# This function evaluates the given arithmetic expression in reverse Polish notation.
# The function uses a stack to store the operands and performs the arithmetic operations based on the operators.
# The time complexity of this function is O(n), where n is the number of tokens in the input list.
# The function iterates through each token in the list and performs the corresponding operation.

