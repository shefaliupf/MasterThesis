import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rankdata
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr

control_babies = [55, 35, 91, 90, 115, 74, 87, 110, 11, 103, 107, 116, 124, 132]
case_babies = [70,82,15,97,101,125,128,131,138,142]



def dataScoreDisjunction( filename = 'Disjunction.csv', case = 1, case_babies = case_babies, control_babies = control_babies):
    
    """ 
    case = 1 for case, case = 0 for control data, case = 1 for all data
    Subtracts the time,shifts in x and shifts in seconds between Incoherent and coherent conditions
    Returns 
    """
    
    file = open(filename, 'r')
    lines = file.readlines()
    array = []
    for line in lines:
        array.append(line.split(','))
    
    # Taking the headers out 
    headers = array.pop(0)
    
    
    # Converting it to numpy array
    array = np.array(array)
    
    # Separating the Incoherent with coherent condition
    condI = array[ array[:,1] == 'I']
    condC = array[array[:,1] == 'C']
    
    
    # Making a new array for output data 
    arraydif = ['BabyId', 'Timedif','Shiftxtrail', 'Shiftxsecond']
    arraydif = np.array(arraydif)
    
    for ii in condC[:,0]:
        
        # Subtracting the information for the two conditions
        
        timeC = (condC[np.where(condC == ii)[0], 2][0])
        timeI = (condI[np.where(condI == ii)[0], 2][0])
        
        trailshiftC = (condC[np.where(condC == ii)[0], 3][0])
        trailshiftI = (condI[np.where(condI == ii)[0], 3][0])
        
        secondshiftC = (condC[np.where(condC == ii)[0], 4][0])
        secondshiftI= (condI[np.where(condI == ii)[0], 4][0])
        
        if timeC != '':
            if timeI != '':
                
                time = (float(timeI) - float(timeC))
                trailshift = (float(trailshiftI) - float(trailshiftC))
                secondshift = ( float(secondshiftI) - float(secondshiftC))
                arraydif = np.vstack([arraydif,[ii,time,trailshift,secondshift]])
                
        else:
            pass
    
   
    arraydifdata = np.delete(arraydif, [0], axis = 0)
    
    arraydifdata = np.array(arraydifdata).astype(float)
    
    rank = rankdata( arraydifdata[:,1])

    arraydifscore = np.column_stack([arraydifdata, rank])
    headers = np.array(['Baby_id', 'timedif','Shiftxtrail', 'Shiftxsecond','Score']) 

    if case == -1:
        print ' This is data for all babies'    
        return headers, arraydifscore
    else:
        if case == 1:
            print ' This is data for case babies'   
            babies = case_babies
        elif case == 0:
            print ' This is data for control babies'   
            babies = control_babies
        
        arraydif = np.array(['Baby_id', 'timedif','Shiftxtrail', 'Shiftxsecond','Score'])
        
        for ii in babies:
            jj = np.where(arraydifscore[:,0] == ii)[0]
              
            arraydif = np.vstack([arraydif, arraydifscore[jj]])
        
        headers = arraydif[0]
        disdata = np.array(arraydif[1:]).astype(float)

        
        return headers, disdata
    
   

    #if case == 0 :
        #timedifcontrol = np.array(['Baby_id', 'timedif','Shiftxtrail', 'Shiftxsecond','Score'])
        #for ii in control_babies:
            #jj = np.where(timedifscore[:,0] == ii)[0]
            
            #timedifcontrol = np.vstack([timedifcontrol, timedifscore[jj]])
        
        #return timedifcontrol
    
    #if case == -1:
        
       
        
        
        
        
    
def dataScoreButterfly( filename = 'Butterfly.csv', case = 1, case_babies = case_babies, control_babies = control_babies):
    
    """
    Data for level and proportion of looking time for butterfly
    Default returns case, case == 0 returns control and case == -1 returns all babies
    Returns headers(string), butterflyscore(float)
    """
    
    
    file = open(filename, 'r')
    lines = file.readlines()
    array = []
    for line in lines:
        array.append(line.split(','))
    
    headers = array.pop(0)
    
    data = np.array(array).astype(float)

    ranktemp = rankdata(data[:,2])
    
    rank1 = max(ranktemp) - ranktemp
    
    rank2temp = rankdata(data[:,1])
    
    rank2 = max(rank2temp) - rank2temp
    
    butterflyscore = np.column_stack( [data, rank1, rank2])
    
    
    if case == -1:
        print 'This is data for control babies'
        return headers, butterflyscore
    else:
        if case == 1:
            babies = case_babies
        else:
            babies = control_babies
            
        butscore = np.array(['Baby_id', 'Level','Time','Score1', 'Score2'])
        for ii in babies:
            
            jj = np.where(butterflyscore[:,0] == ii)[0]
        
            butscore = np.vstack([butscore, butterflyscore[jj]])
    
        headers = butscore[0]
        data = np.array(butscore[1:]).astype(float)
    return headers, data
        


