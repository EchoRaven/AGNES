import math
from matplotlib import pyplot as plt

def dis(p1, p2):
    distant = 0
    for index in range(len(p1)):
        distant += (p1[index]-p2[index])*(p1[index]-p2[index])
    return math.sqrt(distant)

def dMin(c1, c2):
    distant = dis(c1[0], c2[0])
    for i in range(len(c1)):
        for j in range(len(c2)):
            distant = min(distant, dis(c1[i], c2[j]))
    return distant

def dMax(c1, c2):
    distant = dis(c1[0], c2[0])
    for i in range(len(c1)):
        for j in range(len(c2)):
            distant = max(distant, dis(c1[i], c2[j]))
    return distant

def dAvg(c1, c2):
    distant = 0
    for i in range(len(c1)):
        for j in range(len(c2)):
            distant += dis(c1[i], c2[j])
    return distant / (len(c1) * len(c2))

class AGNES:
    def __init__(self):
        self.data = []
        #聚类
        self.Class = []
        #聚类数量
        self.ClassNum = 0

    def Train(self, classNum = 3, data = [], disAlgorithm = dMax):
        self.ClassNum = classNum
        for i in range(len(data)):
            self.Class.append([data[i]])
        while len(self.Class) != classNum:
            distant = disAlgorithm(self.Class[0], self.Class[1])
            c1 = 0
            c2 = 1
            for i in range(len(self.Class)):
                for j in range(len(self.Class)):
                    if i == j:
                        continue
                    if disAlgorithm(self.Class[i], self.Class[j]) < distant:
                        distant = disAlgorithm(self.Class[i], self.Class[j])
                        c1 = i
                        c2 = j
            newClass = []
            class1 = self.Class[c1]
            class2 = self.Class[c2]
            self.Class.pop(c1)
            self.Class.pop(c2-1)
            newClass.extend(class1)
            newClass.extend(class2)
            self.Class.append(newClass)

    def ShowPlot(self):
        marks = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        for i in range(len(self.Class)):
            for p in self.Class[i]:
                plt.plot(p[0], p[1], marks[i], markersize=5)
        plt.show()

if __name__ == "__main__":
    agnes = AGNES()
    datas = [[0.697, 0.460], [0.774, 0.376], [0.634, 0.264], [0.608, 0.318],
             [0.556, 0.215], [0.403, 0.237], [0.481, 0.149], [0.437, 0.211],
             [0.666, 0.091], [0.243, 0.267], [0.245, 0.057], [0.343, 0.099],
             [0.639, 0.161], [0.657, 0.198], [0.360, 0.370], [0.593, 0.042],
             [0.719, 0.103], [0.359, 0.188], [0.339, 0.241], [0.282, 0.257],
             [0.748, 0.232], [0.714, 0.346], [0.483, 0.312], [0.478, 0.437],
             [0.525, 0.369], [0.751, 0.489], [0.532, 0.472], [0.473, 0.376],
             [0.725, 0.445], [0.446, 0.459]]
    agnes.Train(data=datas)
    agnes.ShowPlot()