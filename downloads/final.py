import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry.polygon import LinearRing, Polygon
from descartes import PolygonPatch
import math
import itertools
import sys

totalDistance=0

def visualiseObstacles(number):
    """
    This function plots the obstacles.

    Input: number - workspace number

    Output: None
    """
    # Workspace 1
    W1O0=Polygon([(1,1),(2,1),(2,5),(1,5)])
    W1O1=Polygon([(3,4),(4,4),(4,12),(3,12)])
    W1O2=Polygon([(3,12),(12,12),(12,13),(3,13)])
    W1O3=Polygon([(12,5),(13,5),(13,13),(12,13)])
    W1O4=Polygon([(6,5),(12,5),(12,6),(6,6)])
    Workspace1=[W1O0,W1O1,W1O2,W1O3,W1O4]
    # Workspace 2
    W2O0=Polygon([(-6,-6),(25,-6),(25,-5),(-6,-5)])
    W2O1=Polygon([(-6,5),(30,5),(30,6),(-6,6)])
    W2O2=Polygon([(-6,-5),(-5,-5),(-5,5),(-6,5)])
    W2O3=Polygon([(4,-5),(5,-5),(5,1),(4,1)])
    W2O4=Polygon([(9,0),(10,0),(10,5),(9,5)])
    W2O5=Polygon([(14,-5),(15,-5),(15,1),(14,1)])
    W2O6=Polygon([(19,0),(20,0),(20,5),(19,5)])
    W2O7=Polygon([(24,-5),(25,-5),(25,1),(24,1)])
    W2O8=Polygon([(29,0),(30,0),(30,5),(29,5)])
    Workspace2=[W2O0,W2O1,W2O2,W2O3,W2O4,W2O5,W2O6,W2O7,W2O8]
    if number==1:
        fig = plt.figure(1, figsize=(15,15), dpi=90)
        ax = fig.add_subplot(111)
        for i in range(len(Workspace1)):
            x,y=Workspace1[i].exterior.xy
            ax.plot(x,y,color=(0.67,0.85,0.90))
            ring_patch = PolygonPatch(Workspace1[i],color=(0.67,0.85,0.90))
            ax.add_patch(ring_patch)
            pass
        ax.plot(0,0,'ro')
        ax.plot(10,10,'go')
    elif number==2:
        fig = plt.figure(1, figsize=(45,45), dpi=90)
        ax = fig.add_subplot(111)
        for i in range(len(Workspace2)):
            x,y=Workspace2[i].exterior.xy
            ax.plot(x,y,color=(0.67,0.85,0.90))
            ring_patch = PolygonPatch(Workspace2[i],color=(0.67,0.85,0.90))
            ax.add_patch(ring_patch)
            pass
        ax.plot(0,0,'ro')
        ax.plot(35,0,'go')

def calculateDistance(x1,y1,x2,y2):
    """
    This function calculates the distance between two points.

    Input: x1 - x coordinate of one point
           y1 - y coordinate of one point
           x2 - x coordinate of other point
           y2 - y coordinate of other point

    Output: dist - distance between two points
    """
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  

def followM(xstart,ystart):
    """
    This function plots the path toward the goal from the current location.

    Input: xstart - x coordinate of the current location
           ystart - y coordinate of the current location

    Output: x - coordinate of the point on obstacle where the robot hits
            y - coordinate of the point on obstacle where the robot hits
    """
    print("Following m-line...\n")
    if workspace==1:
        step=2
        pass
    else:
        step=1
        pass
    if abs(M[1][1]-ystart)>abs(M[1][0]-xstart): #step size
        x=np.linspace(xstart+0.0001*np.sign(M[1][0]-xstart),M[1][0],step*abs(M[1][1]-ystart))
        y=np.linspace(ystart+0.0001*np.sign(M[1][1]-ystart),M[1][1],step*abs(M[1][1]-ystart))
    else:
        x=np.linspace(xstart+0.0001*np.sign(M[1][0]-xstart),M[1][0],step*abs(M[1][0]-xstart))
        y=np.linspace(ystart+0.0001*np.sign(M[1][1]-ystart),M[1][1],step*abs(M[1][0]-xstart))
    for i in range(2,len(y)):
        for w in Workspace:
            if FindPoint(w[0][0],w[0][1],w[2][0],w[2][1],x[i],y[i])==True: #point inside the obstacle
                # glx.append(x[i-2])
                glx.append(x[i-1])
                # gly.append(y[i-2])
                gly.append(y[i-1])
                xd.append(x[i-1])
                yd.append(y[i-1])
                visualiseObstacles(workspace)
                for p in range(len(glx)-1):
                    plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
                    pass
                plt.plot(x[i-1],y[i-1],'ro')
                plt.pause(0.0001)
                plt.clf()
                # glx.append(x[i-1])
                glx.append(round(x[i]))
                # gly.append(y[i-1])
                gly.append(round(y[i]))
                xd.append(round(x[i]))
                yd.append(round(y[i]))
                visualiseObstacles(workspace)
                for p in range(len(glx)-1):
                    plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
                    pass
                plt.plot(x[i],y[i],'ro')
                plt.pause(0.0001)
                plt.clf()
                return round(x[i]),round(y[i])
            else:
                # glx.append(x[i-2])
                glx.append(x[i-1])
                # gly.append(y[i-2])
                gly.append(y[i-1])
                xd.append(x[i-1])
                yd.append(y[i-1])
                visualiseObstacles(workspace)
                for p in range(len(glx)-1):
                    plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
                    pass
                plt.plot(x[i-1],y[i-1],'ro')
                plt.pause(0.0001)
                plt.clf()

