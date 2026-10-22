import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap=[]
        i=0
        while i+1<=len(heights)-1:
            current=heights[i]
            next_index=heights[i+1]
            if current>=next_index:
                i+=1
                continue
            left=next_index-current
            heapq.heappush(heap,-left)
            bricks-=left
            if bricks<0:
                if ladders==0:
                    return i
                biggest=-heapq.heappop(heap)
                bricks+=biggest
                ladders-=1
            i+=1
        return i