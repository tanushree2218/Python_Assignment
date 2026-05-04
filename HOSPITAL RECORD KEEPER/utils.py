
import pickle
import os


def addPatient():
   file = open('patient.bin','ab')
   pid = int(input("\n\t Enter patient ID: "))
   pname = input("\t Enter patient name: ")
   page = input("\t Enter patient age: ")
   padd = input("\t Enter patient address: ")
   pmob = input("\t Enter patient phone no: ")
   pickle.dump(pid , file)
   pickle.dump(pname , file)
   pickle.dump(page , file)
   pickle.dump(padd , file)
   pickle.dump(pmob , file)
   print("\n\t Patient Added Successfully!")
   file.close()
   input("\nPress enter to continue....")

def viewPatient():
    file = open('patient.bin','rb')
    try:
        while True:
            print("\n\t Patient ID: ",pickle.load(file))
            print("\t Patient  Name: ",pickle.load(file))
            print("\t Patient  Age: ",pickle.load(file))
            print("\t Patient Address: ",pickle.load(file))
            print("\t Patient Phone no.: ",pickle.load(file))
            print("\t-----------------------------")
    except EOFError:
        print("\n\t Here is your all patients....")
    file.close()
    input("\nPress enter to continue...")

def searchPatientByID():
    try:
        file = open("patient.bin", "rb")
    except:
        print("No record found!")
        return
    search_id = int(input("\n\t Enter Patient ID to search: "))
    found = False
    try:
        while True:
            pid = pickle.load(file)
            pname = pickle.load(file)
            page= pickle.load(file)
            padd = pickle.load(file)
            pmob = pickle.load(file)
            if pid == search_id:
                print("\n\t Patient Found:")
                print("\t Patient ID:", pid)
                print("\t Patient Name:", pname)
                print("\t Patient Age:", page)
                print("\t Patient Address:", padd)
                print("\t Patient Phone:", pmob)
                found = True
                break
    except EOFError:
        pass
    if not found:
        print("\t\tPatient not found!")
    file.close()
    input("\nPress enter to continue....")


def updatePatientInfo():
    search_id = int(input("\n\t Enter Patient ID to update: "))
    found = False
    file = open("patient.bin", "rb")
    temp = open("temp.bin", "wb")
    try:
        while True:
            pid = pickle.load(file)
            pname = pickle.load(file)
            page = pickle.load(file)
            padd = pickle.load(file)
            pmob = pickle.load(file)
            if pid==search_id:
                print("\n\t Old Data:",pid,pname,pmob)
                pname = input("\t Enter new name: ")
                pmob = input("\t Enter new phone:")
                print("Updated Successfully!")
                found = True
            pickle.dump(pid, temp)
            pickle.dump(pname, temp)
            pickle.dump(page, temp)
            pickle.dump(padd, temp)
            pickle.dump(pmob, temp)

    except EOFError:
        pass
    file.close()
    temp.close()
    os.remove("patient.bin")
    os.rename("temp.bin", "patient.bin")
    if not found:
        print("Patient ID not found!")
    


def deletePatientrecord():
    file1 = open('patient.bin','rb')
    file2 = open('temp.bin','ab')
    search_id = int(input("\t Enter patient ID to delete: "))
    flag = 0
    try:
        while True:
            pid = pickle.load(file1)
            pname = pickle.load(file1)
            page = pickle.load(file1)
            padd = pickle.load(file1)
            pmob = pickle.load(file1)
            if pid == search_id:
                print("\n\t Patient Found: ")
                print("\t Patient name: ",pname)
                print("\t Patient age: ",page)
                print("\t Patient address: ",padd)
                print("\t Patient phone no.: ",pmob)
                flag = 1
            else:
                pickle.dump(pid,file2)
                pickle.dump(pname,file2)
                pickle.dump(page,file2)
                pickle.dump(padd,file2)
                pickle.dump(pmob,file2)
    except:
        if flag == 1:
            print("\n\t Patient Deleted Successfully!")
        else:
            print("\n\t Patient Not Found!")
        
    file1.close()
    file2.close()
    os.remove('patient.bin')
    os.rename('temp.bin','patient.bin')
    input("\nPress enter to continue...")

