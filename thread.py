import threading 


def func():
    print('thread working')

threads=[]

for i in range(5):
	th=threading.Thread(target=func) 
	threads.append(th)

for th in threads:
	th.start()

print('done')

# thread workingthread working

# thread working
# thread working
# thread working
# done