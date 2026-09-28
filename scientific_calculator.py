#import
from tkinter import *
import math
import random

#Setup
root = Tk()
root.title("Calculator")
root.resizable(False,False)

data = ""
numtext = StringVar(value=" ")

#สร้างหน้าจอ
Input = Entry(font=('arial',30,'bold'),fg="white",bg="grey",textvariable=numtext,justify="right",width=36,border=10)
Input.grid(columnspan=9)

#ฟังก์ชัน
def btn(number):
    global data
    data = data+str(number)
    numtext.set(data)

def clear():
    global data
    data = ""
    numtext.set(data)

def delete():
    global data
    global numtext
    a = ""
    lenght = len(data)-1
    for i in range(lenght):
        a += data[i]
    data = a
    numtext.set(data)

def result():
    try:
        global data
        cal = ("%.3f"%eval(data))
        numtext.set(cal)
    except:
        numtext.set("Error")
    data = ""
        
def func01_percent():
    global data
    global numtext
    try:
        percent = eval(data)/100
        numtext.set(percent)
    except:
        numtext.set("Error")
    data = ""

def func02_sin():
    global data
    global numtext
    try:
        sin = math.sin(math.radians(eval(data)))
        numtext.set(sin)
    except:
        numtext.set("Error")
    data = ""

def func03_cos():
    global data
    global numtext
    try:
        cos = "%.3f"%(math.cos(float(math.radians(eval(data)))))
        numtext.set(cos)
    except:
        numtext.set("Error")
    data = ""

def func04_tan():
    global data
    global numtext
    try:
        tan = math.tan(math.radians(eval(data)))
        numtext.set(tan)
    except:
        numtext.set("Error")
    data = ""

def func05_sinh():
    global data
    global numtext
    try:
        sinh = math.sinh(eval(data))
        numtext.set(sinh)
    except:
        numtext.set("Error")
    data = ""

def func06_cosh():
    global data
    global numtext
    try:
        cosh = math.cosh(eval(data))
        numtext.set(cosh)
    except:
        numtext.set("Error")
    data = ""

def func07_tanh():
    global data
    global numtext
    try:
        tanh = math.tanh(eval(data))
        numtext.set(tanh)
    except:
        numtext.set("Error")
    data = ""

def func08_radians():
    global data
    global numtext
    try:
        radian = math.radians(eval(data))
        numtext.set(radian)
    except:
        numtext.set("Error")
    data = ""

def func09_degrees():
    global data
    global numtext
    try:
        degree = math.degrees(eval(data))
        numtext.set(degree)
    except:
        numtext.set("Error")
    data = ""

def func10_arcsin():
    global data
    global numtext
    try:
        asin = math.asin(eval(data))
        numtext.set(asin)
    except:
        numtext.set("Error")
    data = ""

def func11_arccos():
    global data
    global numtext
    try:
        acos = math.acos(eval(data))
        numtext.set(acos)
    except:
        numtext.set("Error")
    data = ""

def func12_arctan():
    global data
    global numtext
    try:
        atan = math.atan(eval(data))
        numtext.set(atan)
    except:
        numtext.set("Error")
    data = ""

def func13_arcsinh():
    global data
    global numtext
    try:
        asinh = math.asinh(eval(data))
        numtext.set(asinh)
    except:
        numtext.set("Error")
    data = ""

def func14_arccosh():
    global data
    global numtext
    try:
        acosh = math.acosh(eval(data))
        numtext.set(acosh)
    except:
        numtext.set("Error")
    data = ""

def func15_arctanh():
    global data
    global numtext
    try:
        atanh = math.atanh(eval(data))
        numtext.set(atanh)
    except:
        numtext.set("Error")
    data = ""

def func16_1dx():
    global data
    global numtext
    try:
        x = 1/(float(eval(data)))
        numtext.set(x)
    except:
        numtext.set("Error")
    data = ""

def func17_exp():
    global data
    global numtext
    try:
        exp = math.exp(eval(data))
        numtext.set(exp)
    except:
        numtext.set("Error")
    data = ""

def func18_ln():
    global data
    global numtext
    try:
        ln = math.log(eval(data),2.71828182846)
        numtext.set(ln)
    except:
        numtext.set("Error")
    data = ""

