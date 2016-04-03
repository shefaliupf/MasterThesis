file = open('Analysis.csv', 'r')

lines = file.readlines()

array = []

for line in lines:
    array.append(line.split(','))
    
babylist = (np.array(array)).astype(int)

#for ii in range(len(array)):
    #array[ii][0] = int(array[ii][0])
    #array[ii][2] = int(array[ii][2])
  



file = open('Butterflyscore.csv', 'r')

linesbut = file.readlines()

arraybut = []

for line in linesbut:
    arraybut.append(line.split(','))
    
#for ii in range(len(arraybut)):
    #for jj in range(len(arraybut[ii])):
        #arraybut[ii][jj] = int(arraybut[ii][jj])
        


## weight for all
butterflyscore = (np.array(arraybut)).astype(int)
x = np.zeros(len(babylist))
babylistbscore = np.column_stack([babylist,x])

for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where( babylist[:,0] == id)[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
        print id,a, average, babylist[a]com
        babylistbscore[a[0]][-1] = average
        

weight = babylistbscore[:,2]
bscore = babylistbscore[:,3]




m, b = np.polyfit(weight, bscore, 1)

plt.plot(weight, bscore, 'r*')
plt.plot(weight, m*weight + b, '-')

com
## weight for just control or cases 

var = 1

butterflyscore = (np.array(arraybut)).astype(int)
x = np.zeros(len(babylist))
babylistbscore = np.column_stack([babylist,x])

for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where((babylist[:,0] == id) & (babylist[:,1] == var) )[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
        print id,a, average, babylist[a]
        if len(a) != 0:
            babylistbscore[a[0]][-1] = average
        

weightcase = babylistbscore[:,2]
bscorecase = babylistbscore[:,3]


com

m, b = np.polyfit(weight, bscore, 1)

plt.plot(weight, bscore, 'r*')
plt.plot(weight, m*weight + b, '-')


file = open('McArthur.csv', 'r')

lines = file.readlines()

mcarthur = []

for line in lines:
   mcarthur.append(line.split(','))
   com
mcarthur = (np.array(mcarthur)).astype(int)


x = np.zeros(len(babylistbscore))
babylistmcarthur = np.column_stack([babylistbscore,x])

for ii in range(len(mcarthur)):
    id = mcarthur[ii][0]
    a = np.where( babylistbscore[:,0] == id)[0]
    if len(a) != 0:
            babylistmcarthur[a[0]][-1] = mcarthur[ii][2]
            
weight = babylistmcarthur[:,2]
mcscore = babylistmcarthur[:,-1]
    
m, b = np.polyfit(weight, mcscore, 1)

plt.plot(weight, mcscore, 'r*')
plt.plot(weight, m*weight + b, '-')
plt.xlim(2000,3000)


np.argmax(babylistmcarthur[:,-1])
np.argmax(babylistmcarthur[:,3])

### Reading Disjunction

###Reading Brazen Data

file = open('Brazelton.csv', 'r')

lines = file.readlines()

array = []

for line in lines:
    array.append(line.split(','))

headers = array[0]

array.pop(0)
array.pop(0)

Brazelton = (np.array(array)).astype(float)

plt.plot( Brazelton[:,3], Brazelton[:,7], 'ro') 


plt.plot( Brazelton[:,3], Brazelton[:,7])

indcase = np.where(Brazelton[:,1] == 1)[0]

Brazeltoncase = Brazelton[indcase]

x = np.zeros( len(Brazeltoncase))

Brazelbutscore = np.column_stack([Brazeltoncase,x])

for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where(Brazelbutscore [:,0] == id)[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
       
        if len(a) != 0:
            Brazelbutscore[a[0]][-1] = average

## Plotting graphs

weightbb = Brazelbutscore[:,4]
Butscore = Brazelbutscore[:,-1]

m, b = np.polyfit(weightbb, Butscore, 1)
plt.plot( weightbb, Butscore , 'r*')

plt.plot(weightbb, m*weightbb + b, '-')

plt.xlabel('Weight(gms)')
plt.ylabel('Butterflyscore')

output_file  = '/home/shefali/Desktop/plots/butterflyscorewithweight.png'
plt.savefig(output_file)


Apgar = Brazelbutscore[:,8]

m, b = np.polyfit(Apgar, Butscore, 1)
plt.plot(Apgar, Butscore , 'r*')
plt.xlim(5,12)

plt.plot(Apgar, m*Apgar + b, '-')

plt.xlabel('Apgar')
plt.ylabel('Butterflyscore')

output_file  = '/home/shefali/Desktop/plots/butterflyscorewithApgar.png'
plt.savefig(output_file)

label = range(104)

Butscore = Brazelbutscore[:,-1]

for ii in range(2,103):
    var = Brazelbutscore[:,ii]
    #if ii == 11:
       #ii = ii + 1 
    try:
            m, b = np.polyfit(var, Butscore, 1)
            plt.plot( var, Butscore , 'r*')
            plt.plot(var, m*var + b, '-')
            plt.xlabel(ii)
            plt.ylabel('Butterflyscore')
            plt.ylim(min(Butscore)-1, max(Butscore) + 2)
            offset = (max(var) - min(var))/len(var) 
            plt.xlim( min(var) - offset, max(var) + offset)
            
            output_file  = '/home/shefali/Desktop/plotstests/butterflyscorewith' + str(ii) +'.png'
            plt.savefig(output_file)
            plt.show()
        
        
 
    except:
         
         print 'you can\'t do this'

ii = 50
var = Brazelbutscore[:,ii]
m, b = np.polyfit(var, Butscore, 1)
plt.plot( var, Butscore , 'r*')
plt.plot(var, m*var + b, '-')
plt.xlabel(ii)
plt.ylabel('Butterflyscore')
plt.ylim(min(Butscore)-1, max(Butscore) + 2)
offset = (max(var) - min(var))/len(var) 
plt.xlim( min(var) - offset, max(var) + offset)

output_file  = '/home/shefali/Desktop/plots/butterflyscorewith' + str(ii) +'.png'
plt.savefig(output_file)
plt.show()for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where(Brazelbutscore [:,0] == id)[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
       
        if len(a) != 0:
            Brazelbutscore[a[0]][-1] = average

for ii in range(51,103):
    var = Brazelbutscore[:,ii]
 
    m, b = np.polyfit(var, Butscore, 1)
    plt.plot( var, Butscore , 'r*')
    plt.plot(var, m*var + b, '-')
    plt.xlabel(ii)
    plt.ylabel('Butterflyscore')
    plt.ylim(min(Butscore)-1, max(Butscore) + 2)
    offset = (max(var) - min(var))/len(var) 
    plt.xlim( min(var) - offset, max(var) + offset)
    
    output_file  = '/home/shefali/Desktop/plots/butterffor ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where(Brazelbutscore [:,0] == id)[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
       
        if len(a) != 0:
            Brazelbutscore[a[0]][-1] = averagelyscorewith' + str(ii) +'.png'
    plt.savefig(output_file)
    plt.show()

for ii in range(91,103):
    var = Brazelbutscore[:,ii]
 
    m, b = np.polyfit(var, Butscore, 1)
    plt.plot( var, Butscore , 'r*')
    plt.plot(var, m*var + b, '-')
    plt.xlabel(ii)
    plt.ylabel('Butterflyscore')
    plt.ylim(min(Butscore)-1, max(Butscore) + 2)for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where(Brazelbutscore [:,0] == id)[0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
       
        if len(a) != 0:
            Brazelbutscore[a[0]][-1] = average
    offset = (max(var) - min(var))/len(var) 
    plt.xlim( min(var) - offset, max(var) + offset)
    
    output_file  = '/home/shefali/Desktop/plots/butterflyscorewith' + str(ii) +'.png'
    plt.savefig(output_file)
    plt.show()


file = open('Sumdata.csv', 'r')

linessum = file.readlines()

arraysum = []

for line in linessum:
    arraysum.append(line.split(','))
    
arraysum.pop(0)
    
sumscore = (np.array(arraysum)).astype(int)
    
x = np.zeros( len(Brazeltoncase))

Brazelsumscore = np.column_stack([Brazeltoncase,x])

for ii in range(len(sumscore)):
        id  = sumscore[ii][0]
        a = np.where(Brazelsumscore [:,0] == id)[0]
        rank = sumscore[ii][3]
       
        if len(a) != 0:
            Brazelsumscore[a[0]][-1] = rank
            


Sumrank = Brazelsumscore[:,-1]

for ii in range(1,50):
    var = Brazelsumscore[:,ii]
    if ii == 11:
       ii = ii + 1 
    elif ii == 38 :
       ii = ii + 1
    elif ii == 41 :
       ii = ii + 1
    elif ii == 44 :
       ii = ii + 1
    elif ii == 45:
       ii = ii + 1
    elif ii == 47:
       ii = ii + 1
    else:
        m, b = np.polyfit(var, Sumrank, 1)
        plt.plot( var, Sumrank , 'r*')
        plt.plot(var, m*var + b, '-')
        plt.xlabel(ii)
        plt.ylabel('IUGRSumscore')
        plt.ylim(min(Sumrank)-1, max(Sumrank) + 2)
        offset = (max(var) - min(var))/len(var) 
        plt.xlim( min(var) - offset, max(var) + offset)
        
        output_file  = '/home/shefali/Desktop/plotsum/sumscorewith' + str(ii) +'.png'
        plt.savefig(output_file)
        plt.show()



for ii in range(51,90):
    var = Brazelsumscore[:,ii]
   
    m, b = np.polyfit(var, Sumrank, 1)
    plt.plot( var, Sumrank , 'r*')
    plt.plot(var, m*var + b, '-')
    plt.xlabel(ii)
    plt.ylabel('IUGRSumscore')
    plt.ylim(min(Sumrank)-1, max(Sumrank) + 2)
    offset = (max(var) - min(var))/len(var) 
    plt.xlim( min(var) - offset, max(var) + offset)
    
    output_file  = '/home/shefali/Desktop/plotsum/sumscorewith' + str(ii) +'.png'
    plt.savefig(output_file)
    plt.show()


for ii in range(91,102):
    var = Brazelsumscore[:,ii]
   
    m, b = np.polyfit(var, Sumrank, 1)
    plt.plot( var, Sumrank , 'r*')
    plt.plot(var, m*var + b, '-')
    plt.xlabel(ii)
    plt.ylabel('IUGRSumscore')
    plt.ylim(min(Sumrank)-1, max(Sumrank) + 2)
    offset = (max(var) - min(var))/len(var) 
    plt.xlim( min(var) - offset, max(var) + offset)
    
    output_file  = '/home/shefali/Desktop/plotsum/sumscorewith' + str(ii) +'.png'
    plt.savefig(output_file)
    plt.show()


file = open('Brazelton.csv', 'r')

lines = file.readlines()

array = []


for line in lines:
    array.append(line.split(','))
    
array.pop(0)
array.pop(0)
    
Brazeltonav = (np.array(array)).astype(float)

Av = Brazeltonav[:,[0,1,-1]]

x = np.zeros(len(Av))

Avbr = np.column_stack([Av,x])

for ii in range(len(butterflyscore)):
        id  = butterflyscore[ii][0]
        a = np.where((Avbr[:,0] == id) & (Avbr[:,1] == 1)) [0]
        average = (butterflyscore[ii][1] + butterflyscore[ii][1])/2.0 
       
        if len(a) != 0:
            Avbr[a[0]][-1] = average
            
Avbr_score = Avbr[:,-2]
Butscore = Avbr[:,-1]


m, b = np.polyfit(Avbr_score ,Butscore, 1)
plt.plot(Avbr_score, m*Avbr_score + b, '-')
plt.plot(Avbr_score ,Butscore, 'r*')
        
        
x = np.zeros(len(Avbr))

Avbrsum = np.column_stack([Avbr,x])

for ii in range(len(sumscore)):
        id  = sumscore[ii][0]
        a = np.where(Avbrsum[:,0] == id)[0]
        rank = sumscore[ii][3]
       
        if len(a) != 0:
           Avbrsum[a[0]][-1] = rank

Avbr_score = Avbr[:,-2]
Sumscore = Avbr[:,-1]


m, b = np.polyfit(Avbr_score ,Sumscore, 1)
plt.plot(Avbr_score, m*Avbr_score + b, '-')
plt.plot(Avbr_score ,Sumscore, 'r*')


#a = np.array([1,2,3,0,6])

#for i in a :
    #try :
        #print 3/i
        #break
        #print str(i)  + 'done'
    #except:
        #print 'Not done'
        

    try:
        x = int(raw_input("Please enter a number: "))
        break
        print 'yay'
    except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        
        
        
        
    


