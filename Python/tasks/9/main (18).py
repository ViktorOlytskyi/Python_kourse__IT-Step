
n = 8
rx = [0 for _ in range(n *n)]
ry = [0 for _ in range(n *n)]

def exist(x, y, s):
    global rx
    global ry
    for i in range(s):
        if rx[i]==x and ry[i]==y:
            return True
        else:
            return False

def f(s):
    if s+1>=n *n:
        return True

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx)+abs(dy)!=3:
                continue

            xn = rx[s]+dx
            yn = ry[s]+dy
            if xn < 1 or xn > n or yn < 1 or yn > n:
                continue

            if exist(xn,yn,s):
                continue

            rx[s+1]=xn
            ry[s+1]=yn
            if f(s+1):
                return True
    return False



def main():
    rx[0] = int(input("input coordinate x: "))
    rx[0] = int(input("input coordinate y: "))
    # rx[0] = 2
    # ry[0] = 3
    if f(0):
        i = 0
        print("Possible moves: ")
        while i<n *n:
            print(f"({rx[i]},{ry[i]})", end = ',')
            i += 1
    else:
        print("There is no possible moves\n", end = '')

if __name__ == "__main__":
    main()






