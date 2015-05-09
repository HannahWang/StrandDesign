import sys

strands = []
num_strands = 0

def readDNAfile(filename):
    f = open(filename,'r')
    line = f.readline()
    num_strands = int(line.strip())

    print "====Reading the strands====="
    for i in range(num_strands):
        len_strand = int(f.readline().strip().split()[0])
        f_strand = f.readline().strip()
        b_strand = f.readline().strip()
        strands.append((f_strand,b_strand))
        print "Lenth of Strand:%d Strand:(%s,%s)"%(len_strand,f_strand,b_strand)

def calCost(num_strands):

    for i in range(0,num_strands):
        for j in range(0,num_of_)

def calInteractCost(strand1,strand2,costTypes):

    #Type1: Max Subseq-complement Cost
    print "calculating!"

def calInStrandCost(strand,costTypes):

    #Type1: AT Cost
    #Type2: CG Content Cost
    #Type3: No "CCCC" cost




readDNAfile('strandfile/dna_01.sd')
