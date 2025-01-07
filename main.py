def pawn(x1, y1, x2, y2):
    return y2-y1==1 and abs(x2-x1)==1

print(pawn(x1=1, y1=1, x2=2, y2=2))