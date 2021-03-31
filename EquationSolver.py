from DSAQueue import *
from DSAStack import *

class EquationSolver():
    def solve(self, str_equation):
        queue = self._parseInfixToPostfix(str_equation)
        result = self._evaluatePostfix(queue)
        return round(result, 4)
        # return float
        

    def _parseInfixToPostfix(self, str_equation):
        infix = str_equation.split(" ")
        postfix = DSAShuffleQueue()
        opStack = DSAStack()

        for term in infix:
            if term == "(":
                opStack.push('(')
            elif term == ")":
                while opStack.top() != ('('):
                    postfix.enqueue(opStack.pop())
                opStack.pop()
            elif term == "+" or term == "-" or term == "*" or term == "/":
                while (not opStack.isEmpty()) and (opStack.top != '(') and self._precedenceOf(opStack.top()) >= self._precedenceOf(term):
                    postfix.enqueue(opStack.pop())
                opStack.push(term)
            else:
                postfix.enqueue(term)
        while opStack.count > 0:
            postfix.enqueue(opStack.pop())
        
        return postfix

    def _evaluatePostfix(self, postfixQueue):
        # take postfix queue and evaluate
        operands = DSAStack()

        for item in postfixQueue.queue:
            if item == "+" or item == "-" or item == "*" or item == "/":
                one = operands.pop()
                two = operands.pop()
                result = self._executeOperation(item, float(two), float(one))
                operands.push(result)
                # operands.push('operator')
            elif item == None:
                # operands.push('neg')
                pass
            else:
                # operands.push('operand')
                operands.push(item)


        # return float
        return operands.stack[0]

    def _precedenceOf(self, theOp):
        if theOp == "+" or theOp == "-":
            prec = 1
        elif theOp == "*" or theOp == "/":
            prec = 2
        else:
            prec = 0
        return prec

    def _executeOperation(self, op, op1, op2):
        if op == "+":
            result = op1 + op2
        elif op == "-":
            result = op1 - op2
        elif op == "*":
            result = op1 * op2
        elif op == "/":
            result = op1 / op2
        else:
            print("execution failed")
            result = None
        return result

