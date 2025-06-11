import os
import operations as op

if __name__ == "__main__":
    while True:
        try:
            os.system("clear")
            print('\t'*5,"MATRIX CACULATOR")
            print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''",'','',sep='\n')
            print('\n'*2)
            print("OPERATIONS ON MATRICES")
            print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            
            print("0, EXIT", "1, ADDITION OF 2 MATRICES",\
                "2, SUBSTRACTION OF 2 MATRICES", "3, SCALAR MULTIPLICATION OF MATRICES",\
                "4, MULTIPLICATION OF 2 MATRICES", "5, DETERMINANT CALCULATION",\
                "6, ADJOINT OF A MATRIX", "7, INVERSE OF A MATRIX",\
                "8, TRANSPOSE OF A MATRIX", "9, HISTORY",sep="\n")

            print()
            a = int(input("ENTER YOUR CHOICE(0/1/2/3/4/5/6/7/8/9): "))
            print()
        
            if a == 1:
                b = int(input("ENTER THE NO. OF ROWS: "))
                c = int(input("ENTER THE NO. OF COLUMNS:"))
                if b == 0 or c == 0:
                    print("ENTER VALID ORDER")
                else:
                    d = op.add(b,c)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in d:
                        print(i)
                    print('\n'*3)
            elif a == 2:
                e = int(input("ENTER THE NO. OF ROWS: "))
                f = int(input("ENTER THE NO. OF COLUMNS:"))
                if e == 0 or f == 0:
                    print("ENTER VALID ORDER")
                else:
                    g=op.sub(e,f)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in g:
                        print(i)
                    print('\n'*3)
                        
            elif a == 3:
                e = int(input("ENTER THE NO. OF ROWS: "))
                f = int(input("ENTER THE NO. OF COLUMNS:"))
                if e == 0 or f == 0:
                    print("ENTER VALID ORDER")
                else:
                    g=op.smul(e,f)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in g:
                        print(i)
                    print('\n'*3)
                        
            elif a == 4:
                e =int(input("ENTER THE NO. OF ROWS OF FIRST MATRIX: "))
                f =int(input("ENTER THE NO. OF COLUMNS OF FIRST MATRIX: "))
                g =int(input("ENTER THE NO. OF ROWS OF SECOND MATRIX: "))
                h = int(input("ENTER THE NO. OF COLUMNS OF SECOND MATRIX: "))
                if e == 0 or f == 0 or g == 0 or h == 0:
                    print("ENTER VALID ORDER")
                elif f != g:
                    print("NO. OF COLUMNS OF FIRST MATRIX SHULD BE EQUAL TO THE NUMBER OF ROWS OF SECOND MATRIX")
                else:
                    I = op.mul(e,f,g,h)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in I:
                        print(i)
                    print('\n'*3)
                        
            elif a == 5:
                e = int(input("ENTER THE NO. OF ROWS: "))
                if e == 0:
                    print("ENTER VALID ORDER")
                else:
                    l1, l4, l5, d = [], [], [], 0
                    print()
                    print("ENTER ELEMENTS OF MATRIX")
                    print()
                    for i in range(1,e+1):
                        for j in range(1,e+1):
                            el = (i * 10)+ j
                            elm='a' + str(el)
                            ele=elm + ' : '
                            a=float(input(ele))
                            l1.append(a)
                    for i in range(0,len(l1),e):
                        for j in range(i,e+i):
                            l4.append(l1[j])
                        l5.append(l4)
                        l4 = []
                    m = op.deter(l5)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    print("determinant=",m)
                    print('\n'*3)
            
            elif a == 6:
                e = int(input("ENTER THE NO. OF ROWS: "))
                if e == 0:
                    print("ENTER A VALID ORDER")
                    
                else:
                    p, r = op.adj(e)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in r:
                        print(i)
                    print('\n'*3)
            
            elif a == 7:
                e = int(input("ENTER THE NO. OF ROWS: "))
                if e == 0:
                    print("ENTER VALID ORDER")
                else:
                    o = op.inverse(e)
                    if type(o) == list:
                        print()
                        print("RESULT")
                        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                        print()
                        for i in o:
                            print(i)
                        print('\n'*3)
        
            elif a == 8:
                e = int(input("ENTER THE NO. OF ROWS: "))
                f = int(input("ENTER THE NO. OF COLUMNS:"))
                if e == 0 or f == 0:
                    print("ENTER VALID ORDER")
                else:
                    n = op.trans(e,f)
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in n:
                        print(i)
                    print('\n' * 3)
        
            elif a == 9:
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                fl = op.history()
                print('\n'*3)
                
                if fl == False:
                    if input("DO YOU WANT TO CLEAR HISTORY?(y/n): ").lower()=='y':
                        op.clr()
                
            elif a == 0:
                break
            
            else:
                print()
                print()
                print("ENTER A VALID CHOICE!!!")
                print('\n'*3)
            input("~~~PRESS ENTER TO CONTINUE~~~")
        
        except:
            print('\n'*3)
            print("~~~SOME ERROR OCCURED!!!~~~")
            print()
            input("~~~PRESS ENTER TO RESTART~~~")

        print('\n'*3)
    print("APP DEVELOPED BY","ASWIN P","CLASS 12A 2k22-23 BATCH","KENDRIYA VIDYALAYA ADOOR","SHIFT 1","","THANK YOU",sep='\n')
