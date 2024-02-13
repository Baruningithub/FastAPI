from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from main import user,Session,engine




# #returns dictionary read from the json file
# def get_user_data():
#     with open(FILE_NAME) as j_file:
#         return json.load(j_file)


# user class defining their attributes
class user_data(BaseModel):
    id : int
    name:str
    email: Union[str, None] = None
    date_created: Union[str, None] = None


app = FastAPI()

local_session = Session()

users=local_session.query(user).all()

# create a new user account
@app.post("/create")

async def create(new_user:user_data, local_session): 
    new_user = local_session.add(new_user)
    
    local_session.commit()

    #json response
    return {"status": "success",
            "user_id": new_user.id,
            "message": "Your account is succesfully created"
        }



# # get/print details of an existing user
# @app.get("/get/{user_id}")
# async def get(user_id ,d : dict=Depends(get_user_data) ):

#     # Underflow check
#     if user_id not in d:
#         raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")

    
#     return {"staus":"success","message":"Your account details are"}, d[user_id]

# # updating details of an existing user
# @app.patch("/update/{user_id}")
# async def update(user_id, user:user_data , d : dict=Depends(get_user_data)):

#     # Underflow check
#     if user_id not in d:
#         raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")
    
#     d[user_id] = dict(user)

#     # dump the updates in our json file
#     with open (FILE_NAME,'w+') as out:
#         json.dump(d, out, indent=2)

#     return {"status": "success",
#             "user_id":user_id,
#             "message": "Your details are updated succesfully"
#         }


# # delete an existing user account
# @app.delete("/delete/{user_id}")
# async def delete(user_id , d : dict=Depends(get_user_data)):

#     # Underflow check
#     if user_id not in d:
#         raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")
    
#     del d[user_id]

#     # dump updates in our json file
#     with open (FILE_NAME,'w+') as out:
#         json.dump(d, out, indent=2)

#     return {"status": "success",
#             "user_id": user_id,
#             "message": "Your account is now deleted"
#         }