def rect(x1,y1,x2,y2):
    """
    This function returns a list of points on the circumference of the rectangle at the interval of 1 in both perpendicular directions.

    Input: x1 - x coordinate of one point on the rectangle
           y1 - y coordinate of one point on the rectangle
           x2 - x coordinate of diagonally opposite point on th rectangle
           y2 - y coordinate of diagonally opposite point on th rectangle

    Output: points - list of points
    """
    points=[]
    for i in range(x1,x2,np.sign(x2-x1)):
        points.append([i,y1])
        pass
    for i in range(y1,y2,np.sign(y2-y1)):
        points.append([x2,i])
        pass
    for i in range(x2,x1,np.sign(x1-x2)):
        points.append([i,y2])
        pass
    for i in range(y2,y1,np.sign(y1-y2)):
        points.append([x1,i])
        pass
    return points

def FindPoint(x1, y1, x2, y2, x, y) : 
    """
    This function check if the point is inside a rectangle or not.

    Input: x1 - x coordinate of one point on the rectangle
           y1 - y coordinate of one point on the rectangle
           x2 - x coordinate of diagonally opposite point on th rectangle
           y2 - y coordinate of diagonally opposite point on th rectangle
           x - x coordinate of the point to  check
           y - y coordinate of the point to  check

    Output: True or False
    """
    if (x >= x1 and x <= x2 and 
        y >= y1 and y <= y2) : 
        return True
    else : 
        return False

