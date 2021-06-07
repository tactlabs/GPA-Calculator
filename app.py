import os
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sample.html");   

@app.route("/deptsem",methods=["POST","GET"])
def deptsem():
    dept = request.values.get("dept")
    sem  = request.values.get("sem")
    print(dept)
    print(sem)
    
    if str(dept)=='cse':
        if str(sem)=='1':
            nsize=8
            sub=['1 Communicative English - HS8151','2 Mathematics I - MA8151','3 Engineering Physics - PH8151','4 Engineering Chemistry - CY8151','5 Prob Solving & Python programming - GE8151','6 Engineering Graphics - GE8152','7 Problem Solving& Python Programming Lab - GE8161','8 Physics & Chemistry Lab - BS8161']
            cre=[4,4,3,3,3,4,2,2]

        if str(sem)=='2':
            nsize=8
            sub=['1 Technical English - HS8251','2 Mathematics II - MA8251','3 Physics for Information Science - PH8252','4 Basic Electrical & Measurement Engi - BE8255','5 Environmental Science & Engineering - GE8291','6 Programming in C - CS8251','7 C Programming lab - CS8261','8 Engineering Practices Lab - GE8261']
            cre=[4,4,3,3,3,3,2,2]
        if str(sem)=='3':
            nsize=9
            sub=['1 Discrete Mathematics - MA8351','2 Digital Principles and System Design - CS8351','3 Data Structures - CS8391','4 Object Oriented Programming - CS8392','5 Communication Engineering - EC8395','6 Data Structures  Lab - CS8381','7 Object Oriented programming Lab - CS8383','8 Digital Systems Lab - CS8382','9 Interpersonal Skills Listening and Speaking - HS8381']
            cre=[4,4,3,3,3,2,2,2,1]
        if str(sem)=='4':
            nsize=9
            sub=['1 Probability & Queueing Theory - MA8402','2 Computer Architecture - CS8491','3 Database Management Systems - CS8492','4 Design and Analysis of Algorithms - CS8451','5 Operating Systems - CS8493','6 Software Engineering - CS8494','7 Operating Systems Lab - CS8461','8 Database Management Systems Lab - CS8481','9 Advanced Reading & Writing - HS8461']
            cre=[4,3,3,3,3,3,2,2,1]
        if str(sem)=='5':
            nsize=9
            sub=['1 Algebra & Number theory - MA8551','2 Computer Networks - CS8591','3 Microprocessors and Microcontrollers - EC8691','4 Theory of Computation - CS8501','5 Object Oriented Analysis & Design - CS8592','6 Open Elective I -','7 Microprocessors and Microcontrollers Lab - EC8681','8 Object Oriented Analysis & Design Lab - CS8582','9 Networks Lab - CS8581']
            cre=[4,3,3,3,3,3,2,2,2]
        if str(sem)=='6':
            nsize=10
            sub=['1 Internet Programming - CS8651','2 Artificial Intelligence - CS8691','3 Mobile Computing - CS8601','4 Compiler Design - CS8602','5 Distributed Systems - CS8603','6 Professional Elective I -','7 Internet Programming Lab - CS8661','8 Mobile Application Development Lab - CS8662','9 Mini Project - CS8611','10 Professional Communication - HS8581']
            cre=[3,3,3,4,3,3,2,2,1,1]
        if str(sem)=='7':
            nsize=8
            sub=['1 Principles of Management - MG8591','2 Cryptography & Network Security - CS8792','3 Cloud Computing - CS8791','4 Open Elective II -','5 Professional Elective II -','6 Professional Elective III -','7 Cloud Computing Lab - CS8711','8 Security Lab - IT8761']
            cre=[3,3,3,3,3,3,2,2]
        if str(sem)=='8':
            nsize=3
            sub=['1 Professional Elective IV - CS6801','2 Professional Elective V -','3 Project Work - CS8811']
            cre=[3,3,10]
    if str(dept)=='ece':
        if str(sem)=='1':
            nsize=8
            sub=['1 Communicative English - HS8151','2 Mathematics I - MA8151','3 Engineering Physics - PH8151','4 Engineering Chemistry - CY8151','5 Prob Solving & Python programming - GE8151','6 Engineering Graphics - GE8152','7 Problem Solving& Python Programming Lab - GE8161','8 Physics & Chemistry Lab - BS8161']
            cre=[4,4,3,3,3,4,2,2]
        if str(sem)=='2':
            nsize=8
            sub=['1 Technical English - HS8251','2 Mathematics II - MA8251','3 Physics for Electronics Engineering - PH8253','4 Basic Electrical & Instrumentation Engi - BE8254','5 Circuit Analysis - EC8251','6 Electronic Devices - EC8252','7 Circuits & Devices Lab - EC8261','8 Engineering Practices Lab - GE8261']
            cre=[4,4,3,3,4,3,2,1]
        if str(sem)=='3':
            nsize=8
            sub=['1 Linear Algebra & Partial Differential Equa - MA8352','2 Fundamentals of Data Structures In C - EC8393','3 Electronic Circuits- I - EC8351','4 Signals and Systems - EC8352','5 Digital Electronics - EC8392','6 Control Systems Engineering - EC8391','7 Fundamentals of Data Structures In C Lab - EC8381','8 Analog and Digital Circuits Lab - EC8361','9 Interpersonal SkillsListening &Speaking - HS8381',]
            cre=[4,3,3,4,3,3,2,2,1]
        if str(sem)=='4':
            nsize=8
            sub=['1 Probability & Random Processes - MA8451','2 Electronic Circuits II - EC8452','3 Communication Theory - EC8491','4 Electromagnetic Fields - EC8451','5 Linear Integrated Circuits - EC8453','6 Environmental Science & Engineering - GE8291','7 circuits design & simulation lab - EC8461','8 Linear Integrated Circuit Lab - EC8462']
            cre=[4,3,3,4,3,3,2,2]
        if str(sem)=='5':
            nsize=9
            sub=['1 Digital Communication - EC8501','2 Discrete-Time Signal Processing - EC8553','3 Computer Architecture & Organization - EC8552','4 Communication Networks - EC8551','5 Professional Elective I -','6 Open Elective I -','7 Digital Signal Processing lab - EC8562','8 Communication System Lab - EC8561','9 Communication Networks Lab - EC8563']
            cre=[3,4,3,3,3,3,2,2,2]
        if str(sem)=='6':
            nsize=10
            sub=['1 Microprocessors and Microcontrollers - EC8691','2 VLSI Design - EC8095','3 Wireless Communication - EC8652','4 Principles of Management - MG8591','5 Transmission Lines & RF Systems - EC8651','6 Professional Elective II -','7 Microprocessors & Microcontrollers Laboratory - EC8681','8 VLSI Design Lab - EC8661','9 Technical Seminar - EC8611','10 Professional Communication - EC8611']   
            cre=[3,3,3,3,3,3,2,2,1,1]
        if str(sem)=='7':
            nsize=8
            sub=['1 Antennas and Microwave Engineering - EC8701','2 Optical Communication - EC8751','3 Embedded & Real Tme Systems - EC8791','4 Ad hoc and Wireless Sensor Networks - EC8702','5 Professional Elective III -','6 Open Elective II -','7 Embedded Lab - EC8711','8 Advanced Communication Lab - EC8761']
            cre=[3,3,3,3,3,3,2,2]
        if str(sem)=='8':
            nsize=3
            sub=['1 Professional Elective IV -','2 Professional Elective V -','3 Project Work - EC8811']
            cre=[3,3,10]
    if str(dept)=='civil':
        if str(sem)=='1':
            nsize=8
            sub=['1 Communicative English - HS8151','2 Mathematics I - MA8151','3 Engineering Physics - PH8151','4 Engineering Chemistry - CY8151','5 Prob Solving & Python programming - GE8151','6 Engineering Graphics - GE8152','7 Problem Solving& Python Programming Lab - GE8161','8 Physics & Chemistry Lab - BS8161']
            cre=[4,4,3,3,3,4,2,2]
        if str(sem)=='2':
            nsize=8
            sub=['1 Technical English - HS8251','2 Mathematics II - MA8251','3 Physics for Civil Engi - PH8201','4 Basic Electrical & Electronic Engi - BE8251','5 Environmental Science & Engineering - GE8291','6 Engineering Mechanics - GE8292','7 Engineering Practices Lab - GE8261','8 Computer Aided Building Drawing - CE8211']
            cre=[4,4,3,3,3,3,2,2]
        if str(sem)=='3':
            nsize=9
            sub=['1 Transforms & Partial Differential Equations - MA8353','2 Strength of Materials I - CE8301','3 Fluid Mechanics - CE8302','4 Surveying - CE8351','5 Construction Materials - CE8391','6 Engineering Geology - CE8392','7 Construction Materials Lab - CE8311','8 Surveying Lab - CE8361','9 Interpersonal Skills /Listening and Speaking - HS8381']
            cre=[4,3,3,3,3,3,2,2,1]
        if str(sem)=='4':
            nsize=9
            sub=['1 Numerical Methods - MA8491','2 Construction Techniques and Practices - CE8401','3 Strength of Materials II - CE8402','4 Applied Hydraulic Engineering - CE8403','5 Concrete Technology - CE8404','6 Soil Mechanics - CE8491','7 Strength of Materials Lab - CE8481','8 Hydraulic Engineering Lab - CE8461','9 Advanced Reading & Writing - HS8461']
            cre=[4,3,3,3,3,3,2,2,1]
        if str(sem)=='5':
            nsize=9
            sub=['1 Design of Reinforced Cement Concrete Elements - CE8501','2 Structural Analysis I - CE8502','3 Water Supply Engineering - EN8491','4 Foundation Engineering - CE8591','5 Professional Elective I -','6 Open Elective I -','7 Soil Mechanics Lab - CE8511','8 Water and Waste Water Analysis Lab - CE8512','9 Survey Camp - CE8513']
            cre=[4,3,3,3,3,3,2,2,2]
        if str(sem)=='6':
            nsize=10
            sub=['1 Internet Programming - CS8651','2 Artificial Intelligence - CS8691','3 Mobile Computing - CS8601','4 Compiler Design - CS8602','5 Distributed Systems - CS8603','6 Professional Elective I -','7 Internet Programming Lab - CS8661','8 Mobile Application Development Lab - CS8662','9 Mini Project - CS8611','10 Professional Communication - HS8581']
            cre=[3,3,3,4,3,3,2,2,1,1]
        if str(sem)=='7':
            nsize=2
            sub=['1 Estimation, Costing & Valuation Engineering - CE8701','2 Railways, Airports,Docks & Harbour Engineering - CE8702']
            cre=[3,3]
        if str(sem)=='8':
            nsize=3
            sub=['1 Professional Elective IV -','2 Professional Elective V -','3 Project Work - CE8811']
            cre=[3,3,10]
    if str(dept)=='eee':
        if str(sem)=='1':
            nsize=8
            sub=['1 Communicative English - HS8151','2 Mathematics I - MA8151','3 Engineering Physics - PH8151','4 Engineering Chemistry - CY8151','5 Prob Solving & Python programming - GE8151','6 Engineering Graphics - GE8152','7 Problem Solving& Python Programming Lab - GE8161','8 Physics & Chemistry Lab - BS8161']
            cre=[4,4,3,3,3,4,2,2]
        if str(sem)=='2':
            nsize=8
            sub=['1 Technical English - HS8251','2 Mathematics II - MA8251','3 Physics for Electronics Engi - PH8253','4 Basic Civil & Mechanical Engi - BE8252','5 Environmental Science & Engineering - GE8291','6 Circuit Theory - EE8251','7 Engineering Practices Lab - GE8261','8 Electric Circuits Lab - EE8261']
            cre=[4,4,3,4,3,3,2,2]
        if str(sem)=='3':
            nsize=8
            sub=['1 Transforms & Partial Differential Equations - MA8351','2 Digital Logic Circuits - EE8351','3 Electromagnetic Theory - EE8391','4 Electrical Machines - I - EE8301','5 Electronic Devices & Circuits - EC8353','6 Power Plan Enginnering - ME8792','7 Electronics Lab -','8 Electrical Machines LabI -']
            cre=[4,3,3,3,3,3,2,2]
        if str(sem)=='4':
            nsize=9
            sub=['1 Numerical Methods - MA8491','2 Electrical Machines I - EE8401','3 Transmission & Distribution - EE8402','4 Measurements and Instrumentation - EE8403','5 Linear Integrated Circuits & Applications - EE8451','6 Control Systems - IC8451','7 Electrical Machines LabII - EE8411','8 Linear & Digital Integrated Circuits Lab - EE8461','9 Technical Seminar - EE8412']
            cre=[4,3,3,3,3,4,2,2,1]
    return render_template("reg17.html",nsize=nsize,sub=sub,cre=cre)
    
@app.route("/calc",methods=["POST","GET"])
def calc():
    nsize = request.form["nsize"]

    n=int(nsize)
    print(n)
    credits=[]
    grades=[]
    for i in range(n):
        credit=f"c{i}"
        grade=f"grade{i}"
        credits.append(int(request.form[credit]))
        grades.append(request.form[grade])
    print(credits)
    print(grades)
    for i in range(len(grades)):

        if str(grades[i])=='o':
            grades[i]=10
        elif str(grades[i])=='a+':
            grades[i]=9
        elif str(grades[i])=='a':
            grades[i]=8
        elif str(grades[i])=='b+':
            grades[i]=7
        elif str(grades[i])=='b':
            grades[i]=6
        else:
            grades[i]=0
    print(grades)
    sum=0
    cred=0
    for i in range(n):
        cred=cred+credits[i]
        mul=credits[i]*grades[i]
        print(mul)
        sum=sum+mul
    
    avg=sum/cred
    print(avg)



    return render_template("gpa.html",avg=avg)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)