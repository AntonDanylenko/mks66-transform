from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    matrix = new_matrix
    f = open(fname, 'rU')
    lines = f.read().split('\n')
    i = 0
    while i<len(lines):
        if (lines[i]=="line"):
            args = lines[i+1].split(" ")
            add_edge(matrix, args[0], args[1], args[2], args[3], args[4], args[5])
            i+=2
        else if (lines[i]=="ident"):
            ident(matrix)
            i+=1
        else if (lines[i]=="scale"):
            args = lines[i+1].split(" ")
            transform = make_scale(args[0], args[1], args[2])
            i+=2
