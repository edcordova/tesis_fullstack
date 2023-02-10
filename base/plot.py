import matplotlib.pyplot as plt
from io import StringIO

def return_graph(arr1, arr2, str1, str2):

    x = arr1
    y = arr2

    fig = plt.figure(figsize=(6,4))
    plt.plot(x,y)
    plt.xlabel(str1)
    plt.ylabel(str2)
    plt.title("VISTA HORIZONTAL")

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def return_graph_inv(arr1, arr2):

    x = arr1
    y = arr2

    fig = plt.figure(figsize=(6,4))
    plt.plot(x,y)
    plt.xlabel('DESPLAZAMIENTO HORIZONTAL (pies)')
    plt.ylabel('PROFUNDIDAD (pies)')
    plt.title("VISTA VERTICAL")
    plt.gca().invert_yaxis()
    ax = plt.gca()
    # ax.set_ylim([21000, 0])
    
    
    
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
