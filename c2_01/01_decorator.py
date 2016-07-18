#-*- encoding=UTF-8 -*-

def log(level, *args, **kvargs):
    def inner(func):
        '''
        * 无名字的参数
        ** 有名字的参数
        '''
        def wrapper(*args, **kvargs):
            print 'before calling ', func.__name__
            print 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print 'end calling ', func.__name__
        return wrapper
    return inner

@log(level='INFO')    #装饰器
def hello(name, age):
    print 'hello'

if __name__ == '__main__':
    hello('nowcoder', 1)
    print '---------------'
    hello(name='nowcoder', age=1)
