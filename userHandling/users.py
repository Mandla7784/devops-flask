import json
import os
import userHandling.userHandler as userHandler

new_user = userHandler.User("Mandla","gmal")

print(new_user.getEmail() , new_user.getName())

def save_users_to_json(users , filename ="users.json"):
    with open(filename , "w") as f:
        try:
            json.dump(users, f, indent=4)
        except Exception as e:
            print(f"An error occurred while saving users: {e}")
        
        
def load_users(filename="users.json"):

    if os.path.exists(filename):
        
        with open(filename , "r") as f:
            try:
                return json.load(f)
            
            except Exception as e:
                print(f"An Error occured when saving data" , e.__context__)
        return {}
        

def main():
    save_users_to_json([{} ,{},{}])
    
    

    
if __name__=="__main__":
    main()