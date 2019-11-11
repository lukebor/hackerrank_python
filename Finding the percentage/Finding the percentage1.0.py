if __name__ == '__main__':
    n = int(input())
    x=0.0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=sum(student_marks[query_name])/len(student_marks[query_name])
    print("%.2f" % x)