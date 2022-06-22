from passlib.context import CryptContext

#Telling hashlib to use bcrypt has default algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def hash(password : str):
    return pwd_context.hash(password)


def verify(txt_password, hashed_password):
    return pwd_context.verify(txt_password,hashed_password)