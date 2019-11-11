import re
if __name__ == '__main__':
    sum=0
    S=[]
    sword=[]
    t = int(input())
    for t_itr in range(t):
        S.append(input())
    t1=int(input())
    for t_itr in range(t1):
        sword.append(input())
    for i in range(t1):
        for j in range(t):
            sum+=(len(re.findall(r'^\W?'+sword[i]+r'\W',S[j])))
        print(sum);sum=0