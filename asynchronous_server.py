import socket
import select
import Queue
import sys

s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
inputs=[s]
message_queues={}
outputs=[]
while inputs:
    readable,writable,exception=select.select(inputs,outputs,[])
    for r in readable:
        if r is s:
            cl,addr=s.accept()
            print 'Got a new connection form:',addr
            inputs.append(cl)
            message_queues[cl]=Queue.Queue()
        else:
            data=r.recv(1024)
            if data:
                print>>sys.stderr,'received "%s" from %s' % (data, r.getpeername())
                message_queues[r].put("hi bro")
                if r not in outputs:
                    outputs.append(r)
            else:
                print>>sys.stderr,'closing client',addr
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                r.close()
                del message_queues[r]
    for k in writable:
        try:
            next_msg=message_queues[k].get_nowait()
        except Queue.Empty:
            print>>sys.stderr,'output queue for',message_queues[k],' is  empty.'
            outputs.remove(k)
        else:
            print>>sys.stderr,'sending %s to %s' %(next_msg,k.getpeername())
            k.send(next_msg)
    for t in exception:
        print>>sys.stderr,'handling exception for ',t.getpeername()
        inputs.remove(t)
        if t in 
