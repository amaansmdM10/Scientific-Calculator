from tkinter import *
def calculate(s):
    l=[]
    i=0
    for j in range(len(s)):
        if s[j]==")":
            l.append(s[i:j])
            l.append(s[j])
            i=j+1
        elif s[j]=="(" and j==0:
            i=1
            l.append("(")
        elif s[j]=="(" and j!=0:
            l.append(s[i:j-1])
            l.append(s[j-1])
            l.append("(")
            i=j+1
        elif s[j] in ["+","-","/","x","^"]:
            if s[j+1]=="-":
                l.append(s[i:j])
                l.append(s[j])
                l.append(s[j+1:j+3])
                i=j+3
            else:
                l.append(s[i:j])
                l.append(s[j])
                i=j+1
    l.append(s[i:])
    while "" in l:
        l.remove("")       
    return l
def toPostfix(l):
    stack=[]
    str=""
    p={"+":3,"-":3,"x":2,"/":2,"^":1}
    for i in l:
        if i in p:
            while len(stack)!=0 and stack[-1]!="(" and p[stack[-1]]<=p[i]:
                str+=stack[-1]+" "
                stack.pop(-1)
            stack.append(i)
        elif i=="(":
            stack.append("(")
        elif i==")":
            while len(stack)!=0 and stack[-1]!="(":
                str+=stack[-1]+" "
                stack.pop(-1)
            if len(stack)!=0:
                stack.pop(-1)
        else:
            str+=i+" "
    while len(stack)!=0:
        str+=stack.pop(-1)
    return str
def solve(s):
    s=s.split()
    stack=[]
    for i in range(len(s)):
        if s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        elif s[i]=="x":
            a=stack.pop()
            b=stack.pop()
            stack.append(a*b)
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(b/a)
        elif s[i]=="^":
            a=stack.pop()
            b=stack.pop()
            stack.append(b**a)
        else:
            stack.append(float(s[i]))
        global ent
        ent.delete(0,END)
        ent.insert(0,str(stack[0]))
def setValue(a):
    global ent
    ent.insert(END,a)
def delete():
    global ent
    s=ent.get()
    ent.delete(0,END)
    ent.insert(0,s[:-1])
def compute(s):
    try:
        l=calculate(s)
        p=toPostfix(l)
        k=solve(p)
    except:
        global ent
        ent.delete(0,END)
        ent.insert(0,"Error")
def clear():
    global ent
    ent.delete(0,END)
calci=Tk()
calci.geometry("600x515")
calci.title("Calculator")
ent=Entry(calci,bd=20,width=70)
ent.grid(row=0,column=0,columnspan=3)
b1=Button(calci,text="1",height=5, width=20,command=lambda: setValue("1"))
b1.grid(row=1,column=0)
b2=Button(calci,text="2",height=5, width=20,command=lambda: setValue("2"))
b2.grid(row=1,column=1)
b3=Button(calci,text="3",height=5, width=20,command=lambda: setValue("3"))
b3.grid(row=1,column=2)
b4=Button(calci,text="4",height=5, width=20,command=lambda: setValue("4"))
b4.grid(row=2,column=0)
b5=Button(calci,text="5",height=5, width=20,command=lambda: setValue("5"))
b5.grid(row=2,column=1)
b6=Button(calci,text="6",height=5, width=20,command=lambda: setValue("6"))
b6.grid(row=2,column=2)
b7=Button(calci,text="7",height=5, width=20,command=lambda: setValue("7"))
b7.grid(row=3,column=0)
b8=Button(calci,text="8",height=5, width=20,command=lambda: setValue("8"))
b8.grid(row=3,column=1)
b9=Button(calci,text="9",height=5, width=20,command=lambda: setValue("9"))
b9.grid(row=3,column=2)
b0=Button(calci,text="0",height=5, width=20,command=lambda: setValue("0"))
b0.grid(row=4,column=0)
add=Button(calci,text="+",height=5, width=20,command=lambda: setValue("+"))
add.grid(row=1,column=3)
sub=Button(calci,text="-",height=5, width=20,command=lambda: setValue("-"))
sub.grid(row=4,column=3)
mul=Button(calci,text="x",height=5, width=20,command=lambda: setValue("x"))
mul.grid(row=3,column=3)
div=Button(calci,text="/",height=5, width=20,command=lambda: setValue("/"))
div.grid(row=2,column=3)
equal=Button(calci,text="=",height=5, width=20,command=lambda: compute(ent.get()))
equal.grid(row=4,column=2)
power=Button(calci,text="^",height=5, width=20,command=lambda: setValue("^"))
power.grid(row=5,column=2)
dot=Button(calci,text=".",height=5, width=20,command=lambda: setValue("."))
dot.grid(row=4,column=1)
bs=Button(calci,text="<-",height=5, width=20,command=lambda: delete())
bs.grid(row=5,column=3)
p1=Button(calci,text="(",height=5, width=20,command=lambda: setValue("("))
p1.grid(row=5,column=0)
p2=Button(calci,text=")",height=5, width=20,command=lambda: setValue(")"))
p2.grid(row=5,column=1)
clr=Button(calci, text="clear", height=5, width=20,command=lambda: clear())
clr.grid(row=0, column=3)
calci.mainloop()
