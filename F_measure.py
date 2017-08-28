import sys

a = sys.argv[1]
b = sys.argv[2]

if (len(sys.argv) < 3):
    print("rack of sys.argv")
    exit()


develf = open(a, "r").read().split("\n")[:-1]
predictf = open(b, "r").read().split("\n")[1:-1]
#print(develf)
#print(predictf)
i=0
TP=0
for line1, line2 in zip(develf,predictf):
    print(line1)
#    if int(line1.split(" ")[0]) == int(line2.split(" ")[0]):
  #      TP += 1
   # if int(line1.split(" ")[0]) == int(line2.split(" ")[0]):    
    #    (line2.split(" ")[0],end=(" "))
