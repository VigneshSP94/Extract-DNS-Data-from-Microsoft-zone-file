import os
import sys

script, ptrzne, filename = sys.argv
os.mkdir(str(ptrzne))

with open(filename, 'r') as ibfile:
    counter = 0
    no_of_data_lists = []
    data = ibfile.readlines()
    for i in data:
        data_list = []
        if 'PTR' in i:
          dataagain =  i.replace(" ",",").replace("\t",",").split(",")
          for i in dataagain:
              if i != '':
                  data_list.append(i)
        with open(str(ptrzne)+"\\"+ptrzne+".csv", 'a') as adfile:
            if len(data_list) == 4:
                adfile.write(ptrzne+"."+str(data_list[0])+","+str(data_list[3]))
                #print((ptrzne+str(data_list[0])+","+str(data_list[3])))
            if len(data_list) == 3:
                if int(data_list[0]) > 256:
                    adfile.write('blankip,'+str(data_list[2]))
                    #print(adfile.write('blankip,'+str(data_list[2]))) 
                else:
                    adfile.write(ptrzne+"."+str(data_list[0])+","+str(data_list[2]))
                    #print(ptrzne+"."+str(data_list[0])+","+str(data_list[2]))
        data_list=[]
              
          
