import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'kjbvgvDF2232354ygdfvfdyfgdb2@'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    POST_PER_PAGE = 20

