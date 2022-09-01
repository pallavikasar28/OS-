import threading as thread
import random
global x                #Shared Data\n",
x = 0
lock = thread.Lock()    #Lock for synchronising access\n",
def Reader():
    global x
    print('Reader is Reading!')
    lock.acquire()      #Acquire the lock before Reading (mutex approach)\n",
    print('Shared Data:', x)
    lock.release()      #Release the lock after Reading\n",
    print()

def Writer():
    global x
    print('Writer is Writing!')
    lock.acquire()      #Acquire the lock before Writing\n",
    x += 1              #Write on the shared memory\n",
    print('Writer is Releasing the lock!')
    lock.release()      #Release the lock after Writing\n",
    print()
        
"if__name__" == '__main__'
for i in range(0, 10):
    randomNumber = random.randint(0, 100)#Generate a Random number between 0 to 100\nif(randomNumber > 50)
    if(randomNumber > 50):
        Thread1 = thread.Thread(target = Reader)
        Thread1.start()
    else:
        Thread2 = thread.Thread(target = Writer)
        Thread2.start()
        
Thread1.join()
Thread2.join()
        
        # print(x)"
      
      
