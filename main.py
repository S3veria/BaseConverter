import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tk_font
from PIL import Image
from PIL import ImageTk


mainBack="#0F112A"
entryBack="#1C1E3E"


root=tk.Tk()
root.geometry('1069x592')
root.title('Base Converter')
root.config(bg=mainBack)
tk_font.families()
baseOptions=['Binary','Decimal','Octal','Hexadecimal']

inputBase="Decimal"
outputBase="Binary"

def checkForOtherInput(value):
    global inputBase

    if value=="Binary":
        inputBase=value

    if value=="Decimal":
        inputBase = value

    if value=="Octal":
        inputBase = value

    if value=='Hexadecimal':
        inputBase = value


    if value=="Other":
        inputBase = value



def checkForOtherOutput(value):
    global outputBase
    if value=="Binary":
        outputBase=value

    if value=="Decimal":
        outputBase = value

    if value=="Octal":
        outputBase = value

    if value=='Hexadecimal':
        outputBase = value


    if value=="Other":
        outputBase = value


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
    print("decimal convertion")
    for i in range(numberOfDecimals):
        current=base*num
        print(current)
        if(current==0):
            break
        if current>=1:
            print(current)
            val=str(current).split('.')
            if int(val[0])>=10:
                answer+=letterVals[int(val[0])]
            else:
                answer += val[0]

            num=int(val[1])
            while num>1:
                num=num/10.0
            print(f"num: {num}")
        else:
            answer+="0"
            num=current
    return answer





#Function that converts things
def convertNumber():
    finalResult.config(text="")
    toConvert = userEntry.get()
    toConvert=toConvert.upper()
    print(f"Converting {toConvert} from {inputBase} to {outputBase}")
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

    # First we convert the input to decimal  +++++++++++++++++++++++++++++++++++
    inBaseNumber=10
    if inputBase != "Decimal":
        if inputBase in basesDict:
            inBaseNumber=basesDict[inputBase]
        else:
            try:
                #inBaseNumber=int(otherEntry.get())
                print("I need to remove this shit")
                # NEED TO VALIDATE IF THE BASE IS OVER 35+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if inBaseNumber>35:
                    messagebox.showerror("Invalid input base",f"The input base ({inBaseNumber}) is out of range, please select a base with a numerical value between 2 and 35")
            except:
                messagebox.showerror("Invalid input base",
                                     f"The input base ({inBaseNumber}) is invalid")
    print(f"Base is {inputBase} which numerically is {inBaseNumber}")

    decimalValue=0
    isValidInput=True

    wholeToConvert = toConvert
    decimalToConvert=''
    if '.' in toConvert:
        if toConvert.count('.')>1:
            print("Only one decimal is allowed")
            #REGRESAR OTRO ERROR ACA ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            messagebox.showerror("Invalid input ",
                             f"It appears that there are multiple decimal points (.) in the input, please use one or none")

        listedVals=toConvert.split('.')
        wholeToConvert=listedVals[0]
        decimalToConvert=listedVals[1]




    print(f"Converting whole({wholeToConvert}) and decimal({decimalToConvert})")
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
                print("Invalid argument: Not in the baseDict")
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
                #outBaseNumber=int(otherOutput.get())
                print("This should also work no problem")
                #NEED TO VALIDATE IF THE BASE IS OVER 35+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if outBaseNumber>35:
                    messagebox.showerror("Invalid input base",f"The input base ({outBaseNumber}) is out of range, please select a base with a numerical value between 2 and 35")

            except:
                print("Base is not valid")
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
                print("Decimal Value is not valid")
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
        print(f"Decimal value of input {decimalValue}")

        wholeToBase(outBaseNumber,decimalValue)
        print(outBaseNumber,totalDecimalValue)
        decimalFinalVal=decimalToBase(outBaseNumber,totalDecimalValue)
        outPutString+="."+decimalFinalVal
        if outPutString[0]=='0':
            outPutString=outPutString[1:]
            if outPutString==".0":
                outPutString="0.0"
        finalResult.config(text=outPutString)
        print(f"Output in {outputBase}: {outPutString}")

    else:
        finalResult.config(text='InvalidArguments')



convertBtnPhoto=Image.open("convertButton.PNG")

convertBtnPhoto=ImageTk.PhotoImage(convertBtnPhoto)
convertBtn=Button(root,text='',bg=mainBack, image=convertBtnPhoto, command=convertNumber,border=0,activebackground=mainBack)
convertBtn.place(relx=0.5,rely=0.75, anchor=CENTER)



entryImage=Image.open("entryImage.PNG")
entryImage=entryImage.resize((405,43),Image.ANTIALIAS)
entryImage=ImageTk.PhotoImage(entryImage)
userEntryImage=Label(root,text='',bg=mainBack,image=entryImage)
userEntryImage.place(relx=0.25,rely=0.3,anchor=W)

baseImage=Image.open("baseImage.PNG")
baseImage=baseImage.resize((160,43),Image.ANTIALIAS)
baseImage=ImageTk.PhotoImage(baseImage)
inputBaseOM=Label(root,text='',bg=mainBack,image=baseImage)
inputBaseOM.place(relx=0.65,rely=0.3,anchor=W)

outputBaseOM=Label(root,text='',bg=mainBack,image=baseImage)
outputBaseOM.place(relx=0.65,rely=0.55,anchor=W)
outputEntryImage=Label(root,text='',bg=mainBack,image=entryImage)
outputEntryImage.place(relx=0.25,rely=0.55,anchor=W)




userEntry=Entry(root,width=30,bg=entryBack,fg='#ffffff',font=("Courier",14), border=0)
userEntry.place(relx=0.285,rely=0.3,anchor=W)

fromText=Label(root,text="Number for Conversion", bg=mainBack,fg='#A8AEFF',border=0,font=("Courier",30))
fromText.place(relx=0.52,rely=0.2, anchor=CENTER)


inVar=StringVar()
inVar.set(baseOptions[1])
inBaseMenu=OptionMenu(root,inVar,*baseOptions, command=checkForOtherInput)
inBaseMenu["highlightthickness"]=0
inBaseMenu["menu"].config(bg=entryBack, border=0,fg="#ffffff")
inBaseMenu.config(border=0,bg=entryBack,fg='#ffffff', width=10)
inBaseMenu.place(relx=0.68, rely=0.3,anchor=W)




toText=Label(root,text="Converted Number", bg=mainBack,fg='#ffffff',border=0,font=("Courier",30))
toText.place(relx=0.52,rely=0.45,anchor=CENTER)



outVar=StringVar()
outVar.set(baseOptions[0])
outBaseMenu=OptionMenu(root,outVar,*baseOptions, command=checkForOtherOutput) #Use checkforotheroutput function
outBaseMenu["highlightthickness"]=0
outBaseMenu["menu"].config(bg=entryBack, border=0,fg="#ffffff")
outBaseMenu.config(border=0,bg=entryBack,fg='#ffffff', width=10)
outBaseMenu.place(relx=0.68, rely=0.55,anchor=W)




finalResult=Label(root,text="", bg=entryBack,fg='#b3b5b3',border=0,font=("Courier",15))
finalResult.place(relx=0.275,rely=0.55,anchor=W)

root.mainloop()
