import sys

dev = sys.argv[1]
pre = sys.argv[2]

if (len(sys.argv) < 3):
        print("rack of sys.argv")
        exit()


develf = open(dev, "r").read().split("\n")[:-1]
predictf = open(pre, "r").read().split("\n")[1:-1]
#print(develf)
#print(predictf)

TP=0
TN=0
FP=0
FN=0

for line1, line2 in zip(develf, predictf): 
        #print(line2.split(" "))
        # print(line1.split(" "))
        
        devlist=line1.split(" ")[0]
        #print(devlist)
        
        prelist=line2.split(" ")[0]
        #print(prelist)
        
        if (int(prelist) == 1) and (int(prelist) == int(devlist)):
        #if int(prelist) == 1 and int(devlist) == 1:
                 #print("a")
                
                TP += 1
                 
        if (int(prelist) == -1) and (int(prelist) == int(devlist)):

                TN += 1
                
        if (int(prelist) == 1) and (int(prelist) != int(devlist)):

                FP += 1

        if (int(prelist) == -1) and (int(prelist) != int(devlist)):

                FN += 1

print("TP=",TP)
print("TN=",TN)
print("FP=",FP)
print("FN=",FN)

precision = TP/(TP+FP)

recall = TP/(TP+FN)

F = (2*recall*precision)/(recall+precision)

print("F=",F)

#for line1, line2 in zip(develf,predictf):
  #      print(line1.split(" "))
    #    if int(line1.split(" ")[0]) == int(line2.split(" ")[0]):
    #      TP += 1
    # if int(line1.split(" ")[0]) == int(line2.split(" ")[0]):
    #    (line2.split(" ")[0],end=(" "))
