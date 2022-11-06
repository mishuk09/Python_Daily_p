
def maximum(x,y,z):

    if x > y or x > z:
        return x
    elif y > x or y > z :
        return y
    else:
        return z

result= maximum(1, 20,300)

print(result)