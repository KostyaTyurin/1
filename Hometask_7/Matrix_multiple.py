import multiprocessing as mp
import plotly.graph_objects as go

def time_decorator(func):
    def wrapper(*args):
        import time
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        # print('Code time: {}'.format(end_time - start_time))

        return res, end_time - start_time
    return wrapper

def time_visualizer():
    global a, b
    fig = go.Figure()
    time_list = []
    cpu_count = mp.cpu_count()
    print(cpu_count)
    for j in range(1, cpu_count):
        res, time = a.mul_table(b, j)
        time_list.append(time)
    fig.add_trace(
        go.Scatter(
            x=[j for j in range(1, cpu_count)],
            y=[time_list[0]/sec for sec in time_list]
        )
    )
    fig.update_layout(
        xaxis_title = 'CPU number',
        yaxis_title = 'T1/Tn'
    )

    fig.show()


def skal_mul(list1, list2):
    res = 0
    for j in range(len(list1)):
        res += list1[j] * list2[j]
    return res


def mult_line(vector, other_cols):
    line = []
    for j in range(len(other_cols)):
        res = 0
        for k in range(len(vector)):
            res += vector[k] * other_cols[j][k]
        line.append(res)
    return line

class Matrix():

    def __init__(self, matrix=None):

        if matrix is not None:
            self.matrix = matrix
            self.rows = len(matrix)
            self.columns = len(matrix[0])
        else:
            self.matrix = []
            self.rows = 0
            self.columns = 0

    def read_csv(self, csv_file):
        with open(csv_file, 'r') as f:
            res = []
            lines = f.readlines()
            for line in lines:
                a = list(map(int, line.split(';')))
                res.append(a)
            self.matrix = res
            self.rows = len(res)
            self.columns = len(res[0])

    @time_decorator
    def __mul__(self, other):
        other_cols = []
        for col in range(other.columns):
            other_cols.append([x[col] for x in other.matrix])
        res = []
        for j in range(self.rows):
            res.append(mult_line(self.matrix[j], other_cols))
        return Matrix(res)

    # Multiprocessing
    @time_decorator
    def mul_table(self, other, cpu_num):
        p = mp.Pool(cpu_num)
        other_cols = []
        for col in range(other.columns):
            other_cols.append([x[col] for x in other.matrix])

        data = [(self.matrix[i], other_cols) for i in range(len(self.matrix))]
        res = p.starmap(mult_line, data)
        # print(Matrix(res))
        return Matrix(res)


    def __str__(self):
        res = []
        for line in self.matrix:
            res.append(str(line))
        return "[" + ", \n".join(res) + "]"



if __name__ == '__main__':
    a = Matrix()
    b = Matrix()
    a.read_csv('matrix_1.csv')
    b.read_csv('matrix_2.csv')
    time_visualizer()



