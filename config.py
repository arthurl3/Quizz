from os import environ, path, getcwd


BASE_DIR = path.abspath(getcwd())
DEBUG = True
"""Create SQLAlchemy engine and session objects."""

### SQL_ALCHEMY ###
# <!>For Windows only (due to \ escape, need to transform the string into a raw string by using r"{}".format<!>
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '\database\quizz.sqlite'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Pas encore set
#SQLALCHEMY_DATABASE_PEM = environ.get("SQLALCHEMY_DATABASE_PEM")
#os.environ.get('DATABASE_URL') or
