#coding=utf-8
import sys
print sys.getdefaultencoding( )
str = 'hello everyone, say i love you for your lover'
print (str)
print '\n'.join([''.join([('LoveDaLin'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])

