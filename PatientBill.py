from pickle import TRUE
import PatientClass as pa
import ProcedureClass as pr

pat1=pa.Patient(1,"Matt Jones","123 Main st, Waco TX 76706","254-555-7415",TRUE)

pro1=pr.Procedure("Physical Exam","2/15/2022","Dr. Irvine",250,1)
pro2=pr.Procedure("MRI","2/15/2022","Dr. Hamilton",1500,1)
pro3=pr.Procedure("CT Scan","2/17/2022","Dr. Drey",1200,2)

print("*** Patient Bill***")
pat1.print_patient()
print_procedure()
pro2=print_procedure()
pro3=print_procedure()