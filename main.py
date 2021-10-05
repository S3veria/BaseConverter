
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()
root.geometry('600x400')
root.title('Base Converter')
root.config(bg='#3F3F3F')

baseOptions=['Binary','Decimal','Octal','Hexadecimal','Other']

inputBase="Decimal"
outputBase="Binary"

def checkForOtherInput(value):
    global inputBase
    otherEntry.delete(0, END)
    if value=="Binary":
        inputBase=value
        otherEntry.config(state='normal')
        otherEntry.delete(0, END)
        otherEntry.insert(0,'2')
        otherEntry.config(state='disabled')
    if value=="Decimal":
        inputBase = value
        otherEntry.config(state='normal')
        otherEntry.delete(0, END)
        otherEntry.insert(0,'10')
        otherEntry.config(state='disabled')
    if value=="Octal":
        inputBase = value
        otherEntry.config(state='normal')
        otherEntry.delete(0, END)
        otherEntry.insert(0,'8')
        otherEntry.config(state='disabled')
    if value=='Hexadecimal':
        inputBase = value
        otherEntry.config(state='normal')
        otherEntry.delete(0, END)
        otherEntry.insert(0,'16')
        otherEntry.config(state='disabled')

    if value=="Other":
        inputBase = value
        otherEntry.config(state='normal')
        otherEntry.delete(0, END)
        otherEntry.insert(0,'Other')


def checkForOtherOutput(value):
    global outputBase
    otherOutput.delete(0, END)
    if value=="Binary":
        outputBase=value
        otherOutput.config(state='normal')
        otherOutput.delete(0, END)
        otherOutput.insert(0,'2')
        otherOutput.config(state='disabled')
    if value=="Decimal":
        outputBase = value
        otherOutput.config(state='normal')
        otherOutput.delete(0, END)
        otherOutput.insert(0,'10')
        otherOutput.config(state='disabled')
    if value=="Octal":
        outputBase = value
        otherOutput.config(state='normal')
        otherOutput.delete(0, END)
        otherOutput.insert(0,'8')
        otherOutput.config(state='disabled')
    if value=='Hexadecimal':
        outputBase = value
        otherOutput.config(state='normal')
        otherOutput.delete(0, END)
        otherOutput.insert(0,'16')
        otherOutput.config(state='disabled')

    if value=="Other":
        outputBase = value
        otherOutput.config(state='normal')
        otherOutput.delete(0, END)
        otherOutput.insert(0,'Other')


