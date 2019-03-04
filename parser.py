from display import *
from matrix import *
from draw import *

def parse_file(filename, edges, transform, screen, color):
    ident(transform)
    file = open(filename, "r").read().strip().split('\n')
    index = 0
    while index < len(file):
        item = file[index]
        if item == "line":
            l = file[index + 1].split(' ')
            add_edge(edges,int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5]))
            index += 2
        elif item == "ident":
            ident(transform)
            index += 1
        elif item == "scale":
            l = file[index + 1].split(' ')
            scale(transform, int(l[0]),int(l[1]),int(l[2]))
            index += 2
        elif item == "move":
            l = file[index + 1].split(' ')
            move(transform, int(l[0]), int(l[1]), int(l[2]))
            index += 2
        elif item == "rotate":
            l = file[index + 1].split(' ')
            rotate(transform, l[0], int(l[1]))
            index += 2
        elif item == "apply":
            matrix_mult(transform, edges)
            index += 1
        elif item == "display":
            clear_screen(screen)
            draw_lines(edges, screen, color)
            display(screen)
            index += 1
        elif item == "save":
            fname = file[index + 1]
            clear_screen(screen)
            draw_lines(edges, screen, color)
            save_extension(screen, fname)
            index += 2
        else:
            pass
    pass
