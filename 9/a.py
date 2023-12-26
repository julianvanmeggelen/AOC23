

if __name__ == "__main__":
    lines = open('input.txt').readlines()
    res = 0
    for line in lines:
        diffs = [[int(v) for v in line.split()]]
        while not all(_==0 for _ in diffs[-1]):
            diffs.append([a-b for a,b in zip(diffs[-1][1:], diffs[-1][:-1])])
        for i in range(len(diffs)-1, 0, -1):
            diffs[i-1].append(diffs[i-1][-1] + diffs[i][-1])
        res += diffs[0][-1]
    print(res)




  


    


     

