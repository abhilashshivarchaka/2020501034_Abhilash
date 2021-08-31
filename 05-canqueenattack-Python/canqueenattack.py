# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

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

	pass