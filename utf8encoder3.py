import sys

def findclass(n):
    pos=n.find('1')
    if pos>=9:
        return 1
    elif pos>=5:
        return 2
    else:
        return 3

def convert(n,i):
    ans_arr=[]
    ans=''
    if i==1:
        ans+='0'
        ans+=n[9:]
        ans_arr.append(hex(int(ans, 2)))
    elif i==2:
        ans+='110'
        ans+=n[5:10]
        ans_arr.append(hex(int(ans, 2)))
        ans=''
        ans+='10'
        ans+=n[10:]
        ans_arr.append(hex(int(ans, 2)))
    else:
        ans+='1110'
        ans+=n[:4]
        ans_arr.append(hex(int(ans, 2)))
        ans=''
        ans+='10'
        ans+=n[4:10]
        ans_arr.append(hex(int(ans, 2)))
        ans=''
        ans+='10'
        ans+=n[10:]
        ans_arr.append(hex(int(ans, 2)))
    return ans_arr

#readFile=str(sys.argv[1])
f=open('utf8encoder_out.txt', 'w')
f.close()
with open('C:/Python34/NLP/english_in.txt',"rb") as readInp:
    byte=b"a"
    while byte:
        byte=readInp.read(1)
        if byte==b"":
            break
        data1='{:08b}'.format(ord(byte))
        byte=readInp.read(1)
        data2='{:08b}'.format(ord(byte))
        data=data1+data2
        i=findclass(data)
        answer=convert(data,i)
        with open('utf8encoder_out.txt', 'ab') as output:
            output.write(bytearray(int(j, 16) for j in answer))
            output.close()
    readInp.close()
