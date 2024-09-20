import os
from dotenv import load_dotenv

load_dotenv() #this injects the environment variables declared in the venv/.env file

key = os.getenv('OPENAI_KEY')

print('---------------------------\n' + key)
print(os.getenv('OPENAI_URL'))
print(os.getenv('OPENAI_COMPLETION'))