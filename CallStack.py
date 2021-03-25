from DSAStack import *

def callStack(stack):
    stack.push('Method name here')
    print(stack.stack)
    stack.push('Method arguments here')
    print(stack.stack)

if __name__ == "__main__":
    method = DSAStack()
    method.set_default_capacity(2)

    print("Call stack beginning...")
    callStack(method)
    print("\n")
    print("Method being exited. Taking off the stack")
    method.pop()
    print(method.stack)
    method.pop()
    print(method.stack)