def func19_log():
    global data
    global numtext
    try:
        log = math.log(eval(data),10)
        numtext.set(log)
    except:
        numtext.set("Error")
    data = ""

def func20_e():
    global data
    global numtext
    try:
        e = eval(data)*2.71828182846
        numtext.set(e)
    except:
        numtext.set("Error")
    data = ""

def func21_pi():
    global data
    global numtext
    try:
        pi = eval(data)*3.14159265359
        numtext.set(pi)
    except:
        numtext.set("Error")
    data = ""

def func22_squareroot():
    global data
    global numtext
    try:
        sqr = eval(data)**0.5
        numtext.set(sqr)
    except:
        numtext.set("Error")
    data = ""

def func23_squareroot3():
    global data
    global numtext
    try:
        sqr3 = eval(data)**(1/3)
        numtext.set(sqr3)
    except:
        numtext.set("Error")
    data = ""

def func24_square():
    global data
    global numtext
    try:
        sq2 = eval(data)**2
        numtext.set(sq2)
    except:
        numtext.set("Error")
    data = ""

def func25_square3():
    global data
    global numtext
    try:
        sq3 = eval(data)**3
        numtext.set(sq3)
    except:
        numtext.set("Error")
    data = ""

def func26_absolute():
    global data
    global numtext
    try:
        abl = str(abs(eval(data)))
        numtext.set("|"+abl+"|")
    except:
        numtext.set("Error")
    data = ""

def func27_factorial():
    global data
    global numtext
    try:
        fac = math.factorial(eval(data))
        numtext.set(fac)
    except:
        numtext.set("Error")
    data = ""

def func28_gamma():
    global data
    global numtext
    try:
        gm = math.factorial((eval(data))-1)
        numtext.set(gm)
    except:
        numtext.set("Error")
    data = ""

def func29_random():
    global data
    global numtext
    try:
        ran = random.randint(1,eval(data))
        numtext.set(ran)
    except:
        numtext.set("Error")

def func30_squarearea():
    rootsqa = Tk()
    rootsqa.title("SquareArea")
    rootsqa.resizable(False,False)
    
    Label(rootsqa,text="width =",font=30).grid(row=0,column=0)
    width = IntVar(rootsqa)
    widthsqa = Entry(rootsqa,width=30,textvariable=width,font=30)
    widthsqa.grid(row=0,column=1)
    
    Label(rootsqa,text="length =",font=30).grid(row=1,column=0)
    length = IntVar(rootsqa)
    lengthsqa = Entry(rootsqa,width=30,textvariable=length,font=30)
    lengthsqa.grid(row=1,column=1)
    
    Label(rootsqa,text="SquareArea =",font=30).grid(row=2,column=0)
    sqa = Entry(rootsqa,width=30,font=30)
    sqa.grid(row=2,column=1)
    
    def squarearea():
        sqa.delete(0,END)
        w = width.get()
        l = length.get()
        sqaarea = w*l
        sqa.insert(0,sqaarea)

    btn = Button(rootsqa,text="Calculate",command=squarearea).grid(row=3,column=1)

    rootsqa.mainloop()

def func31_trianglearea():
    roottaga = Tk()
    roottaga.title("TriangleArea")
    roottaga.resizable(False,False)
    
    Label(roottaga,text="width =",font=30).grid(row=0,column=0)
    width = IntVar(roottaga)
    widthtaga = Entry(roottaga,width=30,textvariable=width,font=30)
    widthtaga.grid(row=0,column=1)
    
    Label(roottaga,text="height =",font=30).grid(row=1,column=0)
    height = IntVar(roottaga)
    heighttaga = Entry(roottaga,width=30,textvariable=height,font=30)
    heighttaga.grid(row=1,column=1)
    
    Label(roottaga,text="TriangleArea =",font=30).grid(row=2,column=0)
    taga = Entry(roottaga,width=30,font=30)
    taga.grid(row=2,column=1)
    
    def trianglearea():
        taga.delete(0,END)
        w = width.get()
        h = height.get()
        tagarea = 1/2*w*h
        taga.insert(0,tagarea)
    
    btn = Button(roottaga,text="Calculate",command=trianglearea).grid(row=3,column=1)

    roottaga.mainloop()

