'''HOSPITAL KEEPER RECORD'''

'''
PATIENT(patient id, name, age, address, gender, phone no.)
DOCTOR(doctor id, name, specialisation, available time)
APPOINTMENT(appointment id, patient id, dpctor id, date and time)
DISCHARGE(add id, pateint id,  room no, addm date, discharge date)
MEDICINE(perscription id, patient id, doctor id, medicines, notes)
LOGIN

1. Add new patient
2. View patient details
3. Search patient (by ID)
4. Update patient info
5. Update patient info
6. Add doctor
7. View doctor list
8. Search doctor
9. Update doctor details
10. Book appointment
11. View appointments
12. Cancel appointment
13. Admit patient
14. View admitted patients
15. Add prescription
16. View prescription
17. Update prescription
18. Admin login
19. Check Password
'''

import utils as u   
u.addPatient
u.viewPatient
u.searchPatientByID
u.updatePatientInfo
u.deletePatientrecord
u.addDoctor
u.viewDoctor
u.searchDoctor
u.updateDoctorDetails
u.bookAppointment
u.viewAppointments
u.cancelAppointment
u.admitPatient
u.viewAdmittedPatients
u.addPrescription
u.viewPrescription
u.updatePrescription


# DASHBOARD
input("\t\t Press enter to continue...")

# Authentication
userName = input("\t\t Enter the User Name: ")
user = 'admin'
password = input("\t\t Enter the password:")
password1 ='admin1110'
if(userName == user and password1 == password):
    print("\t\t\t Login Successfully...")
    print("\t*******************************************")
    input("\t Press Enter to Continue...")
    while True:
        print("\n\t\t\t***************HOSPITAL RECORD KEEPER******************")
        print('''
                 1. Add patient
                 2. View patient details
                 3. Search patient (by ID)
                 4. Update patient info
                 5. Delete patient info
                 6. Add doctor
                 7. View doctor list
                 8. Search doctor
                 9. Update doctor details
                 10. Book appointment
                 11. View appointments
                 12. Cancel appointment
                 13. Admit patient
                 14. View admitted patients
                 15. Add prescription
                 16. View prescription
                 17. Update prescription
                 18. EXIT 
              ''')
        ch=int(input("\n\t Enter your choice:"))
        if ch==18:
            print("\n\t\t BYE-BYE ADMIN!")
            break
        elif ch==1:
            u.addPatient()
        elif ch==2:
            u.viewPatient()
        elif ch==3:
            u.searchPatientByID()
        elif ch==4:
            u.updatePatientInfo()
        elif ch==5:
            u.deletePatientrecord()
        elif ch==6:
            u.addDoctor()
        elif ch==7:
            u.viewDoctor()
        elif ch==8:
            u.searchDoctor()
        elif ch==9:
            u.updateDoctorDetails()
        elif ch==10:
            u.bookAppointment()
        elif ch==11:
            u.viewAppointments()
        elif ch==12:
            u.cancelAppointment()
        elif ch==13:
            u.admitPatient()   
        elif ch==14:
            u.viewAdmittedPatients()
        elif ch==15:
            u.addPrescription()
        elif ch==16:
            u.viewPrescription()
        elif ch==17:
            u.updatePrescription()
        input("\n\t Press Enter To Continue..")   
                
else:
    print("\t\tIncorrect UserName and Password")
        
 
