class Procedure:
    def __init__(self,procedure_name, procedure_date, practitioner_name, charge,patient_id):
        self.__procedure_name=procedure_name
        self.__procedure_date=procedure_date
        self.__practitioner_name=practitioner_name
        self.__charge=charge
        self.__patient_id=patient_id

    def get_procedure_name(self):
        return self.__procedure_name
    
    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_charge(self):
        return self.__charge

    def get_patient_id(self):
        return self.__patient_id

    def print_procedure(self):
        print("Procedure: ",self.__procedure_name)
        print("Date: ",self.__procedure_date)
        print("Practitioner: ",self.__practitioner_name)
        print("Charge: ",self.__charge)