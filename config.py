import os


class Config(object):
    ### FLASK ###
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True

    ### SQL_ALCHEMY ###
    # <!>For Windows only (due to \ escape, need to transform the string into a raw string by using r"{}".format<!>
    SQLALCHEMY_DATABASE_URI =  r"{}".format(
        'sqlite:///' + os.path.join(BASE_DIR, 'app/database/quizz.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #os.environ.get('DATABASE_URL') or