outPutString=''
#Function that converts from decimal to any base:
def wholeToBase(base, num):
    letterVals = {10:'A',
                  11:'B',
                  12:'C',
                  13:'D',
                  14:'E',
                  15:'F',
                  16:'G',
                  17:'H',
                  18:'I',
                  19:'J',
                  20:'K',
                  21:'L',
                  22:'M',
                  23:'N',
                  24:'O',
                  25:'P',
                  26:'Q',
                  27:'R',
                  28:'S',
                  29:'T',
                  30:'U',
                  31:'V',
                  32:'W',
                  33:'X',
                  34:'Y',
                  35:'Z'
                  }
    global outPutString
    if num>=(base-1):
        wholeToBase(base,num//base)
    outVar=num%base
    if outVar>=10:
        outPutString+=letterVals[outVar]
    else:
        outPutString+=str(outVar)


#Decimal part of the input to decimal in the base
def decimalToBase(base, num, numberOfDecimals=10):
    letterVals = {10:'A',
                  11:'B',
                  12:'C',
                  13:'D',
                  14:'E',
                  15:'F',
                  16:'G',
                  17:'H',
                  18:'I',
                  19:'J',
                  20:'K',
                  21:'L',
                  22:'M',
                  23:'N',
                  24:'O',
                  25:'P',
                  26:'Q',
                  27:'R',
                  28:'S',
                  29:'T',
                  30:'U',
                  31:'V',
                  32:'W',
                  33:'X',
                  34:'Y',
                  35:'Z'
                  }
    answer=''
    if num==0:
        return '0'
    #print("decimal convertion")
    for i in range(numberOfDecimals):
        current=base*num
        #print(current)
        if(current==0):
            break
        if current>=1:
            #print(current)
            val=str(current).split('.')
            if int(val[0])>=10:
                answer+=letterVals[int(val[0])]
            else:
                answer += val[0]

            num=int(val[1])
            while num>1:
                num=num/10.0
            #print(f"num: {num}")
        else:
            answer+="0"
            num=current
    return answer





#Function that converts things
def convertNumber():
    finalResult.config(text="")
    toConvert = userEntry.get()
    toConvert=toConvert.upper()
    #print(f"Converting {toConvert} from {inputBase} to {outputBase}")
    finalResult.config(text='Answer here')

    basesDict = {'Binary': 2,
                 'Decimal': 10,
                 'Hexadecimal': 16,
                 'Octal': 8}

    letterValsReversed = {'A':10,
                  'B':11,
                  'C':12,
                  'D':13,
                  'E':14,
                  'F':15,
                  'G':16,
                  'H':17,
                  'I':18,
                  'J':19,
                  'K':20,
                  'L':21,
                  'M':22,
                  'N':23,
                  'O':24,
                  'P':25,
                  'Q':26,
                  'R':27,
                  'S':28,
                  'T':29,
                  'U':30,
                  'V':31,
                  'W':32,
                  'X':33,
                  'Y':34,
                  'Z':35
                  }

    # First we convert the input to decimal
    inBaseNumber=10
    if inputBase != "Decimal":
        if inputBase in basesDict:
            inBaseNumber=basesDict[inputBase]
        else:
            try:
                inBaseNumber=int(otherEntry.get())
                # NEED TO VALIDATE IF THE BASE IS OVER 35+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if inBaseNumber>35:
                    messagebox.showerror("Invalid input base",f"The input base ({inBaseNumber}) is out of range, please select a base with a numerical value between 2 and 35")
            except:
                messagebox.showerror("Invalid input base",
                                     f"The input base ({inBaseNumber}) is invalid")
    #print(f"Base is {inputBase} which numerically is {inBaseNumber}")

    decimalValue=0
    isValidInput=True

    wholeToConvert = toConvert
    decimalToConvert=''
    if '.' in toConvert:
        if toConvert.count('.')>1:
            #print("Only one decimal is allowed")
            #REGRESAR OTRO ERROR ACA ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            messagebox.showerror("Invalid input ",
                             f"It appears that there are multiple decimal points (.) in the input, please use one or none")

        listedVals=toConvert.split('.')
        wholeToConvert=listedVals[0]
        decimalToConvert=listedVals[1]




    #print(f"Converting whole({wholeToConvert}) and decimal({decimalToConvert})")
    for i in range(len(wholeToConvert)):
        position=len(wholeToConvert)-i-1
        digit=wholeToConvert[position]
        currBaseConvert=inBaseNumber**i

        #Get the number we're trying to convert
        try:
            digit=int(digit)

        except:
            try:
                digit=letterValsReversed[digit]

            except:
                # REGRESAR UN ERROR++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #print("Invalid argument: Not in the baseDict")
                isValidInput=False
                messagebox.showerror("Invalid argument in input",
                                     f"It appears some character(s) in the input are not valid, please limit the input to numerical and alphabetical characters")
                break
        if digit>=inBaseNumber:
            messagebox.showerror("Whole value out of range",
                                 f"The whole value of the input is out of range of the base")
            isValidInput=False
            break

        decimalValue+=currBaseConvert*digit

    outBaseNumber=10
    if outputBase != "Decimal":
        if outputBase in basesDict:
            outBaseNumber=basesDict[outputBase]
        else:
            try:
                outBaseNumber=int(otherOutput.get())
                #NEED TO VALIDATE IF THE BASE IS OVER 35+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if outBaseNumber>35:
                    messagebox.showerror("Invalid input base",f"The input base ({outBaseNumber}) is out of range, please select a base with a numerical value between 2 and 35")

            except:
                #print("Base is not valid")
                messagebox.showerror("Invalid input base",
                                     f"The input base ({inBaseNumber}) is invalid")

    totalDecimalValue=0
    for j in range(len(decimalToConvert)):
        currentVal=decimalToConvert[j]
        decimalIntVal=0
        try:
            decimalIntVal=int(currentVal)

        except:
            try:
                decimalIntVal=letterValsReversed[currentVal]

            except:
                #print("Decimal Value is not valid")
                messagebox.showerror("Invalid decimal value",
                                     f"The decimal portion of the input appears to be invalid")
                isValidInput = False
                break
                # REGRESAR UN ERROR++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if decimalIntVal>=inBaseNumber:
            messagebox.showerror("Out of range decimal value",
                                 f"The decimal portion is out of range of the base")
            isValidInput = False
        totalDecimalValue+=decimalIntVal*(inBaseNumber**(-j-1))


    if isValidInput:
        global outPutString
        outPutString=''
        #print(f"Decimal value of input {decimalValue}")

        wholeToBase(outBaseNumber,decimalValue)
        #print(outBaseNumber,totalDecimalValue)
        decimalFinalVal=decimalToBase(outBaseNumber,totalDecimalValue)
        outPutString+="."+decimalFinalVal
        if outPutString[0]=='0':
            outPutString=outPutString[1:]
        finalResult.config(text=outPutString)
        #print(f"Output in {outputBase}: {outPutString}")

    else:
        finalResult.config(text='InvalidArguments')