def addDoctor():
    file = open('doctor.bin','ab')
    did = int(input("\n\t Enter Doctor ID: "))
    dname = input("\t Enter Doctor name: ")
    dspec = input("\t Enter Specialization: ")
    dexp = input("\t Enter Experience: ")
    dmob = input("\t Enter Phone no: ")
    pickle.dump(did , file)
    pickle.dump(dname , file)
    pickle.dump(dspec , file)
    pickle.dump(dexp, file)
    pickle.dump(dmob, file)
    print("\n\t Doctor Added Successfully!")
    file.close()
    input("\nPress enter to continue....")
    
def viewDoctor():
    file = open('doctor.bin','rb')
    try:
        while True:
            print("\n\t Doctor ID: ",pickle.load(file))
            print("\t Doctor  Name: ",pickle.load(file))
            print("\t Specialization: ",pickle.load(file))
            print("\t Experience: ",pickle.load(file))
            print("\t Phone no.: ",pickle.load(file))
            print("\t-----------------------------")
    except EOFError:
        print("\n\t Here is your all doctors....")
    file.close()
    input("\nPress enter to continue...")

    
def searchDoctor():
    try:
        file = open("doctor.bin", "rb")
    except:
        print("No record found!")
        return
    search_id = int(input("\n\t Enter Doctor ID to search: "))
    found = False
    try:
        while True:
            did = pickle.load(file)
            dname = pickle.load(file)
            dspec= pickle.load(file)
            dexp = pickle.load(file)
            dmob = pickle.load(file)
            if did == search_id:
                print("\n\t Doctor Found:")
                print("\t Doctor ID:", did)
                print("\t Doctor Name:", dname)
                print("\t Doctor Age:", dspec)
                print("\t Doctor Address:", dexp)
                print("\t Doctor Phone:", dmob)
                found = True
                break
    except EOFError:
        pass
    if not found:
        print("\t\t Doctor not found!")
    file.close()
    input("\nPress Enter To Continue..")    
   
def updateDoctorDetails():
    search_id = int(input("\n\t Enter Doctor ID to update: "))
    found = False
    file = open("doctor.bin", "rb")
    temp = open("temp.bin", "wb")
    try:
        while True:
            did = pickle.load(file)
            dname = pickle.load(file)
            dspec = pickle.load(file)
            dexp = pickle.load(file)
            dmob = pickle.load(file)
            if did==search_id:
                print("\n\t Old Data:",did,dname,dspec,dmob)
                dname = input("\t Enter new name: ")
                dspec = input("\t Enter Specialisation: ")
                dmob = input("\t Enter new phone:")
                print("\t Updated Successfully!")
                found = True
            pickle.dump(did, temp)
            pickle.dump(dname, temp)
            pickle.dump(dspec, temp)
            pickle.dump(dexp, temp)
            pickle.dump(dmob, temp)

    except EOFError:
        file.close()
        temp.close()
        os.remove("doctor.bin")
        os.rename("temp.bin", "doctor.bin")
        if not found:
            print("\t Doctor ID not found!")
        input("\nPress Enter To Continue...")

def bookAppointment():
    file = open("appointment.bin", "ab")

    aid = int(input("\n\t Enter Appointment ID: "))
    pid = int(input("\t Enter Patient ID: "))
    did = int(input("\t Enter Doctor ID: "))
    date = input("\t Enter Date (dd-mm-yyyy): ")
    time = input("\t Enter Time: ")

    pickle.dump(aid, file)
    pickle.dump(pid, file)
    pickle.dump(did, file)
    pickle.dump(date, file)
    pickle.dump(time, file)

    print("\n\t Appointment Booked Successfully!")

    file.close()
    input("\nPress Enter to continue...")

def viewAppointments():
    file = open('appointment.bin','rb')
    try:
        while True:
            print("\n\t Appointment ID: ",pickle.load(file))
            print("\t Patient ID: ",pickle.load(file))
            print("\t Doctor ID: ",pickle.load(file))
            print("\t Date: ",pickle.load(file))
            print("\t Time: ",pickle.load(file))
            print("\t-----------------------------")
    except EOFError:
        print("\n\t Here is your all appointments....")
    file.close()
    input("\nPress enter to continue...")

