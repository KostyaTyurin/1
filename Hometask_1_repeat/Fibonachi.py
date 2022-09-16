import time
import plotly.graph_objs as go
import numpy as np


def fibonachi(n):
    start = time.time()
    if n == 0:
        end = time.time()
        return (0, end - start)
    elif n == 1:
        end = time.time()
        return (1, end - start)
    else:
        list_of_results = list(0 for _ in range(n+1))
        list_of_results[0] = 0
        list_of_results[1] = 1
        for j in range(2, n+1):
            list_of_results[j] = list_of_results[j-1] + list_of_results[j-2]
        end = time.time()
        return(list_of_results[n], end - start)

def fibonachi_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonachi_r(n-1) + fibonachi_r(n-2)




fig = go.Figure()
list_of_args = list(i for i in range(20))
time_list_r = list()
time_list_d = list()
for j in range(20):
    res, time_dyn = fibonachi(j)
    start = time.time()
    fibonachi_r(j)
    end = time.time()
    time_list_d.append(time_dyn)
    time_list_r.append(end - start)

fig.add_trace(
    go.Scatter(
        x=np.array(list_of_args),
        y=np.array(time_list_r),
        name='Recursive'
    )
)
fig.add_trace(
    go.Scatter(
        x=np.array(list_of_args),
        y=np.array(time_list_d),
        name='Dynamic'
    )
)
fig.update_yaxes(title_text='Time, s')
fig.update_xaxes(title_text='Number')
fig.show()