def func32_circlearea():
    rootca = Tk()
    rootca.title("CircleArea")
    rootca.resizable(False,False)
    
    Label(rootca,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootca)
    radiusca = Entry(rootca,width=30,textvariable=radius,font=30)
    radiusca.grid(row=0,column=1)
    
    Label(rootca,text="CircleArea =",font=30).grid(row=1,column=0)
    ca = Entry(rootca,width=30,font=30)
    ca.grid(row=1,column=1)
    
    def circlearea():
        ca.delete(0,END)
        r = radius.get()
        carea = (22/7)*r**2
        ca.insert(0,carea)
    
    btn = Button(rootca,text="Calculate",command=circlearea).grid(row=2,column=1)

    rootca.mainloop()

def func33_circlecircumference():
    rootcc = Tk()
    rootcc.title("CircleCumference")
    rootcc.resizable(False,False)
    
    Label(rootcc,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootcc)
    radiuscc = Entry(rootcc,width=30,textvariable=radius,font=30)
    radiuscc.grid(row=0,column=1)
    
    Label(rootcc,text="CircleCumference =",font=30).grid(row=1,column=0)
    cc = Entry(rootcc,width=30,font=30)
    cc.grid(row=1,column=1)
    
    def circlecircumference():
        cc.delete(0,END)
        r = radius.get()
        cccfr = 2*(22/7)*r
        cc.insert(0,cccfr)
    
    btn = Button(rootcc,text="Calculate",command=circlecircumference).grid(row=2,column=1)

    rootcc.mainloop()

def func34_spherevolume():
    rootsv = Tk()
    rootsv.title("SphereVolume")
    rootsv.resizable(False,False)
    
    Label(rootsv,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootsv)
    radiussv = Entry(rootsv,width=30,textvariable=radius,font=30)
    radiussv.grid(row=0,column=1)
    
    Label(rootsv,text="SphereVolume =",font=30).grid(row=1,column=0)
    sv = Entry(rootsv,width=30,font=30)
    sv.grid(row=1,column=1)
    
    def spherevolume():
        sv.delete(0,END)
        r = radius.get()
        spv = (4/3)*(22/7)*r**3
        sv.insert(0,spv)
    
    btn = Button(rootsv,text="Calculate",command=spherevolume).grid(row=2,column=1)

    rootsv.mainloop()

def func35_spherecircumference():
    rootsc = Tk()
    rootsc.title("SphereCircumference")
    rootsc.resizable(False,False)
    
    Label(rootsc,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootsc)
    radiussc = Entry(rootsc,width=30,textvariable=radius,font=30)
    radiussc.grid(row=0,column=1)
    
    Label(rootsc,text="SphereCircumference =",font=30).grid(row=1,column=0)
    sc = Entry(rootsc,width=30,font=30)
    sc.grid(row=1,column=1)
    
    def spherecircumference():
        sc.delete(0,END)
        r = radius.get()
        spc = 4*(22/7)*r**2
        sc.insert(0,spc)
    
    btn = Button(rootsc,text="Calculate",command=spherecircumference).grid(row=2,column=1)

    rootsc.mainloop()

def func36_cylindricalvolume():
    rootcv = Tk()
    rootcv.title("CylindricalVolume")
    rootcv.resizable(False,False)
    
    Label(rootcv,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootcv)
    radiuscv = Entry(rootcv,width=30,textvariable=radius,font=30)
    radiuscv.grid(row=0,column=1)

    Label(rootcv,text="height =",font=30).grid(row=1,column=0)
    height = IntVar(rootcv)
    heightcv = Entry(rootcv,width=30,textvariable=height,font=30)
    heightcv.grid(row=1,column=1)
    
    Label(rootcv,text="CylindricalVolume =",font=30).grid(row=2,column=0)
    cv = Entry(rootcv,width=30,font=30)
    cv.grid(row=2,column=1)
    
    def cylindricalvolume():
        cv.delete(0,END)
        r = radius.get()
        h = height.get()
        clv = (22/7)*r**2*h
        cv.insert(0,clv)
    
    btn = Button(rootcv,text="Calculate",command=cylindricalvolume).grid(row=3,column=1)

    rootcv.mainloop()

