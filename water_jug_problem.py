def fill_jug():
    max=(4,3)
    stack=[]
    visited=[]
    stack.append((0,0))
    while stack:
        x,y=stack.pop()
        if (x,y) not in visited:
             visited.append((x,y))
             #Fill Jug1
             if (max[0],y) not in visited:
                    stack.append((max[0],y) )
             #
             if (x,max[1]) not in visited:
                 stack.append((x,max[1]) )
             if (0,y) not in visited:
                 stack.append((0,y)) 
             if (x,0) not in visited:
                 stack.append((x,0)) 
             amount=min(x,max[1]-y)
             if amount>0:
                 stack.append((x-amount,y+amount))
             amount=min(y,max[0]-x)
             if amount>0:
                 stack.append((x+amount,y-amount))
    return visited
print(fill_jug())
