def maxArea(height):
    """THis is the brute force method now I need to do the two pointer method so that the time complexity wil be o(N)"""
    max=0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            width=j-i
            height1=min(height[i],height[j])
            area=width*height1
            if area>=max:
                max=area
    print(max)
# maxArea( height = [1,8,6,2,5,4,8,3,7])
def maxARea1(height):
    i=0
    j=len(height)-1
    max_area=0
    while i < j:
            width=j-i
            height1=min(height[i],height[j])
            area=width*height1
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
            if area > max_area:
                max_area=area
    return max_area
print(maxARea1(height = [1,8,6,2,5,4,8,3,7]))


