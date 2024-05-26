from queue import Queue

print("1. Register Patient")
print("2. Remove Patient after Meeting Doctor")
print("3. Display Patient Queue")
print("4. Exit")

patient_queue = Queue()
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        patient_name = input("Enter the patient's name: ")
        patient_queue.put(patient_name)
        print(f"Patient {patient_name} has been registered.")
    elif choice == '2':
        if not patient_queue.empty():
            print(f"Patient {patient_queue.get()} has met the doctor.")
        else:
            print("No patients in the queue.")
    elif choice == '3':
        print("Patient left to be attended:")
        temp = list(patient_queue.queue)
        for patient in temp:
            print(patient)
    elif choice == '4':
        print("Exiting the program......")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
