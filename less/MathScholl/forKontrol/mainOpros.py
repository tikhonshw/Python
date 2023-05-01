from reportlab.lib.units import inch, cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# import matplotlib.pyplot as plt 
 
import random
from os import path as dirPath
 
path = dirPath.dirname('/home/user/MySoft/Python/less/MathScholl/forKontrol/main.py')
print(path)

def createPDF(path,nameFile):
    canvas = Canvas(path + '/' + nameFile + '.pdf')
    return canvas

def genPDF(path,canvas,x,y,primer):
    # canvas = Canvas(path + '/printLabel.pdf', pagesize=(5.8 * cm, 4 * cm))
    pdfmetrics.registerFont(TTFont('Arial', path + '/ArialCyr.ttf')) 
    canvas.setFont("Arial", 14)
    canvas.drawString(y * cm, x * cm, "{}".format(primer)) 

def savePDF(canvas):
    canvas.save()


def genHearderCard(path,canvas,x,y):
    canvas.line((y - 1) * cm, (x) * cm, (y + 17) * cm, (x) * cm)
    canvas.line((y + 9) * cm, (x) * cm, (y + 9.5) * cm, (x + 0.6) * cm)
    canvas.line((y + 9.5) * cm, (x + 0.6) * cm, (y + 17) * cm, (x + 0.6) * cm)
    genPDF(path,canvas,x + 0.15, y, 'ФИО ')
    genPDF(path,canvas,x + 0.15, y + 10, 'класс:')

def generatePer2XX(per1):
    per2 = random.randint(11,99) 
    while per1 == per2:
        per2 = random.randint(11,99)
    return per2

def generatePer1ХХ():
    # print (random.randint(11,99))
    chislo = random.randint(11,99)
    while chislo % 10 == 0:
        chislo = random.randint(11,99)
    return chislo


listDown = 2
maxRange = (91 * listDown) - listDown + 1

canvas = createPDF(path,'Деление без остатка хх хх (opros)')
xStart = 29.7
yStart = 2.5

x = 29.7-1.5
y = 3.24
lineGen = 1 
primerOnPage = 0

arrPer1 = []


genHearderCard(path,canvas,x,y)
x = x - 0.7

for i in range(1, maxRange):
    primerOnPage = primerOnPage + 1

    if lineGen >= 4:
        canvas.line((y - 1) * cm, (x + 0.3) * cm, (y + 17) * cm, (x + 0.3) * cm)
        x = x - 0.8
        genHearderCard(path,canvas,x,y)
        x = x - 0.8
        lineGen = 1        
        print(arrPer1)
        arrPer1.clear() 


    per1 = generatePer1ХХ()
    # arrPer1.append(per1)
    # проверка per1 на повтор в пределах одной карточки
    while per1 in arrPer1:
        per1 = generatePer1ХХ()
        print ('Значение: ', per1, ' уже есть в массиве: ', arrPer1)
    # arrPer1.append(per1)
    # if per1 in arrPer1:
        # print ('Значение: ', per1, ' уже есть в массиве: ', arrPer1)


    per2 = generatePer2XX(per1)  

    if per1 % per2 == 0: 
        # print(i, per1, ':', per2 , '=', str(per1 / per2))
        primer = "{} : {} =".format(per1,per2)
        genPDF(path,canvas,x,y,primer)
        arrPer1.append(per1)
    else:
        while per1 % per2 != 0:
            if per1 % per2 == 0: 
                # primer = "{} : {} =".format(per1,per2)
                genPDF(path,canvas,x,y,primer)
                arrPer1.append(per1)
            else:
                # per1 = random.randint(11,99)
                per1 = generatePer1ХХ()
                # проверка per1 на повтор в пределах одной карточки
                while per1 in arrPer1:
                    per1 = generatePer1ХХ()
                # arrPer1.append(per1)    
                   

                per2 = generatePer2XX(per1)  
                # print(i, '---===---', per1, ':', per2 , '=', str(per1 / per2))
                if per1 % per2 == 0: 
                    primer = "{} : {} =".format(per1,per2)
                    genPDF(path,canvas,x,y,primer)
                    arrPer1.append(per1)

    y = y + 3.5;
    if y > 19:
        x = x - 1
        y = 3.24
        lineGen = lineGen + 1
        

    if primerOnPage == 90 and maxRange - i > 90:
        canvas.showPage()
        x = 29.7-1.5
        y = 3.24
        primerOnPage = 0
        
        print(arrPer1)
        arrPer1.clear() 

        genHearderCard(path,canvas,x,y)
        x = x - 0.8
        lineGen = 1    
           

    # print(arrPer1)

savePDF(canvas)