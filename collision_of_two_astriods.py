def asteroidCollision(asteroids):
    stack=[asteroids[0]]
    ho_gya=False
    for i in range(1,len(asteroids)):
        if stack==[]:
            stack=[asteroids[i]]
            continue
        curr=asteroids[i]
        while stack!=[]:
            prev=stack.pop()
            if curr<0 and prev>0:
                # print("uau")
                if abs(curr)> abs(prev):
                    ho_gya=True
                    # stack.append(curr)
                    continue
                elif abs(prev)> abs(curr):
                    stack.append(prev)
                    ho_gya=False
                    break
                    # curr=prev
                elif abs(prev)==abs(curr):
                    ho_gya=False
                    break
                    # stack.append(prev)
                    # stack.append(curr)
            # elif curr>0 and prev>0:
            else:
                print("aida")
                ho_gya=False
                stack.append(prev)
                stack.append(curr)
                break
        if ho_gya:
            stack.append(curr)
    return stack


# asteroidCollision([5,10,-5])
# asteroidCollision([8,-8])
# asteroidCollision([1,2,3,4,5,-10])
# asteroidCollision([-2,-1])
# asteroidCollision([10,2,-5])
# stack.append(curr)
print(asteroidCollision([1,-1,-2,-2]))
