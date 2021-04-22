#Problem
#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest
#grade. If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line

#Solution

mainlist=[]
marklist=[]
n=int(input())
if __name__ == '__main__':
    for i in range(n):
        name = input()
        score = float(input())
        mainlist.append([name,score])
        marklist.append(score)
mainlist.sort()
# print(mainlist)
myset=set(marklist)
# print(myset)
marklist=list(myset)
marklist.sort(reverse=True)
# print(marklist)
for i in range(0,n):
    if (mainlist[i][1]==marklist[-2]):
        print (mainlist[i][0])
