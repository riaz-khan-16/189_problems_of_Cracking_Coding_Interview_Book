
import heapq
def kClosest(points, k):
        heap=[]
        for i in points:
            x=i[0]
            y=i[1]
            d=(x**2)+(y**2)
            heap.append([d,x,y])
        heapq.heapify(heap)
        result=[]
        for i in range(k):
            d,x,y=heapq.heappop(heap)
            result.append([x,y])
        return result    