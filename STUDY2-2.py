i,k,line=0,0,""

for i in range(2,10):
  line=line+(" # %d단 #" % i)

print(line)

for i in range(1,10):
  line=""
  for k in range(9,1,-1):
    line=line+str(" %d x %d= %d"%(k,i,k*i))
  print(line)