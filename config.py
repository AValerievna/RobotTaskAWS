"""This file holds pytest environment variables used in framework and tests."""
import os
from dotenv import load_dotenv

load_dotenv()

AWS_SERVER_PUBLIC_KEY = os.getenv('AWS_SERVER_PUBLIC_KEY', 'public_key')
AWS_SERVER_SECRET_KEY = os.getenv('AWS_SERVER_SECRET_KEY', 'secret_key')
