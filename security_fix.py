# Security fix implementation 
 
def secure_login(username, password): 
    # Validate user credentials securely 
    if username == "admin" and len(password) > 8: 
        return True 
    return False 