def getScoreMatrix(case = 1):
    

    butscore = dataScoreButterfly(case = case)[1]
    #butscore = np.delete(butterflydata, [0], axis = 0) 
    #butscore = np.array(butterflydata).astype(float)
    disscore = dataScoreDisjunction(case = case)[1]
    #disscore = np.delete(disjunctiondata, [0], axis = 0) 
    #disscore = np.array(disscore).astype(float)
    
    scorematrix = np.array( ['Baby_Id', 'Butterflyscore1', 'Butterflyscore2' , 'Disjunctiontimedif', 'DisjunctionShifttrail', 'DisShiftseconds', 'Butterflyrank1', 'Butterflyrank2', 'Disjunctionrank1'])
    
     
   
    for ii in butscore[:,0] :
        jj = np.where(disscore[:,0] == ii)[0]
        kk = np.where(butscore[:,0] == ii)[0]
       
    
        if len(jj) > 0:
            scorematrix = np.vstack([scorematrix,[ii, butscore[kk,1], butscore[kk,2],disscore[jj, 1],disscore[jj, 2],disscore[jj, 3],butscore[kk,3],butscore[kk,4],disscore[jj, 2]]])
            
    return scorematrix
    
    

def plotScoreMatrix(scorematrix, column1 = 'Butterflyscore1' , column2 = 'DisjunctionScore', case = 1):
    
    headers = scorematrix[0]
    score = np.delete(scorematrix,[0], axis = 0)
    
    score = np.array(score).astype(float)
    x = score[:,1]
    y = score[:,3]
    
     
   
    return x,y
    """
    spearmanr(x,y)
    SpearmanrResult(correlation=0.7142857142857143, pvalue=0.046528232284167283)
    scorematrix = np.vstack([scorematrix,[ii, butscore[kk,2], butscore[kk,1],disscore[jj, 1]]])
    spearmanr(x,y)
    SpearmanrResult(correlation=-0.7142857142857143, pvalue=0.046528232284167283)
    """
    a, b = pearsonr(x,y)
    print a,b
    plt.plot(x,y,'r*')
    m, b = np.polyfit(x, y, 1)
    plt.plot( x,m*x + b, '-')
    plt.xlim(-5,25)
    plt.ylim(-5,25)
    
    plt.show()
    


def getBrazeltonData( filename = 'test2.csv', case = 1, case_babies = case_babies, control_babies = control_babies):
    
    
    
    headerstemp, b = dataArray(filename)
    headers = np.array(headerstemp)
    brazeltondata = np.array(range(len(b[0])))
    
    
    for ii in range(1,len(b)):
        temp = np.array(b[ii]).astype(float)
        brazeltondata = np.vstack([brazeltondata, temp])

        
    
    
    indcase = np.where(brazeltondata[:,1] == 1)
    indcontrol = np.where(brazeltondata[:,1] == 0)
    
    if case == 1:
        return headers, brazeltondata[indcase]
    elif case == 0:
        return headers, brazeltondata[indcontrol]
    else:
        return headers, brazeltondata
                
    
def dataArray( filename, header = 0):
    
    file = open(filename, 'r')

    lines = file.readlines()
    array = []

    for line in lines:
        array.append(line.split(','))

    for ii in range(header + 1):
        headers = array.pop(ii)
        
    data = array
   

    return headers, data





def getBrazelButMatrix(case = 1):
    
    butheaders,butdata = dataScoreButterfly( case = case)
    
    brazelheaders,brazelcase = getBrazeltonData( case = case)
    
    headerstemp = list(brazelheaders) + list(butheaders)
    headers = np.array(headerstemp)
    butbrazel = np.array(range(len(butdata[0]) + len(brazelcase[0])))
    
    butdata = np.array(butdata).astype(float)
    brazelcase = np.array(brazelcase).astype(float)
    for ii in brazelcase[1:,0]:
        jj = np.where(butdata[:,0] == ii)[0]
        kk = np.where(brazelcase[:,0] == ii)[0]
        if len(jj) != 0:
            temp = np.column_stack([brazelcase[kk], butdata[jj]])
            butbrazel = np.vstack([butbrazel,temp])

    return headers, butbrazel





