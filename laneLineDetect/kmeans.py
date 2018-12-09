from numpy import *
import copy

'''
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat
'''
    
#Eucilid distance
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


#random k cent    
def randCent(dataSet, k):
    n = shape(dataSet)[2]
    centroids = zeros((k,1,n))
    for j in range(n):
        minJ = min(dataSet[:,0,j])
        rangeJ = float(max(array(dataSet)[:,0,j]) - minJ)
        centroids[:,0,j] = minJ + rangeJ * random.rand(k)
    return centroids

def firstKCent(dataSet,k):
    return copy.deepcopy(dataSet[0:k])
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(0,m):
            dist=sum((centroids[:,0,:]-dataSet[i,0,:])**2,axis=1)
            
            minDist,minIndex=min(dist),argmin(dist)
            if clusterAssment[i,0] != minIndex: 
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist
        
        for cent in range(0,k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,0,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment

'''
def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt  
    numSamples, dim = dataSet.shape  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in xrange(numSamples):  
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show()
'''

def main(dataMat):
    K=2
    myCentroids, clustAssing= kMeans(dataMat,K)
    return myCentroids
    #show(dataMat, K, myCentroids, clustAssing)  
    
    
if __name__ == '__main__':
    #dataMat = mat(loadDataSet('testSet.txt'))
    dataMat=array([[[0,1]],[[1,0]],[[99,100]],[[100,99]]],dtype="float")
    result=main(dataMat)
    print "result: \n",result
