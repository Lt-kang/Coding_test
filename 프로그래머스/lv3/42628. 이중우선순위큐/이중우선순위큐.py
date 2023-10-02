import heapq as hq
def change_hq(l):
    l = [-i for i in l]
    hq.heapify(l)
    return l


def solution(op):
    h = []
    for i in op:
        if i[0]=="I":
            hq.heappush(h, int(i[1:]))
        if i=="D 1" and h:
            h = change_hq(h)
            hq.heappop(h)
            h = change_hq(h)
        if i=="D -1" and h:
            hq.heappop(h)

    return [max(h),min(h)] if h else [0,0]