def circumnavigateWithPlot(x,y,xend,yend,dir,pre,previousDist,xmin,ymin):
    """
    This function follows the ostacles until it reaches the point (xend,yend) while plotting.

    Input: x - x coordinate of the current location
           y - y coordinate of the current location
           xend - x coordinate of the final location
           yend - y coordinate of the final location
           dir - clockwise or counterclockwise
           pre - internal flag
           previousDist - distance between current point and goal
           xmin - x coordinate of current location
           ymin - y coordinate of current location

    Output: "not on an obstacle" if (x,y) are not on any obstacle
            reccur untill reached (xend,yend)
            xmin - x coordinate of point with least distance
            ymin - y coordinate of point with least distance
    """
    pointonobs.append([x,y])
    xend=xend
    yend=yend
    inclusion=[]
    inside=0
    for i,ele in enumerate(Workspace):
        if [x,y] in rect(ele[1][0],ele[1][1],ele[3][0],ele[3][1]):
            inclusion.append(i)
            inside=1
    if len(inclusion)==1:
        listOfPoints=rect(Workspace[inclusion[0]][1][0],Workspace[inclusion[0]][1][1],Workspace[inclusion[0]][3][0],Workspace[inclusion[0]][3][1])
        index=listOfPoints.index([x,y])
        pre=inclusion[0]
        pass
    else:
        for i in inclusion:
            if i!=pre:
                listOfPoints=rect(Workspace[i][1][0],Workspace[i][1][1],Workspace[i][3][0],Workspace[i][3][1])
                index=listOfPoints.index([x,y])
            pass
        pass
    if inside==0:
        return "not on an obstacle"
    else:
        xnew=listOfPoints[(index+dir)%len(listOfPoints)][0]
        ynew=listOfPoints[(index+dir)%len(listOfPoints)][1]
        glx.append(xnew)
        gly.append(ynew)
        xd.append(xnew)
        yd.append(ynew)
        visualiseObstacles(workspace)
        for p in range(len(glx)-1):
            plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
            pass
        plt.plot(xnew,ynew,'ro')
        plt.pause(0.0001)
        plt.clf()
        if calculateDistance(xnew,ynew,M[1][0],M[1][1])<previousDist:
            previousDist=calculateDistance(xnew,ynew,M[1][0],M[1][1])
            xmin=xnew
            ymin=ynew
        if calculateDistance(xnew,ynew,M[1][0],M[1][1])==previousDist:
            leastpoints.clear()
            leastpoints.append([xmin,ymin])
            leastpoints.append([xnew,ynew])
            xmin=xnew
            ymin=ynew
        if xnew!=xend or ynew!=yend:
            return circumnavigateWithPlot(xnew,ynew,xend,yend,dir,pre,previousDist,xmin,ymin)
        else:
            whichpoint=[]
            if len(leastpoints)>1:
                l=len(pointonobs)
                for lp in leastpoints:
                    ind=pointonobs.index([lp[0],lp[1]])
                    if ind<(len(pointonobs)-ind) and ind<l:
                        l=ind
                        whichpoint=lp
                    elif ind>=(len(pointonobs)-ind) and (len(pointonobs)-ind)<l:
                        l=(len(pointonobs)-ind)
                        whichpoint=lp
                xmin,ymin=whichpoint[0],whichpoint[1]
            print("Point with least distance detected: ("+str(xmin)+","+str(ymin)+")\n")
            return xmin,ymin

def circumnavigateWithoutPlot(x,y,xend,yend,dir,pre):
    """
    This function follows the ostacles until it reaches the point (xend,yend) while plotting.

    Input: x - x coordinate of the current location
           y - y coordinate of the current location
           xend - x coordinate of the final location
           yend - y coordinate of the final location
           dir - clockwise or counterclockwise
           pre - internal flag

    Output: "not on an obstacle" if (x,y) are not on any obstacle
            reccur untill reached (xend,yend)
    """
    xend=xend
    yend=yend
    inclusion=[]
    inside=0
    for i,ele in enumerate(Workspace):
        if [x,y] in rect(ele[1][0],ele[1][1],ele[3][0],ele[3][1]):
            inclusion.append(i)
            inside=1
    if len(inclusion)==1:
        listOfPoints=rect(Workspace[inclusion[0]][1][0],Workspace[inclusion[0]][1][1],Workspace[inclusion[0]][3][0],Workspace[inclusion[0]][3][1])
        index=listOfPoints.index([x,y])
        pre=inclusion[0]
        pass
    else:
        for i in inclusion:
            if i!=pre:
                listOfPoints=rect(Workspace[i][1][0],Workspace[i][1][1],Workspace[i][3][0],Workspace[i][3][1])
                index=listOfPoints.index([x,y])
            pass
        pass
    if inside==0:
        return "not on an obstacle"
    else:
        xnew=listOfPoints[(index+dir)%len(listOfPoints)][0]
        ynew=listOfPoints[(index+dir)%len(listOfPoints)][1]
        glx.append(xnew)
        gly.append(ynew)
        xd.append(xnew)
        yd.append(ynew)
        visualiseObstacles(workspace)
        for p in range(len(glx)-1):
            plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
            pass
        plt.plot(xnew,ynew,'ro')
        plt.pause(0.0001)
        plt.clf()
        if xnew!=xend or ynew!=yend:
            return circumnavigateWithoutPlot(xnew,ynew,xend,yend,dir,pre)
        else:
            print("Leaving the Obstacle...\n")

