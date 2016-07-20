# -*- encoding=UTF8 -*-

from nowstagram import app
from flask_script import Manager

manage = Manager(app)

if __name__=='__main__':
    manage.run()