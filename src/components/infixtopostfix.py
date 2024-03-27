def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z')) #ผลลัพธ์เป็นได้แค่ 1 กับ 0
 
def getPriority(C):
    if (C == '-' or C == '*'):
        return 1
    elif (C == '+' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0
 

def infixToPostfix(infix): #infix คือ 1+2
    operators = []
    operands = []
 
    for i in range(len(infix)):
        
        if (infix[i] == '(' ):
            operators.append(infix[i])
 
        elif (infix[i] == ')'):
            while (len(operators)!=0 and (operators[-1] != '(' )):
                op1 = operands[-1]
                operands.pop()
                op2 = operands[-1]
                operands.pop()
                op = operators[-1]
                operators.pop()
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.pop()
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "") #operands = [1,2]
 
        else:
            while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()
 
                op2 = operands[-1]
                operands.pop()
 
                op = operators[-1]
                operators.pop()
 
                tmp =  op2 + op1 + op
                operands.append(tmp)
            operators.append(infix[i]) #operators = [+]
 
    while (len(operators)!=0):
        op1 = operands[-1]
        operands.pop()
 
        op2 = operands[-1]
        operands.pop()
 
        op = operators[-1]
        operators.pop()
 
        tmp =  op2 + op1 + op
        operands.append(tmp)
    return operands[-1]

while(1):
    s = input("Infix Expression : ")
    print("Postfix Expression : ", infixToPrefix(s))
    
# Step 1: Reverse the infix string. Note that while reversing the string you must interchange left and right parentheses.
# Step 2: Obtain the postfix expression of the infix expression Step 1.
# Step 3: Reverse the postfix expression to get the prefix expression