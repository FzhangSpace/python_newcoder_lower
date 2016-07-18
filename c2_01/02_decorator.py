#-*- encoding=UTF-8 -*-

def log(func):
    def wrap(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrap

@log
def now():
    print '2016-7-7'


def doSomeThing(args):
    print 'doSomeThing, ', args
    def log(func):
        def wrapper(name):
            print 'call %s() before:' % func.__name__
            return func(name)
        return wrapper
    return log

@doSomeThing('args')
def hello(name):
    print 'hello ',name

if __name__ == '__main__':

    #now()
    #log(now)()
    hello('nowcoder')



