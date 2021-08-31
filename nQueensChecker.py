# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN chessboard such that no two queens are attacking each other. For most values of N, there are many ways to solve this problem. Here, you will write the function nQueensChecker(board) that takes a 2d list of booleans where True indicates a queen is present and False indicates a blank cell, and returns True if this NxN board contains N queens all of which do not attack any others, and False otherwise.

def nQueensChecker(a):
    # Your code goes here...
    l=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]==True:
                l.append((i,j))
    # print(l)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            qr=l[i][0]
            qc=l[i][1]
            Or=l[j][0]
            Oc=l[j][1]
            if canqueenattack(qr,qc,Or,Oc)==True:
                return False
    return True

                




def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if qR==oR:
		return True
	if qC==oC:
		return True
	qrc=int(str(qR)+ str(qC))
	orc=int(str(oR)+str(oC))
	r=abs(qrc-orc)
	if r%11 == 0 :
		return True
	return False


a=[[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]]

print(nQueensChecker(a))
