def _get_temp():
    My_list = []
    x = int(input("Press 1 to continue or 0 to terminate: "))
    while(x!=0):
        x=int(input("Put your temperatures"))
        if(x!=0):
            My_list.append(x)
    return My_list

def _avg_temp(x):
    count = len(x)
    y = sum(x)  
    avg = y / count
    return avg

def calc_min_max_temp(x):
    y = max(x)
    print("Therefore the max temp is = " + str(y))
    z = min(x)
    print("Therefore the min temp is = " + str(z))
    c = [y, z]
    return c
def calculation_median(x):
    count=0
    for i in x:
        count =count +1
    f=int((count -1)/2)
    g=x[f]
    return g    
def main():
    x = _get_temp()
    y = _avg_temp(x)
    print("Average temperature =", y)
    print(calc_min_max_temp(x))
    z=calculation_median(x)
    print(z)

if __name__ == "__main__":
    main()
