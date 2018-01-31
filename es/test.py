from jnius import autoclass

Stack = autoclass('java.util.Stack')
print Stack
stack = Stack()
stack.push('hello')
stack.push('world')

print stack.pop() # --> 'world'
print stack.pop() # --> 'hello'
