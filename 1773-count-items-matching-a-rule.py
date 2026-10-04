class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        for i in range(len(items)):
            current_item=items[i]
            if ruleKey=="type" and current_item[0]==ruleValue:
                count+=1
            elif ruleKey=="color" and current_item[1]==ruleValue:
                count+=1
            elif ruleKey=="name" and current_item[2]==ruleValue:
                count+=1
        return count