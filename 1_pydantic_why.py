from pydantic import BaseModel
from typing import List,Dict


# Pydantic model 
class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
                      #    k   v 
def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.contact_details)
    print("Data inserted successfully!")


patient_info = {'name':'Somnath','age':20,'weight':50.5,'married':1,'allergies':['pollen','dust'],'contact_details':{'email':'somnathbedia7@gmail.com','phone':'128745765'}}
patient1 = Patient(**patient_info)


insert_patient(patient1)   