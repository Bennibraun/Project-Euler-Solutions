

def findTriangles(p):
    triangles = []
    for i in range(1,int(p/2)):
        a = i
        for j in range(1,p-a):
            b = j
            c = p-a-b
            if c < a or c < b:
                break
            if a**2 + b**2 == c**2:
                # print(p,a,b,c)
                triangles.append([a,b,c])
    # print(p,triangles)
    return triangles

max_p = 0
max_solutions = 0
for i in range(1,1000):
    num_solutions = len(findTriangles(i))/2
    if num_solutions > max_solutions:
        max_solutions = num_solutions
        max_p = i

print(max_p)
print(max_solutions)