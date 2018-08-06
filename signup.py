import re, uuid

class UserDetails(object):
    def __init__(self):
        #A list to store users
        self.user_list = []


    #A method to register the users
    def validate_data(self, email, username, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", email)\
            or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", username):
                return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 6:
            return "Your username should be atleast six characters long"
        elif len(password) < 6:
            return "Your password should be atleast six characters long" 
        elif password != confirm_password:
            return "Your passwords must match"
        else:
            return True

    #A method to register the user
    def register(self, email, username, password, confirm_password):
        user_details = {}

        if len(self.user_list) > 0:
            #validate user details
            validate = self.validate_data(email, username, password, confirm_password)
            if validate:
                for user in self.user_list:
                    if username == user['email'] or username == user['username']:
                        return "Username or email already exists"

                        #No user with the given email or username exist
                    else:
                        # So, register the user with correct user details
                            user_details['email'] = email
                            user_details['username'] = username
                            user_details['password'] = password
                            user_details['confirm_password'] = confirm_password
                            user_details['id'] = uuid.uuid1()
                            self.user_list.append(user_details) 
                            return "user registered successfully"

            else:
                #An error was found in the user details during validation 
                    #So the error was stored in the varible validate
                    #So you should return the error stored in the validate
                    return validate    
        
        else:
            #there are no users in the list
                #validate data
                validate = self.validate_data(email, username, password, confirm_password)
                if validate:
                    #A the validation of user details if True (user details are correct)
                    #Register the user
                    user_details['email'] = email
                    user_details['username'] = username
                    user_details['password'] = password
                    user_details['confirm_password'] = confirm_password
                    user_details['id'] = uuid.uuid1()
                    self.user_list.append(user_details)
                    return "user registered successfully"
                else:
                    #An error was found in the user details during validation 
                    #So the error was stored in the varible validate
                    #So you should return the error stored in the validate
                    return validate 

def run():
    Bassam = UserDetails()    
    response = Bassam.register("bassam", "bassam10lima@gmail.com", "halima11746", "halima11746")  
    print(response)
    response1 = Bassam.register("bassam", "bassam10lima@gmail.com", "halima11746", "halima11746")  
    print(response1)


if __name__ == "__main__":
    run()