def circumnavigateBug2(x,y,xend,yend,dir,pre):
    """
    This function follows the ostacles until it reaches the point (xend,yend).

    Input: x - x coordinate of the current location
           y - y coordinate of the current location
           xend - x coordinate of the final location
           yend - y coordinate of the final location
           dir - clockwise or counterclockwise
           pre - internal flag

    Output: "not on an obstacle" if (x,y) are not on any obstacle
            reccur untill reached (xend,yend)
    """
    xend=xend
    yend=yend
    inclusion=[]
    inside=0
    for i,ele in enumerate(Workspace):
        if [x,y] in rect(ele[1][0],ele[1][1],ele[3][0],ele[3][1]):
            inclusion.append(i)
            inside=1
    if len(inclusion)==1:
        listOfPoints=rect(Workspace[inclusion[0]][1][0],Workspace[inclusion[0]][1][1],Workspace[inclusion[0]][3][0],Workspace[inclusion[0]][3][1])
        index=listOfPoints.index([x,y])
        pre=inclusion[0]
        pass
    else:
        for i in inclusion:
            if i!=pre:
                listOfPoints=rect(Workspace[i][1][0],Workspace[i][1][1],Workspace[i][3][0],Workspace[i][3][1])
                index=listOfPoints.index([x,y])
            pass
        pass
    if inside==0:
        return "not on an obstacle"
    else:
        xnew=listOfPoints[(index+dir)%len(listOfPoints)][0]
        ynew=listOfPoints[(index+dir)%len(listOfPoints)][1]
        glx.append(x)
        glx.append(xnew)
        gly.append(y)
        gly.append(ynew)
        xd.append(xnew)
        yd.append(ynew)
        visualiseObstacles(workspace)
        for p in range(len(glx)-1):
            plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
            pass
        plt.plot(xnew,ynew,'ro')
        plt.pause(0.0001)
        plt.clf()
        if xnew!=xend or ynew!=yend:
            return circumnavigateBug2(xnew,ynew,xend,yend,dir,pre)
        # else:
            # print("Leaving the Obstacle...\n")

def line(coordinate,value):
    """
    This function returns the other coordinate on mLine.

    Input: coordinate - x or y coordinate
           value - value of the x or y coordinate

    Output: value of the other coordinate
    """
    if coordinate=="x":
        if M[0][0]==M[1][0]:
            return M[0][1]
        else:
            return (((value-M[0][0])*(M[1][1]-M[0][1])/(M[1][0]-M[0][0]))+M[0][1])
    else:
        if M[0][1]==M[1][1]:
            return M[0][0]
        else:
            return (((value-M[0][1])*(M[1][0]-M[0][0])/(M[1][1]-M[0][1]))+M[0][0])
    pass

def gamma(x):
    """
    This function returns the parameter gamma of the points on the mLine.

    Input: x - x coordinate

    Output: gamma
    """
    return (x-M[0][0])/(M[1][0]-M[0][0])

def pointsFromGamma(gamma):
    """
    This function returns the coordinates on the mLine.

    Input: gamma - parameter

    Output: x - x coordinate of the point on the mLine
            y - y coordinate of the point on the mLine 
    """
    x=M[0][0]+gamma*(M[1][0]-M[0][0])
    y=M[0][1]+gamma*(M[1][1]-M[0][1])
    return x,y

def hitpoints():
    """
    This function returns a list of points with their gamma on mLine that cuts the obstacle on the edges.

    Input: None

    Output: hp - list of points
    """
    hp=[]
    for i in Workspace:
        y=[]
        x=[]
        for j in [0,2]:# diagonal points
            y.append(line("x",i[j][0]))
            x.append(line("y",i[j][1]))
        for j in y:
            if i[2][1]>i[0][1]:
                if j>=i[0][1] and j<=i[2][1]:
                    hp.append([round(line("y",j)),round(j),round(gamma(line("y",j)),2)])
                    pass
                pass
            else:
                if j<=i[0][1] and j>=i[2][1]:
                    hp.append([round(line("y",j)),round(j),round(gamma(line("y",j)),2)])
                    pass
                pass
        for j in x:
            if i[2][0]>i[0][0]:
                if j>i[0][0] and j<i[0][1]:
                    hp.append([round(j),round(line("x",j)),round(gamma(j),2)])
                    pass
                pass
            else:
                if j<i[0][0] and j>i[0][1]:
                    hp.append([round(j),round(line("x",j)),round(gamma(j),2)])
                    pass
                pass
    hp.sort()
    hp=list(hp for hp,_ in itertools.groupby(hp))
    return hp

def mLine(x,y):
    """
    This function check if a point is on the mLine

    Input: x - x coordinate of the point
           y - y coordinate of the point

    Output: "on" or "off"
    """
    if (y==(((M[1][1]-M[0][1])*(x-M[0][0]))/(M[1][0]-M[0][0])+M[0][1])):
        return "on"
    else:
        return "off"

