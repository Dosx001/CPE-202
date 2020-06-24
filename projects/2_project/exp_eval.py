from stack_array import Stack


class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    s = Stack(30)
    ops = {"+": (lambda x, y: y+x), "-": (lambda x, y: y-x), "*": (lambda x, y: y*x), "/": (lambda x, y: y/x),
           "**": (lambda x, y: y**x), "<<": (lambda x, y: y << x), ">>": (lambda x, y: y >> x)}
    for i in input_str.split():
        try:
            if '.' in i:
                s.push(float(i))
            else:
                s.push(int(i))
        except ValueError:
            try:
                s.push(ops[i](s.pop(), s.pop()))
            except KeyError:
                raise PostfixFormatException('Invalid token')
            except ZeroDivisionError:
                raise ValueError
            except IndexError:
                raise PostfixFormatException('Insufficient operands')
            except TypeError:
                raise PostfixFormatException('Illegal bit shift operand')
    if s.size() == 1:
        return s.pop()
    else:
        raise PostfixFormatException('Too many operands')


def infix_to_postfix(input_str):
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    s = Stack(30)
    output = []
    ops1 = ['+', '*', '**', '<<']
    ops2 = ['-', '/', '**', '>>']
    for i in input_str.split():
        try:
            if '.' in i:
                output.append(str(float(i)))
            else:
                output.append(str(int(i)))
        except ValueError:
            if s.is_empty():
                s.push(i)
            elif i == '(':
                s.push('(')
            elif i == ')':
                c = s.peek()
                while c != '(':
                    output.append(s.pop())
                    c = s.peek()
                s.pop()
            else:
                op = s.peek()
                if op != '(':
                    x = ops1.index(i) if i in ops1 else ops2.index(i)
                    y = ops1.index(op) if op in ops1 else ops2.index(op)
                    if x > y:
                        s.push(i)
                    if x == y:
                        if i == '**' and op == '**':
                            s.push(i)
                        else:
                            output.append(s.pop())
                            s.push(i)
                    if x < y:
                        while x <= y:
                            try:
                                if i == '**' and op == '**':
                                    break
                                else:
                                    output.append(s.pop())
                                op = s.peek()
                                y = ops1.index(
                                    op) if op in ops1 else ops2.index(op)
                            except IndexError:
                                break
                            except ValueError:
                                break
                        s.push(i)
                else:
                    s.push(i)
    for i in range(s.size()):
        output.append(s.pop())
    return ' '.join(output)


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
	space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
	Returns a String containing a postfix expression(tokens are space separated)"""
    s = Stack(30)
    for i in input_str.split()[::-1]:
        try:
            if '.' in i:
                float(i)
                s.push(i)
            else:
                s.push(str(int(i)))
        except ValueError:
            s.push(s.pop()+' '+s.pop()+' '+i)
    return s.pop()
