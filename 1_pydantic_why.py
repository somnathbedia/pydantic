from pydantic import BaseModel,EmailStr,AnyHttpUrl
from typing import List,Dict,Optional

# Data validation
# Pydantic model 
class Patient(BaseModel):
    name: str
    email:EmailStr
    linkedin_url:AnyHttpUrl
    age: int
    weight:float
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str,str]
                      #    k   v 

                    
def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.contact_details)
    print("Data inserted successfully!")


patient_info = {'name':'Somnath','email':'somnath@gmail.com','linkedin_url':'https://www.linkedin.com/in/somnath-bedia-640178225/','age':20,'weight':50.5,'married':1,'allergies':['pollen','dust'],'contact_details':{'phone':'128745765','address':'Vill - Paglapur, PO-LacchiPur'}}
patient1 = Patient(**patient_info)


insert_patient(patient1)   