def hitpointsC(x,y,xend,yend,dir,pre):
    """
    This function returns the list of hitpoints in order they are encountered while following the obstacle. 

    Input: x - x coordinate of the current location
           y - y coordinate of the current location
           xend - x coordinate of the final location
           yend - y coordinate of the final location
           dir - clockwise or counterclockwise
           pre - internal flag

    Output: "not on an obstacle" if (x,y) are not on any obstacle
            reccur untill reached (xend,yend)
    """
    xend=xend
    yend=yend
    inclusion=[]
    inside=0
    for i,ele in enumerate(Workspace):
        if [x,y] in rect(ele[1][0],ele[1][1],ele[3][0],ele[3][1]):
            inclusion.append(i)
            inside=1
    if len(inclusion)==1:
        listOfPoints=rect(Workspace[inclusion[0]][1][0],Workspace[inclusion[0]][1][1],Workspace[inclusion[0]][3][0],Workspace[inclusion[0]][3][1])
        index=listOfPoints.index([x,y])
        pre=inclusion[0]
        pass
    else:
        for i in inclusion:
            if i!=pre:
                listOfPoints=rect(Workspace[i][1][0],Workspace[i][1][1],Workspace[i][3][0],Workspace[i][3][1])
                index=listOfPoints.index([x,y])
            pass
        pass
    if inside==0:
        print("not on an obstacle")
    else:
        xnew=listOfPoints[(index+dir)%len(listOfPoints)][0]
        ynew=listOfPoints[(index+dir)%len(listOfPoints)][1]
        if mLine(x,y)=="on":
            hp.append([x,y,round(gamma(x),2)])
            pass
        if xend!=xnew or yend!=ynew:
            return hitpointsC(xnew,ynew,xend,yend,dir,pre)
        else:
            return hp
    pass

