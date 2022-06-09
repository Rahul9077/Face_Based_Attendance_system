import datetime
import cv2
import csv
from Detecting_faces import SimpleFacerec
import pandas as pd


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("Users/")

# Load Camera
cap = cv2.VideoCapture(2)
df = pd.read_csv("Employee_details.csv")
Employee_id = list(df['ID'])

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, Id in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, Id,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        if Id in Employee_id:
            df1 = df[df['ID'] == Id]
            data = []
            data.append(df1['ID'])
            data.append(df1['name'])
            data.append(df1['designation'])
            time_chkin = datetime.datetime.now()
            data.append(time_chkin)
            data1 = [data]

            with open('Attendance.csv', 'a') as f:
                writer = csv.writer(f)
                # write multiple rows
                writer.writerows(data1)
                f.close()
            break


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()