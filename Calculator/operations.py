import pickle
import numpy as np

def add(m,n):
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = [], [], [], [], [], [], [], [], []
    print('',"ENTER ELEMENTS OF FIRST MATRIX",'',sep='\n')
    for i in range(1, m+1):
        for j in range(1, n+1):
            ele = 'a'+str((i*10)+j)+' : '
            a = float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, n+1):
            el = (i*10)+j
            elm = 'a'+str(el)
            ele = elm+' : '
            a = float(input(ele))
            l2.append(a)
    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4 = []
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l6.append(l2[j])
        l7.append(l6)
        l6 = []
    for i in range(0,len(l1),n):
        for j in range(i, n+i):
            l8.append(l3[j])
        l9.append(l8)
        l8 = []
    lis = [l5, '+', l7, '=', l9]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l9


def sub(m,n):
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = [], [], [], [], [], [], [], [], []
    print()
    print("ENTER ELEMENTS OF FIRST MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, n+1):
            el = (i*10)+j
            elm = 'a'+str(el)
            ele = elm + ' : '
            a = float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, n+1):
            el = (i*10) + j
            elm = 'a'+str(el)
            ele = elm+' : '
            a = float(input(ele))
            l2.append(a)
    for i in range(len(l1)):
        l3.append(l1[i] - l2[i])
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4 = []
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l6.append(l2[j])
        l7.append(l6)
        l6 = []
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l8.append(l3[j])
        l9.append(l8)
        l8 = []
    lis = [l5, '-', l7, '=', l9]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l9


def smul(m,n):
    l1, l2, l3, l4, l5 = [], [], [], [], []
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, n+1):
            el = (i*10)+j
            elm = 'a'+str(el)
            ele = elm + ' : '
            a = float(input(ele))
            l1.append(a)
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4 = []
    b = float(input("ENTER THE SCALAR VALUE: "))
    for i in range(len(l1)):
        l1[i] *= b
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l2.append(l1[j])
        l3.append(l2)
        l2 = []
    lis=[l5, '×', [b], '=', l3]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis, f)
    return l3

def mul(n1, m1, n2, m2):
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = [], [], [], [], [], [], [], [], []
    print()
    print("ENTER ELEMENTS OF FIRST MATRIX")
    print()
    for i in range(1, n1+1):
        for j in range(1, m1+1):
            el = (i*10)+j
            elm = 'a'+str(el)
            ele = elm + ' : '
            a = float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1, n2+1):
        for j in range(1, m2+1):
            el = (i*10) + j
            elm = 'a' + str(el)
            ele = elm + ' : '
            a = float(input(ele))
            l2.append(a)
    for i in range(0, len(l1), m1):
        for j in range(i, m1+i):
            l3.append(l1[j])
        l5.append(l3)
        l3 = []
    for i in range(0, len(l2), m2):
        for j in range(i, m2+i):
            l4.append(l2[j])
        l6.append(l4)
        l4 = []
    for i in range(n1):
        for j in range(m2):
            l7.append(0)
    for i in range(0, len(l7), m2):
        for j in range(i, m2+i):
            l8.append(l7[j])
        l9.append(l8)
        l8 = []
    for i in range(len(l5)):
        for j in range(len(l6[0])):
            for k in range(len(l6)):
                l9[i][j] +=( l5[i][k] * l6[k][j])
    lis = [l5, '×', l6, '=', l9]
    with open ("history.dat", 'ab') as f:
            pickle.dump(lis, f)
    return l9

def deter(l5):
    
    mat = np.array(l5) 
    n = round(np.linalg.det(mat))
        
    lis = ["DETERMINANT OF",l5,"=",[n]]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis, f)
    return n

def adj(m):
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = [], [], [], [], [], [], [], [], []
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, m+1):
            el = (i * 10)+ j
            elm = 'a' + str(el)
            ele = elm+' : '
            a = float(input(ele))
            l1.append(a)
    print()
    for i in range(0, len(l1), m):
        for j in range(i, m+i):
            l2.append(l1[j])
        l3.append(l2)
        l2 = []
    
    for i in range(m):
        for j in range(m):
            for k in range(m):
                for l in range(m):
                    if k != i and l != j:
                        l4.append(l3[k][l])
                if l4 != []:
                    l5.append(l4)
                    l4 = []            
            d=deter(l5)
            l5 = []
            l6.append(d)
        l7.append(l6)
        l6 = []
    for i in range(len(l7)):
        for j in range(len(l7[i])):
            if (i+j)%2 != 0:
                l7[i][j] *= -1
    for i in range(len(l7)):
        for j in range(len(l7[i])):
            l8.append(round(l7[j][i]))
        l9.append(l8)
        l8 = []
    
    lis=["ADJOINT OF", l3, "=", l9]
    with open ("history.dat", 'ab') as f:
        pickle.dump(lis, f)
    return l3, l9

def inverse(m):
    ad, aj = adj(m)
    d = deter(ad)
    if d == 0:
        print("INVERSE DOESNOT EXISTS")
    else:
        for i in range(len(aj)):
            for j in range(len(aj[i])):
                aj[i][j] /= d
        lis=["INVERSE OF", ad, "=", aj]
        with open ("history.dat", 'ab') as f:
            pickle.dump(lis, f)
        return aj

def trans(m,n):
    l1, l2, l3, l4, l5, l6 =[], [], [], [], [], []
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1, m+1):
        for j in range(1, n+1):
            el = (i*10)+ j
            elm = 'a' + str(el)
            ele = elm + ' : '
            a = float(input(ele))
            l1.append(a)
    for i in range(0, len(l1), n):
        for j in range(i, n+i):
            l2.append(l1[j])
        l3.append(l2)
        l2 = []
    
    for i in range(len(l3[0])):
        for j in range(len(l3)):
            l4.append(l3[j][i])
    
    for i in range(0,len(l4),m):
        for j in range(i,m+i):
            l5.append(l4[j])
        l6.append(l5)
        l5 = []
    
    lis=["TRANSPOSE OF", l3, "=", l6]
    with open ("history.dat", 'ab') as f:
        pickle.dump(lis, f)
    return l6

def history():
    with open('history.dat','rb') as f:
        fl = True
        no = 1
        
        while True:
            try:
                a = pickle.load(f)
                print('\t' + str(no) + ',', '', sep='\n')
                no += 1
                fl = False
                if a[1] == '+' or a[1] == '-' or a[1] == '×':
                    for i in a:
                        for j in i:
                            print('\t', j)
                    print('\t ===========================', '', '', sep='\n')
                    
                elif a[0] == "DETERMINANT OF":
                    print('\t', a[0])
                    print()
                    for i in a[1]:
                        print('\t', i)
                    print()
                    print('\t', a[2], a[3])
                    print('\t ===========================', '', '', sep='\n')
                    
                elif a[0] == "INVERSE OF" or a[0] == "TRANSPOSE OF" or a[0] == "ADJOINT OF":
                    print('\t', a[0])
                    print()
                    for i in a[1]:
                        print('\t', i)
                    print('\t', a[2])
                    for i in a[3]:
                        print('\t', i)
                    print('\t ===========================', '', '', sep='\n')
            except EOFError:
                print()
                print()
                if fl == False:
                    print("NO FURTHER DATA AVAILABLE!!!")
                else:
                    print("NO HISTORY AVAILABLE")
                print()
                print()
                return fl
                break               

def clr():
    f = open('history.dat','wb')
    f.close()
    print("HISTORY SUCCESSFULLY CLEARED!!!")