def getBrazelDisMatrix(case = 1):
    
    
    disheaders, disdata = dataScoreDisjunction(case = case)
    brazeheaders,brazelcase = getBrazeltonData(case = case)
     
    headers =  list( brazeheaders) + list(disheaders) 
    headers = np.array(headers)
    disbrazel = np.array(range(len(disdata[0]) + len(brazelcase[0])))
    for ii in brazelcase[2:,0]:
        

        jj = np.where(disdata[:,0] == ii)[0]
        kk = np.where(brazelcase[:,0] == ii)[0]
        if len(jj) != 0:
            temp = np.column_stack([brazelcase[kk], disdata[jj]])
            disbrazel = np.vstack([disbrazel,temp])

    return headers,disbrazel[1:]





def plotButBrazel( number, folder = '31March', condition = 1):
        
    headers, butbrazelcase = getBrazelButMatrix(case = 1)
    headers, butbrazelcontrol = getBrazelButMatrix(case = 0)
    color = ['b', 'r']
    name = ['case', 'control']
    for ii in range(number,len(butbrazelcase[0])):
        if ii == 1:
           ii = ii+1
        elif ii == 2:
           ii = ii+1
      
        elif ii == 11:
            ii = ii + 1
        elif ii == 17:
            ii = ii + 1 
        elif ii == 38 :
            ii = ii + 1
        #elif ii == 40 :
            ii = ii + 1
        elif ii == 41 :
            ii = ii + 1
        elif ii == 44 :
            ii = ii + 1
        elif ii == 45:
            ii = ii + 1
        elif ii == 47:
            ii = ii + 1
        #elif ii == 49:
            ii = ii + 1
        #elif ii == 86:
            ii = ii + 1
        elif ii == 88:
            ii = ii + 1
        #elif ii == 90:
            ii = ii + 1
        elif ii == 95:
            ii = ii + 1
       
        else :
            print ii
            
            for jj in range(condition):
                if jj == 0:
                    butbrazel = butbrazelcase
                else :
                    butbrazel = butbrazelcontrol
                
                x = butbrazel[1:,ii]
                y = butbrazel[1:,-4]
                b = butbrazel[1:,0]
                maxx = np.max(x)
                minx = np.min(x)

                maxy = np.max(y)
                miny = np.min(y)

                offsetx = (maxx-minx)/(maxx + minx)
                offsety = (maxy- miny)/(maxy + miny)
                
                plt.hold(True)
                for xind in range(len(x)):
                    plt.scatter(x[xind],y[xind], color = color[jj])
                    plt.annotate(str(b[xind]),xy=(x[xind],y[xind]))
                
                coeff, p = pearsonr(x,y)
                
                label = ( name[jj] + ': rPearson coeff :' + str(coeff) + '   ' + 'p :' + str(p))
                m, b = np.polyfit(x, y, 1)
                plt.plot( x, m*x + b , '-', label = label, color = color[jj])
            
            
            
            plt.xlabel(header[ii])
            plt.ylabel('Butterfly-Level')
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)
            
        
            #plt.xlim(minx - offsetx, maxx + offsetx)
            #plt.ylim(miny - offsety, maxy + offsety)
        
            #if coeff >= .3 or coeff <= -.3 :
                    #if p <= .05:
                        #output_file  = '/home/shefali/Desktop/' + folder +'/Level/significantinteresting/'+headers[ii] + str(ii) +'.png'
                    #else : 
                        #output_file  = '/home/shefali/Desktop/' + folder + '/Level/interesting/'+headers[ii] + str(ii) +'.png'
            #else:
            output_file  = '/home/shefali/Desktop/'+ folder + '/Butterfly-Level'+ str(ii) +'.png'
            
            plt.savefig(output_file, bbox_inches='tight')
            plt.show()
            
            
            
            
            