def cancelAppointment():
    try:
        file1 = open("appointment.bin", "rb")
        file2 = open("temp.bin","wb")
    except FileNotFoundError:
        print("\nNo appointments found!")
        return
    search_id = int(input("\n\t Enter Appointment ID to cancel: "))
    found = False
    try:
        while True:
            aid = pickle.load(file1)
            pid = pickle.load(file1)
            did = pickle.load(file1)
            date = pickle.load(file1)
            time = pickle.load(file1)

            if aid == search_id:
                print("\n\t Appointment Found:")
                print("\t Patient ID:", pid)
                print("\t Doctor ID:", did)
                print("\t Date:", date)
                print("\t Time:", time)
                print("\n\t Appointment Cancelled Successfully!")
                found = True
            else:
                pickle.dump(aid, file2)
                pickle.dump(pid, file2)
                pickle.dump(did, file2)
                pickle.dump(date, file2)
                pickle.dump(time, file2)

    except EOFError:
        pass

    file1.close()
    file2.close()
    os.remove("appointment.bin")
    os.rename("temp.bin", "appointment.bin")
    if not found:
        print("\n Appointment ID not found!")
    input("\n Press Enter to continue...")

def admitPatient():
    file = open("admit.bin","ab")
    pid = int(input("\n\t Enter Patient ID: "))
    pname = input("\t Enter Patient Name: ")
    room = input("\t Enter Room Number: ")
    disease = input("\t Enter Disease: ")
    date = input("\t Enter Admit Date (dd-mm-yyyy): ")

    pickle.dump(pid, file)
    pickle.dump(pname, file)
    pickle.dump(room, file)
    pickle.dump(disease, file)
    pickle.dump(date, file)
    print("\n\t Patient Admitted Successfully!")
    file.close()
    input("\n\t Press Enter to continue...")

def viewAdmittedPatients():
    try:
        file = open("admit.bin", "rb")
    except FileNotFoundError:
        print("\n\t No admitted patients found!")
        input("\n\t Press Enter to continue...")
        return
    try:
        while True:
            print("\n\t Patient ID:", pickle.load(file))
            print("\t Name:", pickle.load(file))
            print("\t Room:", pickle.load(file))
            print("\t Disease:", pickle.load(file))
            print("\t Admit Date:", pickle.load(file))
            print("---------------------------------------")
    except EOFError:
        print("\n\t All admitted patients displayed!")

    file.close()
    input("\n\t Press Enter to continue...")

def addPrescription():
    file = open("prescription.bin", "ab")
    prid = int(input("\n\t Enter Prescription ID: "))
    pid = int(input("\t Enter Patient ID: "))
    did = int(input("\t Enter Doctor ID: "))
    med = input("\t Enter Medicine: ")
    dose = input("\t Enter Dosage: ")

    pickle.dump(prid, file)
    pickle.dump(pid, file)
    pickle.dump(did, file)
    pickle.dump(med, file)
    pickle.dump(dose, file)

    print("\n\t Prescription Added Successfully!")

    file.close()
    input("\n\t Press Enter to continue...")

def viewPrescription():
    try:
        file = open("prescription.bin", "rb")
    except FileNotFoundError:
        print("\n\t No prescriptions found!")
        input("\n\t Press Enter to continue...")
        return

    try:
        while True:
            print("\n\t Prescription ID:", pickle.load(file))
            print("\t Patient ID:", pickle.load(file))
            print("\t Doctor ID:", pickle.load(file))
            print("\t Medicine:", pickle.load(file))
            print("\t Dosage:", pickle.load(file))
            print("---------------------------------------")
    except EOFError:
        print("\n\t All prescriptions displayed!")

    file.close()
    input("\n\t Press Enter to continue...")
    
def updatePrescription():
    try:
        file1 = open("prescription.bin", "rb")
        file2 = open("temp.bin", "wb")

    except FileNotFoundError:
        print("\n\t No prescriptions found!")
        input("\n\t Press Enter to continue...")
        return

    search_id = int(input("\n\t Enter Prescription ID to update: "))
    found = False

    try:
        while True:
            prid = pickle.load(file1)
            pid = pickle.load(file1)
            did = pickle.load(file1)
            med = pickle.load(file1)
            dose = pickle.load(file1)

            if prid == search_id:
                print("\n\t Old Data:", prid, pid, did, med, dose)

                med = input("\n\t Enter new Medicine: ")
                dose = input("\n\t Enter new Dosage: ")

                print("\n\tUpdated Successfully!")
                found = True

            pickle.dump(prid, file2)
            pickle.dump(pid, file2)
            pickle.dump(did, file2)
            pickle.dump(med, file2)
            pickle.dump(dose, file2)
    except EOFError:
        pass

    file1.close()
    file2.close()
    os.remove("prescription.bin")
    os.rename("temp.bin", "prescription.bin")

    if not found:
        print("\n\t Prescription ID not found!")

    input("\n\t Press Enter to continue...")
