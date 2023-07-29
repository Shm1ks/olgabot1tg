import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))


admin_id = [
    676814898
]

ip = os.getenv('ip')

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGUSER'))
DATABASE = str(os.getenv('DATABASE'))


POSTGRES_URI = f'postgressql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'