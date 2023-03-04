# python3
# Mareks Siņica-Siņavskis 221RDB430
import sys
import threading
import numpy # pip install numpy 

def compute_height(n, parents):
    max_height = 0
    list = []
   
    for x in range(n):
        list.append(0)

    for i in range(n):
      height = get_h(i, parents, list)
      
      if height > max_height:
        max_height = height
        
    return max_height

def get_h(i, parents, list):

    if parents[i] == -1:
        list[i] = 1
    elif list[i] != 0:
        return list[i]
    else:
        list[i] = get_h(parents[i], parents, list) + 1
    return list[i]

def main():
    input_type = input()
    if input_type[:1] == 'F':
        file_name = input()
        try:
            with open("test/"+file_name+"") as text_file:
                n = int(text_file.readline())
                parents = numpy.asarray([int(x) for x in text_file.readline().split()])
        except IOError:
            print('Invalid file name')
            return
    elif input_type[:1] == 'I':
        n = int(input())
        parents = numpy.asarray([int(x) for x in input().split()])
    else:
        print('Invalid input!')
        return

    max_height = compute_height(n, parents)
    print(max_height)

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
