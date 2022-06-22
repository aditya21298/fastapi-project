from pydantic import BaseSettings

#setting env variables in a pydantic model for easy type casting
#pydantic looks in case sensitive so .env can have caps and config can be case senstive
class Settings(BaseSettings):
    database_hostname : str
    database_port : str
    database_password : str
    database_name : str
    database_username : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int
#telling pydantic to import .env file
    class Config:
        env_file = ".env"

settings =Settings()
