def hfr(p):
    sum=0
    hsum=0
    for k in range(1,4):
        for l in range(1,4):
            hsum+=p[k][l]
    for k in  range(5,8):
        for l in range(5,8):
            sum+=p[k][l]
    hfrval=hsum/sum
    return hfrval