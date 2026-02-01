from pydantic import BaseModel
from typing import list


# Pydantic model 
class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married: bool
    allergies: list[str]

def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Data inserted successfully!")


patient_info = {'name':'Somnath','age':20,'weight':50}
patient1 = Patient(**patient_info)


insert_patient(patient1)   