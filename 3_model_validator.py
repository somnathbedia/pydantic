from pydantic import BaseModel,EmailStr,field_validator,model_validator
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patient older than 60 must have emergency contect')
        return  self
    
def save_patient(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.allergies)

    print("patient record inserted successfully!")


patient_info = {'name':'Somnath','email':'somnath@hdfc.com','age':76,'weight':50.5,'married':1,'allergies':['pollen','dust'],'contact_details':{'phone':'128745765','address':'Vill - Paglapur, PO-LacchiPur','emergency':'23652875'}}

patient1 = Patient(**patient_info) #validation->Type coersion

save_patient(patient1)