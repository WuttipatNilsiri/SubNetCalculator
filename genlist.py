import itertools
import math
import sys
import numpy as np

def defClass(ip):
    test = ip.split('.')
    if int(test[0]) >= 192:
        return 'c' , 24
    elif int(test[0]) >= 128:  
        return 'b' , 16
    else:
        return 'a' , 8


possible_values = [0,1]


totalNum = 32


def isAll(_list,obj):
    check = True
    for x in _list:
        if (x == obj):
            check = check and True
        else:
            check = check and False
    return check

def listdivide8(_list):
    
    if (len(_list) <= 8):
        # print('c')
        return [_list]

    array = []
    l1 = _list[:8]
    array.append(l1)
    l2 = _list[8:len(_list)]
    # print(l2)
    array = array + listdivide8(l2)

    
    return array


def to8bitlist(_list):
    le = len(_list)
    count = 8-le
    arr = list(_list)
    for i in range(count):
        arr.append(0)
    
    return arr


def splitClass(IP,_c):
    array = IP.split('.')
    toReturnIP = ''    
    if (_c == 'c'):
        toReturnIP = '.'.join([array[0],array[1],array[2]])
    if (_c == 'b'):
        toReturnIP = '.'.join([array[0],array[1]])
    if (_c == 'a'):
        toReturnIP = '.'.join([array[0]])
    return toReturnIP
              
        



def IPtolist(IP):
    IParray = IP.split('.')
    array = []
    for x in IParray:
        array = array + int2listbin(int(x))
    return array

# IParray = IP.split('.')

def listbin2int(l):
    strbin = ''.join(str(v) for v in l)
    return int(strbin,2)
    


def int2listbin(x):
    strbin = '{0:08b}'.format(x)
    strbinarray = list(strbin)
    array = []
    for num in strbinarray:
        array.append(int(num))
    
    return array




# print( IPtolist('10.7')   )

# subnetID = itertools.product(possible_values, repeat=netNum)

# hostID = itertools.product(possible_values, repeat=hostNum)

# listres = list(subnetID)
# listres2 = list(hostID)

def hostpure(_list):
    array = []
    for x in _list:
        if not isAll(x,1) and not isAll(x,0):
            array.append(x)
    
    return array

# listres3 = hostpure(listres2)
# print(hostpure(listres2))


def joinpossibe(list1,list2):
    
    array = []
    for x in list1:
        for y in list2:
            joinedlist = list(x) + list(y)
            array.append(joinedlist)
    
    return array


def genhost1st(hostbit):
    array = []
    for i in range(hostbit-1):
        array.append(0)
    array.append(1)
    return array
    
def genhostlast(hostbit):
    array = []
    for i in range(hostbit-1):
        array.append(1)
    array.append(0)
    return array

def genbc(hostbit):
    array = []
    for i in range(hostbit):
        array.append(1)
    return array

def gennet(hostbit):
    array = []
    for i in range(hostbit):
        array.append(0)
    return array

# u = joinpossibe([IPtolist(splitClass(IP,c))],listres)

# p = joinpossibe(u,listres2)




def toString(_list):
    st = ''
    if len(_list) < 4:
        for i in range(4-len(_list)):
            _list.append([0])
    for x in _list:
        if (len(x) < 8):
            x = to8bitlist(x)
        # print(x)
        st = st + str(listbin2int(x)) + '.'
    
    return st[:len(st)-1]

# IP = '130.7.0.0'

# c , fix = defClass(IP)

# netNumber = 500

# netNum = math.ceil(math.log2(netNumber))

# hostNum = totalNum - fix - netNum


