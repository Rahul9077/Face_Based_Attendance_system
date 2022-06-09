import cv2
import os
import csv

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    Id = input("Enter your Employee id : ")
    dir_path = r'Users'
    res = os.listdir(dir_path)
    C_name = Id+'.jpg'
    if C_name in res:
        print("A user with same ID already exist.")
        continue
    else:
        print("Enter following details")
        Name = input("Enter full Name - ")
        Designation = input("Enter Designation - ")
        Contact = input("Enter Contact number - ")
        Place = input("Enter Place - ")
        data = []
        data.append(Id)
        data.append(Name)
        data.append(Designation)
        data.append(Contact)
        data.append(Place)
        data1 = []
        data1.append(data)
        with open('Employee_details.csv', 'a') as f:
            writer = csv.writer(f)
            # write multiple rows
            writer.writerows(data1)
            f.close()

        # os.makedirs(mypath)
        break

while True:
    retval,frame = cap.read()
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(frame1,1.3,5)

    for (x,y,h,w) in faces:
        img = cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.putText(frame, "Press c to take photo ", (10,40), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 0, 255))
    cv2.imshow('',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    # k = cv2.waitKey(0)
    # Check if user hits ‘c’ or ‘g’ key

    elif (k == ord('c')):
        cv2.imwrite('Users/'+C_name, frame)
        print("Image saved successfuly")
        break
        # cv2.destroyAllWindows()



cap.release()
cv2.destroyAllWindows()

