import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('./exams.csv')
data = df["math score"].tolist()

def randomset(counter):
    dataset = []
    for i in range(0, counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    pf = meanlist
    mean = statistics.mean(pf)
    fig = ff.create_distplot([data], ["math score"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        setofnames = randomset(100)
        meanlist.append(setofnames)

    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print("mean of math score = ", mean)

setup()