import pyttsx3
import keyboard
import csv
from datetime import datetime
from datetime import date

#list = [('1', '20R201', 'ABISHEKGURU  A M'), ('2', '20R202', 'ADVAITH RAJ  S'), ('3', '20R203', 'AHILESH R RAM'), ('5', '20R205', 'B AMRITA'), ('6', '20R206', 'ARIKARAN  R'), ('7', '20R207', 'ARUN KUMAR  D'), ('8', '20R208', 'B SOORYA'), ('9', '20R209', 'BARKAVI  M'), ('11', '20R211', 'D L SHRIVARSHINI'), ('12', '20R212', 'DINESH KUMAR  P'), ('15', '20R215', 'GOKUL  P V'), ('16', '20R216', 'GOKUL BALAJI  R'), ('17', '20R217', 'GOPINATH  S'), ('18', '20R218', 'HAREESPANDY  N'), ('19', '20R219', 'HARSHINI  S'), ('20', '20R220', 'IMMANUEL GEORGE WINSTON'), ('21', '20R221', 'K S SHREEYA CENDINI'), ('22', '20R222', 'KESHAV  S'), ('23', '20R223', 'KISHORRE  N'), ('24', '20R224', 'KRISHNA  R S'), ('25', '20R225', 'M DHARANE DHARAN'), ('26', '20R226', 'MADHUSRRI  R S'), ('27', '20R227', 'MANORANJANN  N'), ('28', '20R228', 'MOHAN  S'), ('29', '20R229', 'MOHANAVARSHA  T'), ('30', '20R230', 'OVIYA ARUNACHALAM'), ('31', '20R231', 'P GOKUL RAJA'), ('32', '20R232', 'P S SANJAY'), ('33', '20R233', 'PARAS JAIN'), ('34', '20R234', 'PRAHASHITHAA  H'), ('35', '20R235', 'PRANEESH  S'), ('36', '20R236', 'RAMKUMAR  A'), ('37', '20R237', 'RITHICK SACHIN  D'), ('38', '20R238', 'SANJANA RAGHAVAN'), ('39', '20R239', 'SAYED MOHAMMED AYAAN'), ('40', '20R240', 'SIBI RAJA  P'), ('41', '20R241', 'SRIDHAR  J'), ('42', '20R242', 'SRUTHIKA  M K'), ('43', '20R243', 'SUPREETHA  K J'), ('44', '20R244', 'SURAJ  S'), ('45', '20R245', 'UTTKARSH  S G'), ('46', '20R246', 'VISHNUMAYA  T'), ('47', '20R247', 'VISWA  S'), ('49', '20R249', 'SHAM SUNDER'), ('4 31', '21R431', 'AAKASH  R'), ('4 32', '21R432', 'ARUN  P K'), ('4 33', '21R433', 'ARUNGANESH  S'), ('4 34', '21R434', 'DHIANESHWAR  T M'), ('4 35', '21R435', 'DINESH KUMAR  S'), ('4 36', '21R436', 'KIRUTHICK  S M'), ('4 37', '21R437', 'KISHORE  S'), ('4 38', '21R438', 'MOHAMMED AATHIF  N'), ('4 39', '21R439', 'NABEEL AHMED  M'), ('4 40', '21R440', 'PAVANKUMAR  B'), ('4 41', '21R441', 'PRAGATHEESH  R J'), ('4 42', '21R442', 'RAGHUL  S'), ('4 43', '21R443', 'RUSHABH PARAS NAGDA'), ('4 44', '21R444', 'SNEHA MITHRA  H'), ('4 45', '21R445', 'SUBASH  D'), ('4 46', '21R446', 'VASANTH  D'), ('4 47', '21R447', 'VIMAL  V K'), ('4 48', '21R448', 'YESWANTH  S')]
list = [('1', '20R201', 'ABISHEKGURU  A M'), ('2', '20R202', 'ADVAITH RAJ  S'), ('3', '20R203', 'AHILESH R RAM'), ('5', '20R205', 'B AMRITA')]

engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')                       
engine.setProperty('rate', 200)   

engine.setProperty('volume', 1)

present = []*2
absent = []*2
count = 0

length = len(list)


print("\nPress 'k' for present and press 'l' for absent \n")

for i in range(length):
    print(list[i][0] + " " + list[i][1] + " " + list[i][2])
    engine.say(list[i][0])
    engine.runAndWait()

    while True:
        if keyboard.is_pressed('k'):
            engine.stop()
            present.append(list[i])
            break
        elif keyboard.is_pressed('l'):
            engine.stop()
            absent.append(list[i])
            count = count + 1
            break
        
dt = datetime.now()
now = datetime.now()
today = str(now.day)+"."+str(now.month)+"."+str(now.year)


with open('Attendance.txt', 'a') as f:
    f.write("\nDate and time: ")
    f.write("\n" + str(dt) + "\n")
    print("\nDate and time: ", dt)


    print("\nStudents Absent:")
    for i in range(count):
        num = i+1
        f.write("\n" + str(num) + " " + absent[i][1] + " " + absent[i][2])
        print(str(num) + " " + absent[i][1] + " " + absent[i][2])

    f.write("\n\nNo. of Absentees " + str(len(absent)) + "\n\n")
    print("\nNo. of Absentees " + str(len(absent)))

with open('Attendance.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['Date:', today,'','Time:', now.strftime("%H:%M:%S")])

    for i in range(count):
        num = i+1
        csvwriter.writerow([str(num), absent[i][1], absent[i][2]])

    csvwriter.writerow(["No. of Absentees ", str(len(absent))])
    csvwriter.writerow([])
    csvwriter.writerow([])
input()