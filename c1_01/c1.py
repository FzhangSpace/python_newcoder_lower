#-*- encoding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content,'html.parser')
    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip()

def demo_String():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    strb = '  \n\rhello nowcoder  '
    print 1, strb.lstrip(), 1
    print 2, strb.lstrip().rstrip(), 2
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, 'len =',len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('ello')

def demo_operation():
    print 1, 1+2, 5/2, 5*2, 5-2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2<<3
    print 5, 5|3, 5&3, 5^3,
    x = 2
    y = 3.3
    print x, y, type(x), type(y)

def demo_buildinFunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x + 3')
    print 7, chr(65), ord('A')
    print 8, divmod(11, 3)

def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'
    while score < 100:
        print score
        score += 10
    score = 65

    for i in range(0, 10, 2):
        if i == 0:
            pass #do_special
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break

if __name__ == '__main__':
    print 'hello world'

    #def qiushibaike()
    #demo_String()
    #demo_operation()
    #demo_buildinFunction()
    demo_controlflow()