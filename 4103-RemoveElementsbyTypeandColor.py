class Solution(object):
    def canRemoveAll(self, types, colors, groupSize):
        typeArray=[]
        color=[]
        count=[]
        for i in range(len(types)):
            currentType=types[i]
            currentColor=colors[i]
            isSame=False

            if len(typeArray)>0:
                typeTop=typeArray[-1]
                colorType=color[-1]
                if typeTop==currentType and colorType==currentColor:
                    isSame=True

            if isSame==True:
                count[-1]=count[-1]+1  
            else:
                typeArray.append(currentType)
                color.append(currentColor)
                count.append(1)

            if count[-1]==groupSize[currentType]:
                typeArray.pop()
                color.pop()
                count.pop()

        if len(typeArray)==0:
            return True
        return False