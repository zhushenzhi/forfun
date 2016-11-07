"""

保留地址主要在以下三类：
A类：10.0.0.0－10.255.255.255
     100.64.0.0－100.127.255.255
B类：172.16.0.0－172.31.255.255\]
C类：192.168.0.0－192.168.255.255
人们根据需要来选用适当的地址类，在内部局域网中将这些地址当作公用IP地址一样地使用。在互联网上，那些不需要与互联网通讯的设备，如打印机、可管理集线器等也可以使用这些地址，以节省IP地址资源。
特殊IP地址：
0.0.0.0
  它表示的是这样一个集合：所有不清楚的主机和目的网络。这里的“不清楚”是指在本机的路由表里没有特定条目指明如何到达。如果在网络设置中设置了缺省网关，那么系统会自动产生一个目的地址为0.0.0.0的缺省路由.对本机来说，它就是一个“收容所”，所有不认识的“三无”人员，一 律送进去。如果你在网络设置中设置了缺省网关，那么Windows系统会自动产生一个目的地址为0.0.0.0的缺省路由。
169.254.x.x
  如果主机使用了动态主机设置协议功能自动获得一个IP地址，那么当动态主机设置协议服务器发生故障，或响应时间太长而超出了一个系统规定的时间，系统会分配这样一个地址。如果发现主机IP地址是一个这样的地址，该主机的网络大都不能正常运行。
224.0.0.0 -239.255.255.255 
   广播地址
240.0.0.0 -255.255.255.255
   暂时保留
127.0.0.0 -127.255.255.255 
   系统回环地址


"""
import re

pattern_a1 = '^10(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){3}$'
pattern_a2 = '^100\.(6[4-9]|[7-9][0-9]|1[01][0-9]|12[07])(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){2}$'
pattern_b = '^172\.([1][6-9]|[2]\d|3[01])(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){2}$'
pattern_c = '^192\.168(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){2}$'
pattern_ip = '^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$'
pattern_169 = '^169\.254\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$'
pattern_224 = '^2([34]\d|2[4-9]|5[0-5])(\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])){3}$'
pattern_127 = '127(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){3}$'


prog_a1 = re.compile(pattern_a1)
prog_a2 = re.compile(pattern_a2)
prog_b = re.compile(pattern_b)
prog_c = re.compile(pattern_c)
prog_ip = re.compile(pattern_ip)
prog_169 = re.compile(pattern_169)
prog_224 = re.compile(pattern_224)
prog_127 = re.compile(pattern_127)

special_ip = ['0.0.0.0']


def check_ip(ipstr):
    '''
    whether ip
    '''
    result = prog_ip.match(ipstr)
    return result


def check_special(ipstr):
    if ipstr in special_ip:
        return False
    else:
        return True


def check_ipa1(ipstr):
    '''
       Whether the A class of ip
       10.0.0.0-10.255.255.255
       If it is true, it returns the IP
       If it is false, it returns None
    '''
    result = prog_a1.match(ipstr)
    # print result
    return result

def check_ipa2(ipstr):
    '''
        100.64.0.0-100.127.255.255
    '''
    result = prog_a2.match(ipstr)
    # print result
    return result

def check_ipb(ipstr):
    '''
       whether the B class of ip
       172.16.0.0-172.31.255.255
    '''
    result = prog_b.match(ipstr)
    # print result
    return result


def check_ipc(ipstr):
    '''
       whether the C class of ip
       192.168.0.0-192.168.255.255
    '''
    result = prog_c.match(ipstr)
    # print result
    return result


def check_169(ipstr):
    """
       whether 169.254.x.x
    """
    result = prog_169.match(ipstr)
    return result


def check_224(ipstr):
    """
      whether 224.x.x.x - 255.x.x.x
    """
    result = prog_224.match(ipstr)
    return result

def check_127(ipstr):
    """
      whether 127.x.x.x
    """
    result = prog_127.match(ipstr)
    return result

def is_network_ip(ipstr):
    '''
    check whether it is network ip
    '''
    result_ip = check_ip(ipstr)
    if result_ip is None:
        return False

    result_special = check_special(ipstr)
    if result_special is False:
        return False

    result_a1 = check_ipa1(ipstr)
    if result_a1 is not None:
        return False

    result_a2 = check_ipa2(ipstr)
    if result_a2 is not None:
        return False


    result_b = check_ipb(ipstr)
    if result_b is not None:
        return False

    result_c = check_ipc(ipstr)
    if result_c is not None:
        return False

    result_169 = check_169(ipstr)
    if result_169 is not None:
        return False

    result_224 = check_224(ipstr)
    if result_224 is not None:
        return False

    result_127 = check_127(ipstr)
    if result_127 is not None:
        return False

    return True


#testa = check_ipa('100.1.1.1')
#testb = check_ipb('173.16.1.1')
#testc = check_ipc('193.168.1.1')
# test = is_network_ip('224.0.0.251')
# print test