def func37_conevolume():
    rootcov = Tk()
    rootcov.title("ConeVolume")
    rootcov.resizable(False,False)
    
    Label(rootcov,text="radius =",font=30).grid(row=0,column=0)
    radius = IntVar(rootcov)
    radiuscov = Entry(rootcov,width=30,textvariable=radius,font=30)
    radiuscov.grid(row=0,column=1)

    Label(rootcov,text="height =",font=30).grid(row=1,column=0)
    height = IntVar(rootcov)
    heightcov = Entry(rootcov,width=30,textvariable=height,font=30)
    heightcov.grid(row=1,column=1)
    
    Label(rootcov,text="ConeVolume =",font=30).grid(row=2,column=0)
    cov = Entry(rootcov,width=30,font=30)
    cov.grid(row=2,column=1)
    
    def conevolume():
        cov.delete(0,END)
        r = radius.get()
        h = height.get()
        covl = (1/3)*(22/7)*r**2*h
        cov.insert(0,covl)
    
    btn = Button(rootcov,text="Calculate",command=conevolume).grid(row=3,column=1)

    rootcov.mainloop()

def func38_pyramidvolume():
    rootpv = Tk()
    rootpv.title("PyramidVolume")
    rootpv.resizable(False,False)
    
    Label(rootpv,text="base =",font=30).grid(row=0,column=0)
    base = IntVar(rootpv)
    basepv = Entry(rootpv,width=30,textvariable=base,font=30)
    basepv.grid(row=0,column=1)

    Label(rootpv,text="height =",font=30).grid(row=1,column=0)
    height = IntVar(rootpv)
    heightpv = Entry(rootpv,width=30,textvariable=height,font=30)
    heightpv.grid(row=1,column=1)
    
    Label(rootpv,text="PyramidVolume =",font=30).grid(row=2,column=0)
    pv = Entry(rootpv,width=30,font=30)
    pv.grid(row=2,column=1)
    
    def pyramidvolume():
        pv.delete(0,END)
        b = base.get()
        h = height.get()
        prmv = (1/3)*b*h
        pv.insert(0,prmv)
    
    btn = Button(rootpv,text="Calculate",command=pyramidvolume).grid(row=3,column=1)

    rootpv.mainloop()

def func39_prismvolume():
    rootpsv = Tk()
    rootpsv.title("PrismVolume")
    rootpsv.resizable(False,False)
    
    Label(rootpsv,text="base =",font=30).grid(row=0,column=0)
    base = IntVar(rootpsv)
    basepsv = Entry(rootpsv,width=30,textvariable=base,font=30)
    basepsv.grid(row=0,column=1)

    Label(rootpsv,text="height =",font=30).grid(row=1,column=0)
    height = IntVar(rootpsv)
    heightpsv = Entry(rootpsv,width=30,textvariable=height,font=30)
    heightpsv.grid(row=1,column=1)
    
    Label(rootpsv,text="PrismVolume =",font=30).grid(row=2,column=0)
    psv = Entry(rootpsv,width=30,font=30)
    psv.grid(row=2,column=1)
    
    def prismvolume():
        psv.delete(0,END)
        b = base.get()
        h = height.get()
        psvl = b*h
        psv.insert(0,psvl)
    
    btn = Button(rootpsv,text="Calculate",command=prismvolume).grid(row=3,column=1)

    rootpsv.mainloop()

def func40_2pi():
    global data
    global numtext
    try:
        pi2 = eval(data)*3.14159265359*2
        numtext.set(pi2)
    except:
        numtext.set("Error")
    data = ""

def func41_2dx():
    global data
    global numtext
    try:
        x2 = 2/(float(eval(data)))
        numtext.set(x2)
    except:
        numtext.set("Error")
    data = ""

def func42_log2():
    global data
    global numtext
    try:
        log2 = math.log(eval(data),2)
        numtext.set(log2)
    except:
        numtext.set("Error")
    data = ""



