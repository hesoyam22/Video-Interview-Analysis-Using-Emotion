import csv

label1=input('enter the name:\n')
label2=input('enter the name:\n')
label3=input('enter the name:\n')
label4=input('enter the name:\n')
label5=input('enter the name:\n')
row = ['Angry' ,'Happy', 'Neutral' , 'Sad', 'Surprise']

#while True:
    

if label1==row[0]:
    f=open('UserInfo.txt','a+')
    f.write("Angry" +'\t' +'\n')
    print("done")


if label2==row[1]:
    f=open('UserInfo.txt','a+')
    f.write("Happy"+'\t' +'\n')
    print("done")


if label3==row[2]:
    f=open('UserInfo.txt','a+')
    f.write("Neutral"+'\t' +'\n')
    print("done")


if label4==row[3]:
    f=open('UserInfo.txt','a+')
    f.write("Sad"+'\t' +'\n')
    print("done")


if label5==row[4]:
    f=open('UserInfo.txt','a+')
    f.write("Surprise"+'\t' +'\n')
    print("done")



    #break




    
##    with open('UserInfo.csv','a+') as csvfile:
##        writer = csv.writer(csvfile)
##        aa=["Angry"]
##        writer.writerow(aa)
##        #print(row[0])
##
##
##if label2==row[1]:
##    with open('UserInfo.csv','a+') as csvfile:
##        writer = csv.writer(csvfile)
##        aa=["Happy"]
##        writer.writerow(aa)
####        print(row[1])
##
##if label3==row[2]:
##    with open('UserInfo.csv','a+') as csvfile:
##        writer = csv.writer(csvfile)
##        aa=["Neutral"]
##        writer.writerow(aa)(row[2])
####        print(row[2])
##
##if label4==row[3]:
##    with open('UserInfo.csv','a+') as csvfile:
##        writer = csv.writer(csvfile)
##        aa=["Sad"]
##        writer.writerow(aa)
####        print(row[3])
##with open('UserInfo.csv','a+') as csvfile:
##    reader = csv.reader(csvfile)
##    lines= len(list(reader))
##    print(lines)
