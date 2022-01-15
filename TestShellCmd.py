# coding=utf-8
import os
import subprocess

def shell(command, stdin):
    """
    执行命令，返回一个tuple对象(ele1,ele2,ele3)，ele1为stdout输出内容，ele2为stderr输出内容，ele3为shell执行返回码(相当于echo $?)
    这种方式能够让执行很耗时的shell在执行过程中实时获取输出内容，如执行cat一个很大的文件，这时候就能在执行命令过程中实时获取cat输出结果command shell脚本字符串stdin 为shell脚本提供输入的内容
    有一个缺点就是p.returncode是立即返回的（脚本没执行完returncode为None），也许这个时候脚本没执行完
    :param command:
    :param stdin:
    :return:
    """
    p = subprocess.Popen(command, shell=True, close_fds=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    res = p.communicate(stdin)
    return res[0], res[1], p.returncode

if __name__ == '__main__':
  result = shell ("date",None)
  print (result[0])
  print (result[1])
  print (result[2])
  #result = os.popen("date")
  #print (result.read())
  #cmd = "/root/local/bin/kubectl get svc | grep kafka-svc"
  #if os.popen(cmd).read() != "":
  #  print ("kafka svc already exits")
