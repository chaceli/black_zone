#! /usr/bin/python
import pwn
import os

name = ''
def getFlag():
    '''
    The function to get call for get flag.You can make a different flag for different listen
    '''
    return "congratulations " + name + 'here is you flag: a flag'
def getName(listen):
    global name
    listen.sendline('please get you name')
    name = listen.recvline()
    
a = pwn.daemon(10)  # A demon class,The argument is the second of time out, 0 is no timeout

a.set_listen(12345)  # The port you want to listen
newEnv = os.environ.copy()
a.set_process('/bin/bash', cwd='/home/pwn', env=newEnv)  # first argument is the binary,
# make sure other has permission of execute for it
a.set_sql('explorer', '123456')  # The name and password of mysql. Default it will log data in database pwnlog.
# But you can easy change it.And dot't worry of table.I will create it
a.open_permission()
a(getFlag,getName)  # start it