def plotDiswthbut(name, condition = 2):
    
    acase = getScoreMatrix(case = 1)
    acontrol = getScoreMatrix(case = 0)
    color = ['b', 'r']
    case = ['case', 'control']
    for jj in range(condition):
        if jj == 0:
            a = acase
        if jj == 1:
            a = acontrol
    
        b = a[2:]
        b = np.array(b).astype(float)
        x = b[:,1]
        y = b[:,5]
        plt.hold(True)
        for xind in range(len(x)):
            plt.scatter(x[xind],y[xind], s = 10, color = color[jj])
            plt.annotate(str(b[xind][0]),xy=(x[xind],y[xind]))
        
        
        coeff, p = pearsonr(x,y)
        print coeff, p
        label = ( case[jj] + ': Pearson coeff :' + str(coeff) + '   ' + 'p :' + str(p))
        #plt.ylim(-15,12)
        m, b = np.polyfit(x, y, 1)
        plt.plot( x, m*x + b , '-', color = color[jj], label = label)
        
    plt.xlabel('Butterfly - Level', fontsize  = 20)
    plt.ylabel('Disjunction- Shiftsxseconds', fontsize = 20)
        
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)
    plt.savefig('/home/shefali/Desktop/31March/DisButCaseControl/' + name + '.png',bbox_inches='tight')
    plt.show()
        
   
   
   

def plotDisBrazel(number = 3, folder = 'temp', condition = 2):
    
    """
    This plots Brazelton data ( all rows) with Disjunction ( The difference data for shift trials, shift seconds,
    Timedif)
    
    
    """
    
    headerscase,disbrazelcase  = getBrazelDisMatrix(case = 1)
    headerscontrol,disbrazelcontrol = getBrazelDisMatrix(case = 0)
    headers = headerscase
    color = ['b', 'r']
    name = ['case', 'control']
    
    for ii in range(number,len(disbrazelcase[0])):
        if ii == 1:
            pass
        elif ii == 11:
            ii = ii + 1
        elif ii == 17:
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
        elif ii == 49:
            ii = ii + 1
        elif ii == 86:
            ii = ii + 1
        elif ii == 88:
            ii = ii + 1
        elif ii == 90:
            ii = ii + 1
        elif ii == 95:
            ii = ii + 1
        else :
            print ii
            
            for jj in range(condition):
                    if jj == 0:
                        disbrazel = disbrazelcase
                    else :
                        disbrazel = disbrazelcontrol
                    x = disbrazel[1:,ii]
                    y = disbrazel[1:,-3]
                    b = disbrazel[1:,0]
                    maxx = np.max(x)
                    minx = np.min(x)

                    maxy = np.max(y)
                    miny = np.min(y)

                    offsetx = (maxx-minx)/(maxx + minx)
                    offsety = (maxy- miny)/(maxy + miny)
                    
                    plt.hold(True)
                    for xind in range(len(x)):
                        plt.scatter(x[xind],y[xind], color = color[jj])
                        plt.annotate(str(b[xind]),xy=(x[xind],y[xind]))
                    
                    coeff, p = pearsonr(x,y)
                    print coeff, p
                    label = ( 'Pearson coeff :' + str(coeff) + '   ' + 'p :' + str(p))
                    m, c = np.polyfit(x, y, 1)
                    plt.plot( x, m*x + c , '-', color = color[jj],label = label )
                
        plt.xlabel(unicode(headers[ii]))
        plt.ylabel('Disjunction-CumulativeTimeDif')
        
        
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)
    
        output_file  = '/home/shefali/Desktop/31March/timedif/notinteresting/'+headers[ii] + str(ii) +'.png'
        plt.savefig(output_file,bbox_inches='tight')
        plt.show()






def plotIUGRsum():
    
    """
    This gets us the ranks of IUGR
    
    """
    
    a = dataArray('IUGRsum.csv')
    headers = a[0]
    dataIUGR = np.array(a[1:]).astype(float)
    scorematrix = getScoreMatrix()
    headersscore = scorematrix[0]
    datascore = np.array(scorematrix[2:]).astype(float)
    

    
    
def correlateData( filename1 = 'Brazelton.csv', filename2 = 'Analysis.csv', column_name1 = [], column_name2 = []):

    """ 
    This function correlates one data with the other, default with the brazelton file . If column names are not given, it does it for all the columns

    """
    
    headers1, data1 = dataArray(filename1)
    headers2, data2 = dataArray(filename2)


    ##if len(column_name1) == 0:
       ##if len(column_name2) == 0:
          
          ##for column1 in column_name1:
              ##for column2 in column_name2:
                   ##index1 = np.where(headers1 == column1)[0]
                   ##index2 = np.where(headers2 == column2)[0]
                   ##d1 = data1[ :, index1]
                   ##d2 = data2[ :, index2]
                   
                   ##corr, p = pearsonr(d1,d2)
