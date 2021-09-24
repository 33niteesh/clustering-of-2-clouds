import numpy as np
import random as r
from matplotlib import  pyplot
def clusters(list):
    l1=[]
    l2=[]
    list.sort()
    m1=r.randint(list[0],list[-len(list)//2])
    m2=r.randint(list[len(list)//2],list[-1])
    for i in range(0,len(list)):
        d1=abs(list[i]-m1)
        d2=abs(list[i]-m2)
        if d1>d2:
            l2.append(list[i])
        else:
            l1.append(list[i])
    l1=(np.array(l1))
    l2=(np.array(l2))
    while(m1!=round(np.mean(l1)) and m2!=round(np.mean(l2))):
        print(m1,m2)
        m1=round(np.mean(l1))
        m2=round(np.mean(l2))
        for i in range(0,len(list)):
            d1=abs(list[i]-m1)
            d2=abs(list[i]-m2)
            if d1>d2:
                np.append(l2,list[i])
            else:
                np.append(l1,list[i])
    print("two clusters are:",l1,l2)
    df,kr=len(l1),len(l2)
    x_ax=[]
    y_ax=np.array(l1)
    for i in range(len(l1)):
        x_ax.append(i)
    pyplot.scatter(x_ax,y_ax,marker="o",color='green')
    x_ax=[]
    y_ax=np.array(l2)
    for i in range(len(l2)):
        x_ax.append(i)
    mean_l1=(sum(l1)/len(l1))
    mean_l2=(sum(l2)/len(l2))
    print('means of cluster 1,2:',mean_l1,mean_l2)
    p_x1=[len(l1)/2]
    p_y1=[mean_l1]
    pyplot.scatter(p_x1,p_y1,marker=".",s=300)
    p_x2=[len(l2)/2]
    p_y2=[mean_l2]
    mid_x=[(len(l1)/2+len(l2)/2)/2]
    mid_y=[(mean_l1+mean_l2)/2]
    per_x=[p_x1,p_x2]
    per_y=[p_y1,p_y2]
    slope=abs((mean_l2-mean_l1)/(len(l2)/2-len(l1)/2))
    c=mid_y/(slope*((len(l1)/2+len(l2)/2)/2))
    print('Line that devides two clusters')
    print('y=',slope,'*(x)+',c[0])
    mid_x1=[(len(l1)/2+len(l2)/2)/2,0]
    mid_y1=[(mean_l1+mean_l2)/2,c[0]]
    pyplot.plot(mid_x,mid_y)
    pyplot.plot(mid_x1,mid_y1)
    pyplot.scatter(mid_x,mid_y,marker="o",color='pink',s=500)
    pyplot.scatter(p_x2,p_y2,marker=".",s=300)
    pyplot.scatter(x_ax,y_ax,marker="*",color='red')
    pyplot.show()
    return ''
n=[1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 10, 12, 14, 15, 16, 17, 18, 20, 30, 40, 50, 55, 60, 60, 66, 67, 70, 70, 77, 77, 78, 79, 80, 80, 80, 80, 80, 81, 81, 82, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 121, 123, 124, 150, 160, 200, 1001, 
1002, 1003, 1003, 1004, 1005, 1009, 1020, 1030, 1030, 1031, 1042, 1070, 1080, 1090, 1092, 1092, 1093, 1094, 1097, 1098, 1100, 1109, 1111, 1111, 1121, 1122, 1123, 1131, 1143, 1211, 1213, 1216, 1221, 1232, 1232, 1234, 1243, 1243, 1265, 1287, 1290, 1321, 1321]
print(clusters(n))
