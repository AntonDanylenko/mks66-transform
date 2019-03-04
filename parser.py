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
    f = open(fname, 'rU')
    lines = f.read().split('\n')
    f.close()
    i = 0
    while i<len(lines):
        #print("len(lines): " + str(len(lines)))
        #print("line: " + str(i))
        #print("command: " + lines[i])
        if (lines[i]=="line"):
            #print("args: " + lines[i+1])
            args = lines[i+1].split(" ")
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            i+=2
        elif (lines[i]=="ident"):
            ident(transform)
            i+=1
        elif (lines[i]=="scale"):
            #print("args: " + lines[i+1])
            args = lines[i+1].split(" ")
            matrix_mult(make_scale(float(args[0]), float(args[1]), float(args[2])), transform)
            i+=2
        elif (lines[i]=="translate"):
            #print("args: " + lines[i+1])
            args = lines[i+1].split(" ")
            #print("args[0]: " + str(int(args[0])))
            #print_matrix(transform)
            matrix_mult(make_translate(int(args[0]), int(args[1]), int(args[2])), transform)
            i+=2
        elif (lines[i]=="rotate"):
            #print("args: " + lines[i+1])
            args = lines[i+1].split(" ")
            if (args[0]=="x"):
                matrix_mult(make_rotX(int(args[1])), transform)
            elif (args[0]=="y"):
                matrix_mult(make_rotY(int(args[1])), transform)
            else:
                matrix_mult(make_rotZ(int(args[1])), transform)
            i+=2
        elif (lines[i]=="apply"):
            matrix_mult(transform, points)
            for col in range(len(points)):
                for row in range(len(points[0])):
                    points[col][row] = int(points[col][row])
            i+=1
        elif (lines[i]=="display"):
            #print_matrix(points)
            #clear_screen(screen)
            draw_lines(points, screen, color)
            color[1]+=15
            display(screen)
            i+=1
        elif (lines[i]=="save"):
            #print("args: " + lines[i+1])
            args = lines[i+1].split(" ")
            #clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, args[0])
            i+=2
        elif (lines[i]=="quit"):
            i=len(lines)
        else:
            i+=1
