from os import getenv, path
from dotenv import load_dotenv_files, find_dotenv

# load_dotenv(path.join(path.dirname, '.env'))
# load_dotenv(find_dotenv())

ENV = getenv('ENV')

dotenv_file_list = ['.env']
if ENV == 'production':
  dotenv_file_list.append(path.join(path.dirname, '.env.production'))
elif ENV == 'staging':
  dotenv_file_list.append(path.join(path.dirname, '.env.staging'))
elif ENV == 'development':
  dotenv_file_list.append(path.join(path.dirname, '.env.development'))
else:
  pass

load_dotenv_files(dotenv_file_list)

SECRET_KEY = getenv('SECRET_KEY')
