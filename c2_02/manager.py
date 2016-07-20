from flask_script import Manager

from flash import app

manager=Manager(app)

@manager.option('-n', '--name', dest='name', default='nowcoder')
def hello(name):
    print 'hello',name

@manager.command
def initialize_database():
    'initialize database~~'
    print 'databases....'

if __name__=='__main__':
    manager.run()