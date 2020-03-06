


# student name = mostafa nasser ali      student code = 1404-3-130   course_name = Networks and information security

from tkinter import *   #for making GUI
from tkinter import messagebox
dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
DIC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Frequency_Of_X = [7.487792, 1.295442, 3.544945, 3.621812, 13.99891, 2.183939, 1.73856, 4.225448, 6.653554, 0.269036, 0.465726, 3.569814, 3.39121, 6.741725, 7.372491, 2.428106,
         0.262254, 6.140351, 6.945198, 9.852595, 3.004612, 1.157533, 1.691083, 0.278079, 1.643606, 0.036173 ] #Frequency of every letter in trained text

#applying function to find the max correlation between Frequency_of_X and Frequency_of_Y (example) for every key.

def Correlation(Frequency_Of_X,Frequency_Of_Y):
    def SumXY(Frequency_Of_X,Frequency_Of_Y):
        SumXY = []
        for i in range (1,26):
            SumXY.append(Frequency_Of_X[i]*Frequency_Of_Y[i])
        return sum(SumXY)

    def SumSquare(F):
        SumSquare = []
        for i in F:
            SumSquare.append(i**2)
        return sum(SumSquare)

    r = float((26*SumXY(Frequency_Of_X,Frequency_Of_Y)) - 10000)/((((26*SumSquare(Frequency_Of_X))- 10000)**0.5)*(((26*SumSquare(Frequency_Of_Y))- 10000)**0.5))

    return r



def Encrypt(DIC,dic):
    TEXT = e1.get("1.0","end-1c")
    key = int(v.get())
    Text = []
    for i in TEXT:
        for j in range (0,26): # loop for transforming uppercase to lowercase
            if i == DIC[j]:
                i = dic[j]
            else:
                continue
        Text.append(i)
    text = ''.join(Text) #to transform list to string


    cipher = []
    for i in text:
        for j in range (0,26):
            if i == dic[j]:
                i = dic[((j+key)%26)] #to add key over the letter index .... and we used modulus to continue conting after 26
                break
            else:
                continue
        cipher.append(i)
    Cipher = ''.join(cipher) #to transform list to string
    return Cipher


def Decrypt(dic):
    ciphers = e2.get("1.0","end-1c")
    freq = []
    for i in range(0,26):
        x = 0
        for j in ciphers:
            if dic[i] == j:
                x += 1
            else:
                continue
        freq.append(x)
#i can make a variable that carry sum(freq) and use it directly to reduce the processing time


    Frequency_Of_Y = []
    for i in freq: #this loop calculate the frequency of each letter in the decrypt text
        x = (float(i)/sum(freq))*100
        Frequency_Of_Y.append(x)
    FREQY = []    #mother list that contains 26 list
    for i in range(0,26):
        FreqYY = []    #list in list
        for j in range(0,26):
            FreqYY.append(Frequency_Of_Y[(i+j)%26])   #making a shifted list of the previus list
        FREQY.append(FreqYY)
    Final = []
    for i in FREQY:
        Final.append(Correlation(Frequency_Of_X,i))   #calculating corr 26 times ..

    l = 0
    for i in Final:
        if i > l:
            l = i  #replace the initial value of l with i to reach a final value which is the max .. and it's equal to l
        else:
            continue
    key =  Final.index(l)
    cipher = []
    for i in ciphers:
        for j in range (0,26):
            if i == dic[j]:
                i = dic[((j-key)%26)] #decipher every letter to the original form by subtracting it's index from the key
                break
            else:
                continue
        cipher.append(i)
    Cipher = ''.join(cipher) #again ... list to string
    v.set((key - 26)%26)
    return Cipher




r=Tk()
r.geometry("900x500") #Size of GUI Window
r.title('Ceasar Cipher Enc/Dec') #Title of GUI
r.configure(background='#367bbb') #Background color

e1=Text(r,height=15,width=50)
e1.place(x=20,y=20)
e2=Text(r,height=15,width=50)
e2.place(x=500,y=20)
v=StringVar()
v.set('0')
e=Entry(r,textvariable=v,width=5)
e.place(x=450,y=400)


def p1():
    e2.delete("1.0","end-1c")
    e2.insert(INSERT,Encrypt(DIC,dic))
    messagebox.showinfo("Good Job", "Successfully Encrypted")
def p2():
    e1.delete("1.0","end-1c")
    e1.insert(INSERT,Decrypt(dic))
    messagebox.showinfo("Note", "Successfully Decrypted")




b1=Button(r,text='Encrypt',command=p1).place(x=200,y=400)

b2=Button(r,text='Decrypt',command=p2).place(x=650,y=400)
r.mainloop()


# In[ ]:
