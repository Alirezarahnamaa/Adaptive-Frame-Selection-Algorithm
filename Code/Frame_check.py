def Algoritm(frameOne, frameTwo):
    cMul = 2.0*frameOne * frameTwo
    cPow = np.sqrt(pow(frameOne, 2.0)+pow(frameTwo, 2.0))
    cDivid = np.divide(cMul, cPow, where=(cMul != 0) | (cPow != 0))
    cMean = np.mean(cDivid)
    
    return float("{:.4f}".format(cMean))

def FrameCheck(Video):
    finalFrame = []
    frameLenght = len(Video)

    finalFrame.append(np.asarray(Video[0]))
    tempFrame = finalFrame[0]
    tempResult = []
    tempResult.append(Algoritm(tempFrame, Video[1]))

    for frameIndex in range(2, frameLenght-1):
        algoritmResult = Algoritm(tempFrame, Video[frameIndex])
        if np.mean(tempResult) > algoritmResult:
        #if np.mean(tempResult[-10:]) > algoritmResult:
            finalFrame.append(np.asarray(Video[frameIndex]))
            tempFrame = Video[frameIndex]
            tempResult.append(algoritmResult)

    print('mean: '+str(np.mean(tempResult)))
    print(str(frameLenght-len(finalFrame))+' frams is removed')

    return finalFrame
