if __name__ == '__main__':
    min,secmin=10000.0,10000.0
    a=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())

        result=[]
        a.append([name,score])
        if score < min:
            secmin=min
            min=score

        elif min < score <=secmin:
            secmin=score
    for i in range(len(a)):
        if a[i][1]==secmin:
            result.append(a[i][0])
    print ('\n'.join(sorted(result)))