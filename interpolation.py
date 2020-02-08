#interpolation module
#takes 2 two-dimensional points and interpolates for a point in between them
#author: shulkasr

def interpolate(two_dim_array,interpPoint):
    x1 = two_dim_array[0][0] if two_dim_array[0][0] <= two_dim_array[1][0] else two_dim_array[1][0]
    y1 = two_dim_array[0][1] if two_dim_array[0][0] <= two_dim_array[1][0] else two_dim_array[1][1]
    x2 = two_dim_array[1][0] if two_dim_array[0][0] <= two_dim_array[1][0] else two_dim_array[0][0]
    y2 = two_dim_array[1][1] if two_dim_array[0][0] <= two_dim_array[1][0] else two_dim_array[0][1]
    print "1:",x1,y1,"2:",x2,y2
    slope = (y2-y1)/(x2-x1)
    constant = (y1*x2-y2*x1)/(x2-x1)
    interPolatedPoint = slope*interpPoint + constant
    return interPolatedPoint

def findClosestPoints(windspeed_list,inputPoint):
    #assumes sorted windspeed_list
    if inputPoint < windspeed_list[0]:
        closest1 = -1
        closest2 = -1
    elif inputPoint > windspeed_list[-1]:
        closest1 = -1
        closest2 = -1
    else:
        closest1 = min(windspeed_list, key=lambda x:abs(x-inputPoint))
        if closest1==inputPoint:
            closest2 = closest1
        elif closest1 < inputPoint:
            closest2 = windspeed_list[windspeed_list.index(closest1)+1]
        elif closest1> inputPoint:
            closest2 = windspeed_list[windspeed_list.index(closest1)-1]
    return sorted([closest1,closest2])

    
    


if __name__ == '__main__':
    
   intPoint = interpolate([(21.4,5),(21,10)],21.1)
   print intPoint
   print findClosestPoints([0.5,1.0,1.5,2.0,2.5,3.0],4.25)
