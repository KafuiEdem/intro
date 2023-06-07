import pickle
import json

"""
    Coding Challenge
In order to simply the serialization and deserialization process your task is:
1. Create a function called serialize() that takes 3 arguments: 1) the Python object you want to serialize, 2) the file to which it serializes the object and 3) the serialization protocol which is pickle or json.
The function will create the file (the 2nd argument) and will write the Python object to that file according to its 3rd argument. If the 3rd argument is pickle, It will use pickle to serialize the object and if the argument is json it will use json for serialization.
2. Create a function called deserialize() that takes 2 arguments: 1) the file which contains serialized data and 2) the type of deserialization which is pickle or json.
The function will deserialize from the file into a Python object and will return that object.
3. Test the functions by serializing and deserializing Python objects using both pickle and json.
Note: The script can also be used as a module that will be imported in other Python scripts.
"""

def serialize(py_obj,file,protocol):
    if protocol =='json':
        with open(file+".json",'w') as f:

            """
            Serialization of file to json
            """
            json.dump(py_obj,f)
            
    elif protocol =='pickel':
        with open(file+".dat",'wb') as f:

            """
             Serialization of file to pickel
            """
            pickle.dump(py_obj,f)
    else:
        print("Protocl can only be [JSON] or [PICKEL]")
    
def deserialize(file,protocol):
    if protocol =='json':
        with open(file+".json",) as f:
            
            """
                Deserialization of file to json
            """
            json_file = json.load(f)
        return json_file
    elif protocol =='pickel':
        with open(file+".dat",'rb') as f:
            
            """
                Deserialization of file to pickel
            """
            pickle_file = pickle.load(f)
        return pickle_file
        
frineds = {"Dan":[20,"London",342232],"Maria":[25,"Madrid",234533]}


serialize(frineds,"edem_json","json")
serialize(frineds,"edem_pickel","pickel")

j = deserialize("edem_json","json")
p = deserialize("edem_pickel","pickel")
print("JSON FILE >>",j,"\n","PICKEL FILE >>",p)

