#!/usr/bin/env  python
#coding:utf-8
import paramiko
import user_conf
import  sys

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
     #  stdin.write('app\n')
    #   stdin.flush()
       result = stdout.read(),stderr.read()
       ssh.close()
       return result

username='app'
password='app'

def service(cmd):
     if len(sys.argv) > 1:
         if sys.argv[1]=='start':     
             for  i in  user_conf.info.keys():
                  ssh(i,cmd)
                  print  '%s  is  ok'  % i
         if sys.argv[1]=='stop':
             for  i in  user_conf.info.keys():
                  cmd='pkill  -9 java'
                  ssh(i,cmd)
         if sys.argv[1]=='status':
             for  i in  user_conf.info.keys():
                  cmd='ps  aux  |  grep java |  grep  -v "grep" '
                  for k in ssh(i,cmd):
                      print  '%s output' % i
                      print k
         else:
             print 'error input ,please enter: start | stop | status' 
     else:
         print 'error input ,please enter: start | stop | status' 


if user_conf.install_env == 'dmb_agent':
    cmd='cd  /data/agent/ESCAgent/tools;source /etc/profile;nohup sh startAgent.sh  >  /dev/null 2>&1 &'
    service(cmd)
    
elif user_conf.install_env == 'dmb_gov':
    cmd='cd  /data/app/GOVManager/bin;source /etc/profile;sh /data/app/GOVManager/bin/startGovern.sh'
    service(cmd)
elif user_conf.install_env == 'dmb_reg':
    cmd='cd /data/app/ESCManager/bin/;source /etc/profile;sh /data/app/ESCManager/bin/startConsole.sh'
    service(cmd)
elif user_conf.install_env == 'dmb_monitor':
    cmd='cd  /data/app/ESCMonitor/bin/;source /etc/profile;sh /data/app/ESCMonitor/bin/startMonitor.sh'
    service(cmd)
elif user_conf.install_env == 'dmb_journal':
    cmd='cd  /data/agent/ESCAgent/tools;source /etc/profile;nohup sh startAgent.sh  >  /dev/null 2>&1 &'
    service(cmd)
else:
   print  'nothing to do'

