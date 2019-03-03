import math

def print_matrix(matrix):
    output = ""
    for num in range(len(matrix[0])):
        for item in matrix:
            output+=str(item[num])+" "
        output+="\n"
    print(output)
    pass

def ident(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    pass

def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        tmp = row[:]
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def scale(matrix, sx, sy, sz):
    d = [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]
    matrix_mult(d, matrix)
    pass

def move(matrix, tx, ty, tz):
    t = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [tx, ty, tz, 1]]
    matrix_mult(t, matrix)
    pass

def rotate(matrix, axis, theta):
    t = theta * math.pi/180
    if axis == 'z':
        r = [[math.cos(t), math.sin(t), 0, 0], [-1*math.sin(t), math.cos(t), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        matrix_mult(r, matrix)
    elif axis == 'x':
        r = [[1, 0, 0, 0], [0, math.cos(t), math.sin(t), 0], [0, -1*math.sin(t), math.cos(t), 0], [0, 0, 0, 1]]
        matrix_mult(r, matrix)
    else:
        r = [[-1*math.sin(t), 0, math.cos(t), 0], [0, 1, 0, 0], [math.cos(t), 0, math.sin(t), 0], [0, 0, 0, 1]]
        matrix_mult(r, matrix)
    pass
