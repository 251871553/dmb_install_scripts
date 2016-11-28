#!/usr/bin/env  python
#coding:utf-8
import paramiko
import user_conf
import multiprocessing

def  sftp(hostname,localpath,remotepath):
       t = paramiko.Transport((hostname,22))
       t.connect(username = username, password = password)
       sftp = paramiko.SFTPClient.from_transport(t)
       sftp.put(localpath,remotepath)
       t.close()

def  ssh(hostname,remote_cmd):
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname,22,username, password)
      # stdin, stdout, stderr = ssh.exec_command(remote_cmd,get_pty=True)
       stdin, stdout, stderr = ssh.exec_command(remote_cmd)
   #    stdin.write('app\n')
    #   stdin.flush()
       result = stdout.read(),stderr.read()
       ssh.close()
       return result

username='app'
password='app'

cmd=raw_input('please  enter you command:')

pool = multiprocessing.Pool(processes=50)
result = {}
for  i in  user_conf.info.keys():
          a=pool.apply_async(ssh, (i,cmd, ))
          result[i]=a
pool.close()
pool.join()

number=0
for  k,v in result.items():
     print '\033[32m[%s]\033[0m'  %k
     number=number+1
     print 'number %s machine output:\n ' %number
     for content in  v.get():
         print content
