'''
@Description: 实现栈的数据结构
@Version: 
@Author: biofool2@gmail.com
@Date: 2018-12-07 23:53:26
@LastEditTime: 2019-03-06 00:47:27
@LastEditors: Please set LastEditors
'''


class Stack(object):
    def __init__(self):
        self._s = []
    
    def show(self):
        """显示栈内所有元素"""
        return self._s
        
    def push(self, item):
        """添加项目到栈顶"""
        self._s.append(item)
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self._s)==0
    
    def pop(self):
        """弹出栈顶元素"""
        return self._s.pop(-1)
    
    def peek(self):
        """返回栈顶部元素，但不改变栈结构，也不删除栈顶元素"""
        return self._s[-1]
    
    def size(self):
        """返回栈中项的数量"""
        return len(self._s)


def bracket_check(bracket_str):
    """检查括号是否匹配"""
    s = Stack()
    balance = True
    idx = 0
    while idx < len(bracket_str) and balance:
        br = bracket_str[idx]
        if br == "(":
            s.push(br)
        else:
            if s.is_empty():
                balance = False
            else:
                s.pop()
        idx += 1
    
    if balance and s.is_empty():
        return True
    return False


def dec_converter(dec_num, base):
    """将十进制数转换为base进制"""
    digits = '0123456789ABCDEF'

    remainder = Stack()
    while dec_num > 0:
        rem = dec_num % base
        remainder.push(rem)
        dec_num = dec_num // base
    
    base_str = ""
    while not remainder.is_empty():
        base_str += str(digits[remainder.pop()])
    
    return base_str


def infix_to_postfix(infix_expr):
    """中缀表达式转化为后缀表达式"""
    # 表达式优先级
    priority = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1
        }
    op_stack = Stack()
    post_list = []
    infix_list = infix_expr.split()

    for expr in infix_list:
        if expr.upper() in "ASDFGHJKLZXCVBNMQWERTYUIOP" or expr in '0123456789':
            post_list.append(expr)
        elif expr == '(':
            op_stack.push(expr)
        elif expr == ')':
            top_expr = op_stack.pop()
            while top_expr != '(':
                post_list.append(top_expr)
                top_expr = op_stack.pop()
        else:
            # 先把优先级高的操作符弹出
            while (not op_stack.is_empty()) and \
                (priority[op_stack.peek()] >= priority[expr]):
                post_list.append(op_stack.pop())
            op_stack.push(expr)
    
    # 剩余的操作符出栈，得到后缀表达式
    while not op_stack.is_empty():
        post_list.append(op_stack.pop())
    
    return " ".join(post_list)


def cal_postfix(postfix):
    """根据后缀表达式求值"""
    op_stack = Stack()
    post_list = postfix.split()

    def do_math(op, num1, num2):
        """计算两个数的值"""
        if op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
        elif op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        else:
            return 
    
    for pt in post_list:
        if pt in '0123456789':
            op_stack.push(int(pt))
        else:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            res = do_math(pt, op2, op1)
            op_stack.push(res)
    return op_stack.pop()


if __name__ == "__main__":
    # s = Stack()
    # print(s.is_empty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.is_empty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())
    
    # bstr1 = "((((()))))"
    # bstr2 = "()()(())()"
    # bstr3 = "()()()((())()"
    # print("Bracket string : %s , Check: %s" % (bstr1, bracket_check(bstr1)))
    # print("Bracket string : %s , Check: %s" % (bstr1, bracket_check(bstr2)))
    # print("Bracket string : %s , Check: %s" % (bstr1, bracket_check(bstr3)))

    # print(dec_converter(152, 2))
    # print(dec_converter(256, 16))
    # print(dec_converter(26, 8))

    # print(infix_to_postfix("A * B + C * D"))
    # print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    expr = "( 7 + 8 ) / ( 2 + 3 )"
    pf = infix_to_postfix(expr)
    result =  cal_postfix(pf)
    print("Infix : %s\nPostfix : %s\nResult : %d" % (expr, pf, result))