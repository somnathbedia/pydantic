from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float #kg
    height:float #mtr
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field()
    @property
    def calculate_bmi(self)->float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI',patient.calculate_bmi)
    print("updated")

patient_info = {'name':'Somnath Bedia','email':'somnathbedia7@gmail.com','age':23,'weight':49,'height':1.64,'married':False,'allergies':['pollen','dust'],'contact_details':{'village':'Rashbera'}}

patient = Patient(**patient_info)

update_patient_data(patient)

