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
       stdin, stdout, stderr = ssh.exec_command(remote_cmd)
       result = stdout.read(),stderr.read()
       ssh.close()

username='app'
password='app'




def trans(scp_list):
    for  i in  user_conf.info.keys():
       for k in scp_list:
          p = multiprocessing.Process(target=sftp, args=(i,k,'/tmp/%s'% k ))
          p.start()
          print 'scp %s  to %s  is  ok'  % (k,i)
       print  '##########scp to next host###############'
    print  'done'

if user_conf.install_env == 'dmb_agent':    
    scp_list=['install.py' ,'user_conf.py','ESCAgent.zip','ESCTerminal.zip','SmartMOM.zip' ]   
    trans(scp_list)
elif user_conf.install_env == 'dmb_gov':
    scp_list=['install.py' ,'user_conf.py','ESCGovern.zip','GOVManager.zip' ]   
    trans(scp_list)
elif user_conf.install_env == 'dmb_reg':
    scp_list=['install.py' ,'user_conf.py','ESCConsole.zip','ESCManager.zip' ]   
    trans(scp_list)
elif user_conf.install_env == 'dmb_monitor':
    scp_list=['install.py' ,'user_conf.py','ESCMonitor.zip' ]   
    trans(scp_list)
elif user_conf.install_env == 'dmb_journal':
    scp_list=['install.py' ,'user_conf.py','ESCJournal.zip' ]   
    trans(scp_list)
else:
   print  'nothing to do'



#scp_list=['install.py' ,'user_conf.py','ESCGovern.zip','GOVManager.zip' ]   
#scp_list=['install_cloud_terminal_pro.py' ,'SmartMOM.zip','ESCAgent.zip','jdk-7u79-linux-x64.rpm','ESCTerminal.zip' ]   
#scp_list=['install_cloud_terminal_pro.py' ]   

#for  i in  user_conf.info.keys():
#     for k in scp_list:
#          p = multiprocessing.Process(target=sftp, args=(i,k,'/tmp/%s'% k ))
#          p.start()
#          print 'scp %s  to %s  is  ok'  % (k,i)          
#     print  '##########scp to next host###############'

#print  'done'
