import pandas as pd 
import tkinter as tk
from tkinter import simpledialog,messagebox


df = pd.read_csv('Periodic Table of Elements.csv')
oneLetter= set()
twoLetter= set()
element_dict={}
number_dict={}


for i,row in df.iterrows():
    sym = row["Symbol"].lower()
    element_dict[sym] = row["Element"]
    number_dict[sym] = row["AtomicNumber"]

for sym in df['Symbol']:
    if len(sym)==1:
        oneLetter.add(sym.lower())
    else:
        twoLetter.add(sym.lower())



def dfs(word):
    word=word.lower()
    stack = [(word, [])]
    while stack:
        curr, path = stack.pop()
        if len(curr)==0:
            return path
        if curr[0] in oneLetter:
            stack.append((curr[1:],path+[curr[0]]))
        if len(curr)>=2 and curr[:2] in twoLetter:
            stack.append((curr[2:],path+[curr[0:2]]))
    return []
    

def toString(list):
    word=''
    for sym in list:
        word+=sym
    return word.capitalize()

def toSymbol(list):
    word=''
    for sym in list:
        word+=sym.capitalize() + " "
    return word

def toEl(list):
    elements=''
    for sym in list:
        elements+=element_dict[sym] + " "
    return elements

def toNum(list):
    nums=''
    for sym in list:
        nums+=str(number_dict[sym]) + " "
    return nums
    

def gui(prompt,type):
    if type==1:
        root = tk.Tk()
        root.withdraw()
        user_input = simpledialog.askstring("Periodic Table AI", prompt)
        return user_input
    if type==2:
        messagebox.showinfo("Periodic Table AI", prompt)
    if type==3:
        return messagebox.askyesno("Periodic Table AI",prompt)
        
 


def main():
    running=True
    while running:
        userWord=gui("Enter your word",1)
        finalList=dfs(userWord)
        if len(finalList)==0:
            gui("Your word is not able to be created with atomic symbols.",2)
            cont=gui("Do you want to enter another word?",3)
            if not cont:
                running=False
   
        else:
            finalWord=toString(finalList)
            finalSym=toSymbol(finalList)
            finalEl=toEl(finalList)
            finalNum=toNum(finalList)
            gui("Your word is able to be made! \n" + "Word: " + finalWord + "\nSymbols: " + finalSym + "\nElements: " + finalEl + "\nAtomic Numbers: " + finalNum, 2)
            cont=gui("Do you want to enter another word?",3)
            if not cont:
                running=False
           

main()
