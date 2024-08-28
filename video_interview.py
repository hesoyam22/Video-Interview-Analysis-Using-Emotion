import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
import cv2
import os
import tensorflow.keras
from tensorflow.keras.preprocessing.image import img_to_array
import imutils
from tensorflow.keras.models import load_model
import numpy as np
import time
import pandas as pd
import datetime
# the json module to work with json files 
import json
import tkinter
from PIL import Image,ImageTk
import matplotlib.pyplot as plt

#import random
import os

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Emotion_Recogniser")


#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1200x600')
#window.configure(background='light cyan4')
img=Image.open("bagg.webp")
img=img.resize((1200,600))
img= ImageTk.PhotoImage(img)
label= ttk.Label(window,image = img)
message = tk.Label(window, text="Video Interview"   ,bg="#b7e1dc",fg="black"  ,width=60  ,height=2,font=('gigi', 25, 'italic bold underline')) 
message.place(x=0, y=0)


lbl1 = tk.Label(window, text="Username",width=18  ,height=1  ,fg="Black"  ,bg="#b7e1dc" ,font=('Arial', 15, ' bold ') ) 
lbl1.place(x=550, y=200)
txt1 = tk.Entry(window,width=15  ,bg="#b7e1dc" ,fg="Black",font=('Arial', 15, ' bold '))
txt1.place(x=800, y=200)

lbl2= tk.Label(window, text=" Password",width=18  ,height=1  ,fg="Black"  ,bg="#b7e1dc" ,font=('Arial', 15, ' bold ') ) 
lbl2.place(x=550, y=300)
txt2 = tk.Entry(window,width=15  ,bg="#b7e1dc" ,fg="Black",font=('Arial', 15, ' bold '),show="*")
txt2.place(x=800, y=300)



def main():
    with open("UserDetails.csv","r") as file:
        file_reader=csv.reader(file)
        user_find(file_reader)
        file.close()
        
def user_find(file):
    global user
    user= txt1.get()
##    user = input ("enter user name")
    for row in file:
        if row[0] == user:
            print("user name found", user)
            user_found= [row[0], row[1]]
            pass_check(user_found)
            break
        else:
            print("not found")
            #unsuccess()

def pass_check(user_found):
   # global user
    user =txt2.get()
##    user=input("enter password")
    if user_found[1] == user:
        print("password matched")
        successful()
    else:
        print("invalid password")
        unsuccess()


def register():
    global window1
    window1 = tk.Toplevel()  
    window1.title("Register")
    # window1.geometry('1280x720')
    window1.configure(background ='blue')

    window1.geometry('1200x600')
#window.configure(background='light cyan4')
    img=Image.open("bagg.webp")
    img=img.resize((1200,600))
    img= ImageTk.PhotoImage(img)
    label= ttk.Label(window1,image = img)
