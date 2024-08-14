from dotenv import dotenv_values
config = dotenv_values(".env") 


ICC_USER =config['ICC_USER']
ICC_PASSWORD = config['ICC_PASSWORD']

print(1)