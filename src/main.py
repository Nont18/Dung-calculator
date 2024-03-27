import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from components.lexica import MyLexer
from components.parsers import MyParser
from components.memory import Memory

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_1:QPushButton
    button_2:QPushButton
    # button_3:QPushButton
    # button_4:QPushButton
    # button_5:QPushButton
    # button_6:QPushButton
    button_plus:QPushButton
    button_equal:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber
    output_lcd1:QLCDNumber


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("components/main.ui", self)

        #### Binding button to function ####
        # Method 1:
        self.button_1.clicked.connect(self.push_1)
        # Method 2:
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_3.clicked.connect(lambda: self.push("3"))
        self.button_4.clicked.connect(lambda: self.push("4"))
        self.button_5.clicked.connect(lambda: self.push("5"))
        self.button_6.clicked.connect(lambda: self.push("6"))
        self.button_7.clicked.connect(lambda: self.push("7"))
        self.button_8.clicked.connect(lambda: self.push("8"))
        self.button_9.clicked.connect(lambda: self.push("9"))
        self.button_0.clicked.connect(lambda: self.push("0"))
        self.button_plus.clicked.connect(lambda: self.push("+"))
        self.button_time.clicked.connect(lambda: self.push("*"))

        self.button_equal.clicked.connect(self.push_equal)

    def push_1(self):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}1")
    
    def push(self, text:str):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")

    
    def push_equal(self):
        def isOperator(c):
            return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

        def getPriority(C):
            if (C == '-' or C == '*'):
                return 1
            elif (C == '+' or C == '/'):  # + มีpriority สูงกว่า * (ดูตามค่า)
                return 2
            elif (C == '^'):
                return 3
            return 0

        def infixToPrefix(infix):
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
                    operands.append(infix[i] + "")
        
                else:
                    while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                        op1 = operands[-1]
                        operands.pop()
        
                        op2 = operands[-1]
                        operands.pop()
        
                        op = operators[-1]
                        operators.pop()
        
                        tmp = op + op2 + op1
                        operands.append(tmp)
                    operators.append(infix[i])
        
            while (len(operators)!=0):
                op1 = operands[-1]
                operands.pop()
        
                op2 = operands[-1]
                operands.pop()
        
                op = operators[-1]
                operators.pop()
        
                tmp = op + op2 + op1
                operands.append(tmp)
            return operands[-1]



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


        print("Calculate")
        lexer = MyLexer()
        parser = MyParser()
        memory = Memory()
        input_text = self.input_text.text()
        out1 = infixToPrefix(input_text)
        out2 = infixToPostfix(input_text)
        result = parser.parse(lexer.tokenize(input_text))
        print(type(result))
        print(type(input_text))
        print(out1)
        print(out2)
        self.output_lcd.display(result)
        self.label.setText(out1)
        self.label_2.setText(out2)

        # for debug
        print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()