# get the maximum area from the given contours

def getmaxfun(mdict_area, mdict_cnt):
    max_area = max(mdict_area)
    print('Max_area - ', max_area)
    maxiarea_index = mdict_area.index(max(mdict_area))
    currentcontour = mdict_cnt[maxiarea_index]
    return currentcontour