##    img=Image.open("b")
    
    message = tk.Label(window1, text="Registration Form / Entry Form "  ,bg="#b7e1dc" ,fg="black"  ,width=60  ,height=2,font=('gigi', 25, 'italic bold underline')) 
    message.place(x=0, y=0)


      
    lbl = tk.Label(window1, text="Username",width=18  ,height=1  ,fg="Black"  ,bg="#b7e1dc" ,font=('Arial', 15, ' bold ') ) 
    lbl.place(x=370, y=150)

    txt = tk.Entry(window1,width=15  ,bg="#b7e1dc" ,fg="Black",font=('Arial', 15, ' bold '))
    txt.place(x=650, y=150)

    lbl2 = tk.Label(window1, text="  Password",width=18  ,fg="Black"  ,bg="#b7e1dc"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl2.place(x=370, y=200)

    txt2 = tk.Entry(window1,width=15  ,bg="#b7e1dc"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt2.place(x=650, y=200)

    lbl5 = tk.Label(window1, text="  Loction",width=18  ,fg="Black"  ,bg="#b7e1dc"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl5.place(x=370, y=250)

    txt5 = tk.Entry(window1,width=15  ,bg="#b7e1dc"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt5.place(x=650, y=250)

    lbl3 = tk.Label(window1, text=" E-mail",width=18  ,fg="Black"  ,bg="#b7e1dc"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl3.place(x=370, y=300)

    txt3 = tk.Entry(window1,width=15  ,bg="#b7e1dc"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt3.place(x=650, y=300)

    lbl4 = tk.Label(window1, text="  Phone",width=18  ,fg="Black"  ,bg="#b7e1dc"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl4.place(x=370, y=350)

    txt4 = tk.Entry(window1,width=15  ,bg="#b7e1dc"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt4.place(x=650, y=350)


    def TakeImages():
        global ID
        global username
        username=(txt.get())
        password =(txt2.get())
        ID=(txt3.get())
        phone=(txt4.get())
        location=(txt5.get())
##        print()
        row = [username, password, ID, phone, location ]
        with open('UserDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            
        csvFile.close()
        print("file Updated successfully")
        register1()
    
    takeImg = tk.Button(window1, text ="Submit",  
    command = TakeImages, fg ="white", bg ="#4f9e94",  
    width = 15, height = 2, activebackground = "Red",  
    font =('times', 10, ' bold ')) 
    takeImg.place(x = 550, y = 400)
    label.pack()
    window1.mainloop()
 
def  unsuccess():
        root=Tk()
        root.geometry('250x150')
        root.title("UnSuccess")
        #cv2.destroy()
        
        lbl=Label(root, text="Login UnSuccessfull")
        print("Login UnSuccessfull")   
        lbl.pack()

                       
        quitWindow = tk.Button(root, text ="OK",  
        command = root.destroy, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)

        root.mainloop()

def quiz():
    os.system("python quizstar.py")
    
def register1():
    root=Tk()
    root.geometry('250x150')
    root.title("Success")
    #cv2.destroy()
    
    lbl=Label(root, text="Registered Successfully")
    print("Registered Successful")   
    lbl.pack()
    def bb():
        root.destroy()
        cv2.destroyAllWindows()
        window1.destroy()
##            time.sleep(3)
        #feedback()
        
    quitWindow = tk.Button(root, text ="OK",  
    command = bb, fg ="white", bg ="blue",  
    width = 5, height = 1, activebackground = "Red",  
    font =('times', 15, ' bold ')) 
    quitWindow.place(x = 85, y = 50)
    time.sleep(1)

    root.mainloop()
    
def successful():
##        global cam
        root=Tk()
        root.geometry('250x150')
        root.title("Success")
        #cv2.destroy()
        
        lbl=Label(root, text="Logged In Successfully")
        print("Login Successful")   
        lbl.pack()
        def bb():
            root.destroy()
            #quiz()
            feedback()
            
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)

        root.mainloop()

def feedback():

    # parameters for loading data and images
    detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
    emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

    # hyper-parameters for bounding boxes shape
    # loading models
    face_detection = cv2.CascadeClassifier(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
     "neutral"]


    #feelings_faces = []
    #for index, emotion in enumerate(EMOTIONS):
       # feelings_faces.append(cv2.imread('emojis/' + emotion + '.png', -1))

    # starting video streaming
    cv2.namedWindow('your_face')
    global camera
    camera = cv2.VideoCapture(0)
    count=0
    while True:
        frame = camera.read()[1]
        #reading the frame
        frame = imutils.resize(frame,width=350)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        global date
        global timeStamp
        now = datetime.datetime.now()
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        
        canvas = np.zeros((250, 350, 3), dtype="uint8")
        frameClone = frame.copy()
        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
                        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            
            preds = emotion_classifier.predict(roi)[0]
            print(preds)
            emotion_probability = np.max(preds)
            label = EMOTIONS[preds.argmax()]
        else: continue

     
        for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                    # construct the label text
                    text = "{}: {:.2f}%".format(emotion, prob * 100)
                    global res
                    
                   
                    #if emotion==EMOTIONS[0]:
                     #   res="Stress"

                    if emotion =='happy':
                        emotion1="Happy User"
                        res="Stress"
                        #if cv2.waitKey(1) & 0xFF == ord('q'):
                        row = [user , emotion1]
                        row = [user,emotion1,date,timeStamp ]
                        if(os.path.exists('report.txt')):
                            os.remove('report.txt')    
                            with open('reviews.csv','a+') as csvFile:
                                 writer = csv.writer(csvFile)
                                 writer.writerow(row)
                                 csvFile.close()
                                 print("file updated for happy ")

                    #if emotion==EMOTIONS[1]:
                      #  res="Stress"
                    if  emotion =='sad' or  emotion =='scared'  :
                        emotion1="User under pressure"
                        #if cv2.waitKey(1) & 0xFF == ord('q'):
                        row = [user , emotion1]
                        row = [user,emotion1,date,timeStamp ]
                        if(os.path.exists('report.txt')):
                            with open('reviews.csv','a+') as csvFile:
                                 writer = csv.writer(csvFile)
                                 writer.writerow(row)
                                 csvFile.close()
                                 print("file updated")
                            time.sleep(0.5)

                    if emotion =='neutral'   :
                        emotion1="User is Calm"
                        #if cv2.waitKey(1) & 0xFF == ord('q'):
                        row = [user , emotion1]
                        row = [user,emotion1,date,timeStamp ]
                        if(os.path.exists('report.txt')):
                            with open('reviews.csv','a+') as csvFile:
                                 writer = csv.writer(csvFile)
                                 writer.writerow(row)
                                 csvFile.close()
                                 print("file updated")
                            time.sleep(0.5)
                    if emotion =='angry'  or emotion =='disgust'   :
                        emotion1="User is Uncomfortable"
                        #if cv2.waitKey(1) & 0xFF == ord('q'):
                        row = [user , emotion1]
                        row = [user,emotion1,date,timeStamp ]
                        if(os.path.exists('report.txt')):
                            with open('reviews.csv','a+') as csvFile:
                                 writer = csv.writer(csvFile)
                                 writer.writerow(row)
                                 csvFile.close()
                                 print("file updated")
                            time.sleep(0.5)

                               


                    if emotion==EMOTIONS[3]:
                        res="No Stress"
                    var=0
                    count=count+1
                    #time.sleep(5)
##                    if var==1:
##                        print(count)
##                        var=0
                    #if count>=6:
                     #   print("aa")
                      #  updated()
                        
                        
                    
                    w = int(prob * 300)
                    cv2.rectangle(canvas, (7, (i * 35) + 5),
                    (w, (i * 35) + 35), (0, 0, 255), -1)
                    cv2.putText(canvas, text, (10, (i * 35) + 23),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (255, 255, 255), 2)
                    cv2.putText(frameClone, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                  (0, 0, 255), 2)
                    #break
                    cv2.imshow('your_face', frameClone)
                    cv2.imshow("Probabilities", canvas)        



        cv2.imshow('your_face', frameClone)
        cv2.imshow("Probabilities", canvas)
        time.sleep(0.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            updated(preds)

            break
        

    camera.release()
    cv2.destroyAllWindows()
    



def updated(preds):
        root=Tk()
        root.geometry('450x350')
        root.title("Success")

        
        lbl=Label(root, text="Thanks for your feedback")
        print("Thanks for your feedback")   
        lbl.pack()
        def bb():
            camera.release()
            cv2.destroyAllWindows()
            root.destroy()
        def statuss():
            EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
                        "neutral"]
            plt.figure(figsize=(8, 8))
            plt.pie(preds, labels=EMOTIONS, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Emotion Distribution')
            plt.savefig('emotion_distribution_pie_chart.png')  # Save the plot
            plt.show()  # Show the plot
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)

        quitWindow = tk.Button(root, text ="Check Status",  
        command = statuss, fg ="white", bg ="blue",  
         height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 150)

        time.sleep(1)

        root.mainloop()
        


takeImg = tk.Button(window, text="Login", command=main  ,fg="Black"  ,bg="#4f9e94"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=500, y=450)

takeImg = tk.Button(window, text="Register", command=register  ,fg="Black"  ,bg="#4f9e94"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=700, y=450)

takeImg = tk.Button(window, text="Quit", command=window.destroy  ,fg="Black"  ,bg="#4f9e94"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=900, y=450)


label.pack()
window.mainloop()
