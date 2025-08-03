# global and local variables
DEVICE_ID = "0000"
def update_device_id(new_id):
    global DEVICE_ID  # Declare that we are using the global variable DEVICE_ID
    DEVICE_ID = new_id 

idone = "0001"
def update_device_idone(new_id):
    global idone  
    idone = new_id

update_device_idone("0002")
print(idone)