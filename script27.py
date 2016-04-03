headers, b = code.dataArray('test2.csv')

brazeltondata = np.array(range(len(b[0])))

for ii in range(1,len(b)):
    temp = np.array(b[ii]).astype(float)
    brazeltondata = np.vstack([brazeltondata, temp])
    
score = code.getScoreMatrix()

headers = score[0]

temp = score[2:]

scoredata = np.array(temp).astype(float)

headers, butdata = code.dataScoreButterfly()




butbrazel = np.array(range(len(butdata[0]) + len(brazelcase[0])))
for ii in brazelcase[2:,0]:
    
    
    jj = np.where(butdata[:,0] == ii)[0]
    if len(jj) != 0:
        temp = np.column_stack([brazelcase[ii], butdata[jj]])
        butbrazel = np.vstack([butbrazel,temp])

return butbrazel


a = code.getBrazelButMatrix(brazelcase,butdata)



plt.plot(brazelcase[1:,4], butdata[:,1], 'ro')
plt.xlim(minx - offsetx, maxx + offsetx)
plt.ylim(miny - offsety, maxy + offsety)


maxx = np.max(brazelcase[1:,4])
minx = np.min(brazelcase[1:,4])

maxy = np.max(butdata[:,1])
miny = np.min(butdata[:,1])

offsetx = (maxx-minx)/(maxx + minx)
offsety = (maxy- miny)/(maxy + miny)


x = disbrazel[1:,99]
y = disbrazel[1:,-4]
b = disbrazel[1:,0]
maxx = np.max(x)
minx = np.min(x)

maxy = np.max(y)
miny = np.min(y)

offsetx = (maxx-minx)/(maxx + minx)
offsety = (maxy- miny)/(maxy + miny)

plt.hold(True)
for xind in range(len(x)):
    plt.scatter(x[xind],y[xind])
    plt.annotate(str(b[xind]),xy=(x[xind],y[xind]))

coeff, p = pearsonr(x,y)
print coeff, p
label = ( 'Pearson coeff :' + str(coeff) + '   ' + 'p :' + str(p))
m, c = np.polyfit(x, y, 1)
plt.plot( x, m*x + c , '-', label = label)
#plt.xlabel(unicode(headers[ii]))
plt.ylabel('cumulativetimedif')


    a = code.dataArray('IUGRsum.csv')
    headers = a[0]
    data = np.array(a[2:]).astype(float)
    
    
brazheaders = code.getBrazeltonData( case = 0)[0]

brazcontroldata = code.getBrazeltonData( case = 0)[1]

brazcontroldata = np.array(brazcontroldata).astype(float)

headers = code.dataScoreButterfly(case = 0)[0]



butcontroldata = code.dataScoreButterfly(case = 0)

butcontroldata = np.array(butcontroldata).astype(float)


headers, butbrazelcase = code.getBrazelButMatrix(case = 1)
headers, butbrazelcontrol = code.getBrazelButMatrix(case = 0)
y = butbrazelcase[:,4]
x = butbrazelcase[:,-3]
m, c = np.polyfit(x, y, 1)

X = range(2)
plt.plot(x,y,'r*')
label = 'shefali'
plt.plot( X, m*X + c , '-', label = label)

plt.xlim(0, 1)

x = [1,2]
plt.plot( x, 3*x + 2, '-')


disbrazel = code.getBrazelDisMatrix(case = 1)

brazeldata = code.getBrazeltonData( case = 1)


brazeldata = code.getBrazeltonData( case = -1)[1]
brazeldata = np.delete(brazeldata,[0], axis = 0)

b = brazeldata.argsort(axis=0).argsort(axis=0) + 1

for ii in range(len(brazeldata[:,0])):
    plt.hist(b[ii])
    
    outputfile = '/home/shefali/Desktop/31March/BabyID/' + str(brazeldata[:,0][ii]) + '.png'
    plt.savefig(outputfile)
    plt.show()
    
