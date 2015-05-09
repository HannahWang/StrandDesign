import sys

strands = []
number_of_strands = 0

def readDNAfile(filename):
    f = open(filename,'r')
    line = f.readline()
    num_strands = int(line.strip())
    s = []

    print "====Reading the strands====="
    for i in range(num_strands):
        len_strand = int(f.readline().strip().split()[0])
        f_strand = f.readline().strip()
        b_strand = f.readline().strip()
        s.append((f_strand,b_strand))
        print "Lenth of Strand:%d ||| Strand:(%s,%s)"%(len_strand,f_strand,b_strand)

    return num_strands ,s

def calCost(num_strands,s):

    total_cost = 0.
    print "NUM_STRNADS: %d"%(num_strands)
    ## calInteractCost
    ## calInStrandCost
    for i in range(num_strands):
        total_cost += calInStrandCost(s[i],[True,False,False])
    return total_cost

def calInteractCost(strand1,strand2,costTypes):

    #Type1: Max Subseq-complement Cost
    print "calculating!"
    return

def calInStrandCost(strand,costTypes):

    #Type1: AT Cost
    #Type2: CG Content Cost
    #Type3: No "CCCC" cost
    weight =[1. ,1. ,1.]
    total_cost = 0.


    if costTypes[0] == True:
        count = 0
        total_cost += weight[0]*countATCostofOneSide(strand[0])
        total_cost += weight[0]*countATCostofOneSide(strand[1])
    #elif costTypes[1] == True:
    #elif costTypes[2] == True:

    return total_cost




##### calCost Helper function  #####

def countATCostofOneSide(strand_oneside):
    cost = 0.
    count = 0.
    AT_threshold = 5
    length = len(strand_oneside)

    for i in range(length):
        if strand_oneside[i] == ("A" or "T"):
            count = count +1
            if i == (length-1):
                if(count >= AT_threshold):
                    cost += (count /length)
        else :
            if(count >= AT_threshold):
                cost += (count/ length)
                count = 0

    return cost




number_of_strands, strands = readDNAfile('strandfile/dna_01.sd')
cost = calCost(number_of_strands, strands)
print "Total Cost: %f"%(cost)