if __name__ == "__main__":

    workspace=input("Which Workspace???\n")

    workspace=int(workspace)

    if workspace==1:
        W1O0=[[1,1],[2,1],[2,5],[1,5]]
        W1O1=[[3,4],[4,4],[4,12],[3,12]]
        W1O2=[[3,12],[12,12],[12,13],[3,13]]
        W1O3=[[12,5],[13,5],[13,13],[12,13]]
        W1O4=[[6,5],[12,5],[12,6],[6,6]]
        Workspace=[W1O0,W1O1,W1O2,W1O3,W1O4]
        M=[[0,0],[10,10]]
        pass
    elif workspace==2:
        W2O0=[[-6,-6],[25,-6],[25,-5],[-6,-5]]
        W2O1=[[-6,5],[30,5],[30,6],[-6,6]]
        W2O2=[[-6,-5],[-5,-5],[-5,5],[-6,5]]
        W2O3=[[4,-5],[5,-5],[5,1],[4,1]]
        W2O4=[[9,0],[10,0],[10,5],[9,5]]
        W2O5=[[14,-5],[15,-5],[15,1],[14,1]]
        W2O6=[[19,0],[20,0],[20,5],[19,5]]
        W2O7=[[24,-5],[25,-5],[25,1],[24,1]]
        W2O8=[[29,0],[30,0],[30,5],[29,5]]
        Workspace=[W2O0,W2O1,W2O2,W2O3,W2O4,W2O5,W2O6,W2O7,W2O8]
        M=[[0,0],[35,0]]
        pass
    else:
        print("No such Workspace!!!")
        sys.exit(0)

    bug=input("Which Bug???\n")

    bug=int(bug)

    circum=input("'left' or 'right' turning???\n")

    if circum == "left":
        d=1
        pass
    elif circum == "right":
        d=-1
        pass
    else:
        print("Enter the correct direction!!!")
        sys.exit(0)

    xd=[]
    xd.append(M[0][0])
    yd=[]
    yd.append(M[0][1])

    if bug == 1:
        if M[0][0]==M[1][0]:
            M=[[M[0][0],M[0][1]],[M[1][0],float(M[1][1])+0.001]]
            pass
        elif M[0][1]==M[1][1]:
            M=[[M[0][0],float(M[0][1])+0.001],[M[1][0],M[1][1]]]
            pass
        glx=[M[0][0]]
        gly=[M[0][1]]
        Lx,Ly=M[0][0],M[0][1]
        while 1:
            try:
                Hx,Hy=followM(Lx,Ly)
                print("Hit the Obstacle at: ("+str(Hx)+","+str(Hy)+")\n")
                maxDist=calculateDistance(M[0][0],M[0][1],M[1][0],M[1][1])
                print("Following the Obstacles...\n")
                pointonobs=[]
                leastpoints=[]
                Lx,Ly=circumnavigateWithPlot(Hx,Hy,Hx,Hy,d,-1,maxDist,0,0)
                dilemma=pointonobs.index([Lx,Ly])
                if dilemma<=(len(pointonobs)-1-dilemma):
                    dtemp=d
                    pass
                else:
                    dtemp=-d
                    pass
                circumnavigateWithoutPlot(Hx,Hy,Lx,Ly,dtemp,-1)
                print("Leave the Obstacle at: ("+str(Lx)+","+str(Ly)+")\n")
            except:
                glx.append(M[1][0])
                gly.append(M[1][1])
                break
        xd.append(M[1][0])
        yd.append(M[1][1])
        for i in range(len(xd)-1):
            totalDistance=totalDistance+calculateDistance(xd[i],yd[i],xd[i+1],yd[i+1])
            pass
        print("The total distance travelled is: "+str(round(totalDistance,2))+" units")
        plt.clf()
        visualiseObstacles(workspace)
        for p in range(len(glx)-1):
            plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
            pass
        plt.show()
        pass

    elif bug == 2:
        glx=[M[0][0]]
        gly=[M[0][1]]
        visited=[]
        flag='f'
        x=M[0][0]
        y=M[0][1]
        hp=[]
        h=[]
        if M[0][0]==M[1][0]:
            M=[[M[0][0],M[0][1]],[M[1][0],float(M[1][1])+0.001]]
            pass
        elif M[0][1]==M[1][1]:
            M=[[M[0][0],float(M[0][1])+0.001],[M[1][0],M[1][1]]]
            pass
        hitPoints=hitpoints()
        M=[[int(M[0][0]),int(M[0][1])],[int(M[1][0]),int(M[1][1])]]
        for i in range(len(hitPoints)):
            h=h+hitpointsC(hitPoints[i][0],hitPoints[i][1],hitPoints[i][0],hitPoints[i][1],d,-1)
            pass
        dup_free = []
        for dup in h:
            if dup not in dup_free:
                dup_free.append(dup)
        hitPoints=list(dup_free for dup_free,_ in itertools.groupby(dup_free))
        hlen=len(hitPoints)
        M=[[M[0][0],M[0][1]],[M[1][0],M[1][1]]]
        while 1:
            try:
                #do this
                if flag=='f':
                    print("Leaving the Obstacle at: ("+str(x)+","+str(y)+")\n")
                    x,y=followM(x,y)
                    bestgamma=gamma(x)
                    print("Hit the Obstacle at: ("+str(x)+","+str(y)+")\n")
                    print("Following the Obstacles...\n")
                    pass
                else:
                    i=hitPoints.index([x,y,round(gamma(x),2)])
                    circumnavigateBug2(x,y,hitPoints[(i+1)%hlen][0],hitPoints[(i+1)%hlen][1],d,-1)
                    x,y=hitPoints[(i+1)%hlen][0],hitPoints[(i+1)%hlen][1]
                    pass
                #next conditions
                flag='f'
                if visited.count([x,y])>=1:#visited
                    print("Point is visited...\n")
                    flag='c'
                    pass
                xnew,ynew=pointsFromGamma(gamma(x)+0.01)#blocking
                for w in Workspace:
                    if FindPoint(w[0][0],w[0][1],w[2][0],w[2][1],xnew,ynew)==True:
                        flag='c'
                        pass
                    pass
                if gamma(x)<bestgamma:#update leave points
                    flag='c'
                    pass
                visited.append([x,y])
                pass
            except:
                glx.append(M[1][0])
                gly.append(M[1][1])
                break
        xd.append(M[1][0])
        yd.append(M[1][1])
        pass
        for i in range(len(xd)-1):
            totalDistance=totalDistance+calculateDistance(xd[i],yd[i],xd[i+1],yd[i+1])
            pass
        print("The total distance travelled is: "+str(round(totalDistance,2))+" units")
        plt.clf()
        visualiseObstacles(workspace)
        for p in range(len(glx)-1):
            plt.plot([glx[p],glx[p+1]],[gly[p],gly[p+1]],'black',alpha=0.5,linewidth=4)
            pass
        plt.show()
    
    else:
        print("No such Bug!!!")
        sys.exit(0)