#ปุ่มกด
def switch1():
    BtnRev = Button(root,text='🔄',font=('ariel',30,'bold'),fg='green',bg='black',width=3,height=1,border=5,command=switch2).grid(row=1,column=0)
    BF01 = Button(root,text='%',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func01_percent).grid(row=1,column=7)
    BF02 = Button(root,text='sin',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func02_sin).grid(row=4,column=1)
    BF03 = Button(root,text='cos',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func03_cos).grid(row=4,column=2)
    BF04 = Button(root,text='tan',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func04_tan).grid(row=4,column=3)
    BF05 = Button(root,text='sinh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func05_sinh).grid(row=5,column=1)
    BF06 = Button(root,text='cosh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func06_cosh).grid(row=5,column=2)
    BF07 = Button(root,text='tanh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func07_tanh).grid(row=5,column=3)
    BF16 = Button(root,text='1/x',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func16_1dx).grid(row=2,column=1)
    BF17 = Button(root,text='e\u02e3',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func17_exp).grid(row=5,column=0)
    BF18 = Button(root,text='ln',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func18_ln).grid(row=3,column=0)
    BF19 = Button(root,text='log',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func19_log).grid(row=2,column=0)
    BF20 = Button(root,text='e',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func20_e).grid(row=4,column=0)
    BF21 = Button(root,text='\u03c0',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func21_pi).grid(row=3,column=1)
    BF22 = Button(root,text='\u00b2\u221A',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func22_squareroot).grid(row=2,column=2)
    BF23 = Button(root,text='\u00b3\u221A',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func23_squareroot3).grid(row=2,column=3)
    BF24 = Button(root,text='x\u00b2',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func24_square).grid(row=3,column=2)
    BF25 = Button(root,text='x\u00b3',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func25_square3).grid(row=3,column=3)
    BF26 = Button(root,text='|x|',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func26_absolute).grid(row=2,column=4)
    BF27 = Button(root,text='x!',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func27_factorial).grid(row=3,column=4)
    BF28 = Button(root,text='Γ',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func28_gamma).grid(row=4,column=4)

def switch2():
    BtnReV2 = Button(root,text='🔄',font=('ariel',30,'bold'),fg='red',bg='black',width=3,height=1,border=5,command=switch1).grid(row=1,column=0)
    BF10 = Button(root,text='sin\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func10_arcsin).grid(row=4,column=1)
    BF11 = Button(root,text='cos\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func11_arccos).grid(row=4,column=2)
    BF12 = Button(root,text='tan\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func12_arctan).grid(row=4,column=3)
    BF13 = Button(root,text='sinh\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func13_arcsinh).grid(row=5,column=1)
    BF14 = Button(root,text='cosh\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func14_arccosh).grid(row=5,column=2)
    BF15 = Button(root,text='tanh\u207B\u00B9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func15_arctanh).grid(row=5,column=3)
    BF30 = Button(root,text='⬛',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func30_squarearea).grid(row=2,column=0)
    BF31 = Button(root,text='▲',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func31_trianglearea).grid(row=3,column=0)
    BF32 = Button(root,text='⬤',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func32_circlearea).grid(row=2,column=1)
    BF33 = Button(root,text='◯',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func33_circlecircumference).grid(row=3,column=1)
    BF34 = Button(root,text='🌐',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func34_spherevolume).grid(row=2,column=2)
    BF35 = Button(root,text='🔿',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func35_spherecircumference).grid(row=3,column=2)
    BF36 = Button(root,text='🛢',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func36_cylindricalvolume).grid(row=2,column=3)
    BF37 = Button(root,text='ꘜ',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func37_conevolume).grid(row=3,column=3)
    BF38 = Button(root,text='◭',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func38_pyramidvolume).grid(row=2,column=4)
    BF39 = Button(root,text='🌈⃤',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func39_prismvolume).grid(row=3,column=4)
    BF40 = Button(root,text='2\u03c0',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func40_2pi).grid(row=4,column=4)
    BF41 = Button(root,text='2/x',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func41_2dx).grid(row=5,column=0)
    BF42 = Button(root,text='log2',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func42_log2).grid(row=4,column=0)

Btn0 = Button(root,text='0',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(0)).grid(row=5,column=5)
Btn00 = Button(root,text='00',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("00")).grid(row=5,column=6)
Btn1 = Button(root,text='1',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(1)).grid(row=4,column=5)
Btn2 = Button(root,text='2',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(2)).grid(row=4,column=6)
Btn3 = Button(root,text='3',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(3)).grid(row=4,column=7)
Btn4 = Button(root,text='4',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(4)).grid(row=3,column=5)
Btn5 = Button(root,text='5',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(5)).grid(row=3,column=6)
Btn6 = Button(root,text='6',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(6)).grid(row=3,column=7)
Btn7 = Button(root,text='7',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(7)).grid(row=2,column=5)
Btn8 = Button(root,text='8',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(8)).grid(row=2,column=6)
Btn9 = Button(root,text='9',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(9)).grid(row=2,column=7)

BtnDot = Button(root,text='.',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(".")).grid(row=5,column=7)
BtnP = Button(root,text='+',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("+")).grid(row=4,column=8)
BtnM = Button(root,text='-',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("-")).grid(row=3,column=8)
BtnMul = Button(root,text='*',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("*")).grid(row=2,column=8)
Btnd = Button(root,text='/',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("/")).grid(row=1,column=8)
BtnOB = Button(root,text='(',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn("(")).grid(row=1,column=3)
BtnCB = Button(root,text=')',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=lambda:btn(")")).grid(row=1,column=4)

BtnRS = Button(root,text='=',font=('ariel',30,'bold'),fg='white',bg='red',width=3,height=1,border=5,command=result).grid(row=5,column=8)
BtnC = Button(root,text='C',font=('ariel',30,'bold'),fg='red',bg='black',width=3,height=1,border=5,command=clear).grid(row=1,column=5)
BtnDel = Button(root,text='Del',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=delete).grid(row=1,column=6)
BtnRev = Button(root,text='🔄',font=('ariel',30,'bold'),fg='green',bg='black',width=3,height=1,border=5,command=switch2).grid(row=1,column=0)

BF01 = Button(root,text='%',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func01_percent).grid(row=1,column=7)
BF02 = Button(root,text='sin',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func02_sin).grid(row=4,column=1)
BF03 = Button(root,text='cos',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func03_cos).grid(row=4,column=2)
BF04 = Button(root,text='tan',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func04_tan).grid(row=4,column=3)
BF05 = Button(root,text='sinh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func05_sinh).grid(row=5,column=1)
BF06 = Button(root,text='cosh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func06_cosh).grid(row=5,column=2)
BF07 = Button(root,text='tanh',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func07_tanh).grid(row=5,column=3)
BF08 = Button(root,text='rad',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func08_radians).grid(row=1,column=1)
BF09 = Button(root,text='deg',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func09_degrees).grid(row=1,column=2)
BF16 = Button(root,text='1/x',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func16_1dx).grid(row=2,column=1)
BF17 = Button(root,text='e\u02e3',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func17_exp).grid(row=5,column=0)
BF18 = Button(root,text='ln',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func18_ln).grid(row=3,column=0)
BF19 = Button(root,text='log',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func19_log).grid(row=2,column=0)
BF20 = Button(root,text='e',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func20_e).grid(row=4,column=0)
BF21 = Button(root,text='\u03c0',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func21_pi).grid(row=3,column=1)
BF22 = Button(root,text='\u00b2\u221A',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func22_squareroot).grid(row=2,column=2)
BF23 = Button(root,text='\u00b3\u221A',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func23_squareroot3).grid(row=2,column=3)
BF24 = Button(root,text='x\u00b2',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func24_square).grid(row=3,column=2)
BF25 = Button(root,text='x\u00b3',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func25_square3).grid(row=3,column=3)
BF26 = Button(root,text='|x|',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func26_absolute).grid(row=2,column=4)
BF27 = Button(root,text='x!',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func27_factorial).grid(row=3,column=4)
BF28 = Button(root,text='Γ',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func28_gamma).grid(row=4,column=4)
BF29 = Button(root,text='rand',font=('ariel',30,'bold'),fg='white',bg='black',width=3,height=1,border=5,command=func29_random).grid(row=5,column=4)

root.mainloop()