userEntry=Entry(root,width=40,bg='#6E6E6E',fg='#000000',font=("Calibri",12), border=0)
userEntry.place(x=25,y=100)

fromText=Label(root,text="Input number and base:", bg='#3F3F3F',fg='#b3b5b3',border=0,font=("Calibri",20))
fromText.place(x=25,y=50)

devName=Label(root,text="Developed by Santiago Reyes", bg='#3F3F3F',fg='#b3b5b3',border=0,font=("Calibri",14))
devName.place(x=25,y=10)

inVar=StringVar()
inVar.set(baseOptions[1])
inBaseMenu=OptionMenu(root,inVar,*baseOptions, command=checkForOtherInput)
inBaseMenu.config(border=0,bg='#6E6E6E',fg='#040404', width=20)
inBaseMenu.place(x=400,y=95)

otherEntry=Entry(root,width=10,font=("Calibri",15), border=0)
otherEntry.config(bg='#6E6E6E',fg='#000000')
otherEntry.insert(0,"10")
otherEntry.place(x=400,y=125)
otherEntry.config(state='disabled')


toText=Label(root,text="Output Base:", bg='#3F3F3F',fg='#b3b5b3',border=0,font=("Calibri",20))
toText.place(x=25,y=200)

outVar=StringVar()
outVar.set(baseOptions[0])
outBaseMenu=OptionMenu(root,outVar,*baseOptions, command=checkForOtherOutput)
outBaseMenu.config(border=0,bg='#6E6E6E',fg='#040404', width=20)
outBaseMenu.place(x=220,y=205)

otherOutput=Entry(root,width=10,font=("Calibri",15), border=0)
otherOutput.config(bg='#6E6E6E',fg='#000000')
otherOutput.insert(0,"2")
otherOutput.place(x=220,y=240)
otherOutput.config(state='disabled')



convertBtn=Button(root,text='Convert!',bg='#E46A6B',fg='#000000', width=22, command=convertNumber)
convertBtn.place(x=400,y=205)

answerText=Label(root,text="ANSWER:", bg='#3F3F3F',fg='#b3b5b3',border=0,font=("Calibri",20))
answerText.place(x=20, y=320)
finalResult=Label(root,text="", bg='#3F3F3F',fg='#b3b5b3',border=0,font=("Calibri",20))
finalResult.place(x=150,y=320)

root.mainloop()