class subnetCal(object):
    def __init__(self,IP,netNumber):
        self.IP = IP
        self.c , self.fix = defClass(IP)
        self.netNum = math.ceil(math.log2(netNumber))
        self.hostNum = totalNum - self.fix - self.netNum
        self.mask = [1 for i in range(0,self.fix)]
    
    def cal(self):

        if (self.hostNum < 2):
            raise ValueError('fix= '+ str(self.fix) + ' netNum= '+ str(self.netNum) + ' hostNum= '+str(self.hostNum) + " =>impossibe") 
        
        subnetID = itertools.product(possible_values, repeat=self.netNum)

        hostID = itertools.product(possible_values, repeat=self.hostNum)

        listres = list(subnetID)
        listres2 = list(hostID)

        u = joinpossibe([IPtolist(splitClass(self.IP,self.c))],listres) 
        
        array = []
        for x in u:
            # key = toString(listdivide8(x))
            curr = joinpossibe([x],listres2)
            print(str(
                'NETID: ' + toString( listdivide8(curr[0]) ) +  
                ' Host1ST: ' + toString( listdivide8(curr[1]) ) + 
                ' Hostlast: ' + toString( listdivide8(curr[-2]) ) +
                ' BoardCast: ' + toString( listdivide8(curr[-1]) ) ))
            arrayin = []
            for i in  range( len(curr) ) :
                arrayin.append( toString( listdivide8(curr[i]) ) )
            array.append(arrayin)
            # array.append(curr)
            
        return array


    def calShort(self,sampleNum):

        if (self.hostNum < 2):
            raise ValueError('fix= '+ str(self.fix) + ' netNum= '+ str(self.netNum) + ' hostNum= '+str(self.hostNum) + " =>impossibe") 
        
        subnetID = itertools.product(possible_values, repeat=self.netNum)

        hostID = itertools.product(possible_values, repeat=self.hostNum)

        listres = list(subnetID)
        listres2 = list(hostID)



        u = joinpossibe([IPtolist(splitClass(self.IP,self.c))],listres)

        array = []
        if len(u) < sampleNum:
            sampleNum = len(u)-1
        for i in list(range(sampleNum)) + [-1]:
            # key = toString(listdivide8(x))
            curr = joinpossibe([u[i]],listres2)
            print(str(
                'NETID: ' + toString( listdivide8(curr[0]) ) +  
                ' Host1ST: ' + toString( listdivide8(curr[1]) ) + 
                ' Hostlast: ' + toString( listdivide8(curr[-2]) ) +
                ' BoardCast: ' + toString( listdivide8(curr[-1]) ) ))
            arrayin = []
            for i in range( len(curr) ) :
                arrayin.append( toString( listdivide8(curr[i]) ) )
            array.append(arrayin)
            # array.append(curr)
        
    def calSuperShort(self,sampleNum):

        if (self.hostNum < 1):
            raise ValueError('fix= '+ str(self.fix) + ' netNum= '+ str(self.netNum) + ' hostNum= '+str(self.hostNum) + " =>impossibe") 
        
        subnetID = itertools.product(possible_values, repeat=self.netNum)

        hostID = [gennet(self.hostNum),genhost1st(self.hostNum),genhostlast(self.hostNum),genbc(self.hostNum)]

        listres = list(subnetID)
        listres2 = list(hostID)



        u = joinpossibe([IPtolist(splitClass(self.IP,self.c))],listres)

        array = []
        if len(u) <= sampleNum:
            sampleNum = len(u)-1
        for i in list(range(sampleNum)) + [-1]:
            # key = toString(listdivide8(x))
            curr = joinpossibe([u[i]],listres2)
            # print(str(
            #     'NETID: ' + toString( listdivide8(curr[0]) ) +  
            #     ' Host1ST: ' + toString( listdivide8(curr[1]) ) + 
            #     ' Hostlast: ' + toString( listdivide8(curr[-2]) ) +
            #     ' BoardCast: ' + toString( listdivide8(curr[-1]) ) ))
            arrayin = []
            for i in range( len(curr) ) :
                arrayin.append( toString( listdivide8(curr[i]) ) )
            array.append(arrayin)
            # array.append(curr)
        
        
            
        return array
    def __str__(self):
        return str(
            'IP: '+self.IP+
            '\nclass: '+str(self.c)+
            '\nmask: '+str(toString(listdivide8(self.mask))) +
            '\nnetID (Bit): '+str(self.fix)+
            '\nsubnet (Bit): '+str(self.netNum)+
            '\nhost (Bit): '+str(self.hostNum) +
            '\ntotal subnet: '+str(2**self.netNum)
        )

def run(IP,netNumber,sampleNum):
    s = subnetCal(IP,netNumber)
    # print(s)
    # print('--------------------------------------')
    # if s.hostNum > 10:
    arrayres = s.calSuperShort(sampleNum)
    # print(a)  
   
    
    np.set_printoptions(linewidth=150,edgeitems=3)
    z = np.array(arrayres)
    stringres = np.array2string(z,max_line_width=150,edgeitems=3,threshold=100)
    # print(y)
    
    # for x in a:
    #    z = np.array(x)
    #    np.set_printoptions(linewidth=150,edgeitems=3)
    #    print(z)
    #    s = np.array2string(z,max_line_width=150,edgeitems=3)
    #    print(s)
    #    w = w + s + '\n' 
    
    # print(w)
    return stringres , arrayres , s
if __name__ == "__main__":
    arg = sys.argv
    res = run(arg[1],int(arg[2]),int(arg[3]))  
    # print(str(res))
    # sys.stdout.flush()
    # print(res)


# array2d = {}
# for x in u:
#     # key = toString(listdivide8(x))
#     curr = joinpossibe([x],listres2)
#     print(str(
#     'NETID: ' + toString( listdivide8(curr[len(curr)-1]) ) +  
#     ' Host1ST: ' + toString( listdivide8(curr[len(curr)-2]) ) + 
#     ' Hostlast: ' + toString( listdivide8(curr[1]) ) +
#     ' BoardCast: ' + toString( listdivide8(curr[0]) ) ))
# for x in array2d['10.7.128.0']:
# for 
# iptest = '10.7.0.0'


# print('BC: ' + toString(listdivide8(array2d[iptest][0])) )
# print('HOSTLAST: ' + toString(listdivide8(array2d[iptest][1])) )
# print('HOST1ST: ' + toString(listdivide8(array2d[iptest][len(array2d[iptest])-2])) )
# print('NETID: ' + toString(listdivide8(array2d[iptest][len(array2d[iptest])-1])) )
    # print( toString(listdivide8(array2d['10.7.128.0'][1])) )
# print(array2d['10.7.128.0'])
# for x in array2d:
#     print(x)
# print(array2d[0])
     
# print('count:'+ str(len(p)))