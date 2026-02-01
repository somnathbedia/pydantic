from pydantic import BaseModel,EmailStr,AnyHttpUrl,Field
from typing import List,Dict,Optional,Annotated

# Data validation
# Pydantic model 
class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str,Field(max_length=50,title="Name of the patient",description="Give the name of the patient in 50 character",examples=['Somnath','Amit'])]
    email:EmailStr
    linkedin_url:AnyHttpUrl
    age: int = Field(lt=0)
    weight:Annotated[float,Field(gt=0,strict=True)]
    # married: Optional[bool] = None
    married:Annotated[bool,Field(default=None,description='Is the patient is married or not')]
    allergies: List[str] = Field(max_length=5)
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