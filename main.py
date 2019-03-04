from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#parse_file( 'script', edges, transform, screen, color )

screen2 = new_screen()
yellow = [255, 203, 76]
orange = [241, 144, 32]
brown = [101, 71, 27]
face = new_matrix()
hand = new_matrix()
transform2 = new_matrix()

add_multi(face, "85,88 57,122 32,168 18,218 15,271 33,348 60,398 102,443 177,485 238,498 294,495 366,473 414,439 458,388 489,314 496,240 482,178 457,126 424,86 377,51 335,31 285,19 265,18", 500)
add_multi(hand, "85,88 92,118 110,143 136,169 144,187 145,207 140,224 140,236 145,243 152,246 162,243 176,233 188,210 192,186 189,165 181,151 176,143 179,139 194,142 334,174 347,171 353,163 356,153 353,144 344,138 262,118 271,107 274,95 270,82 261,74 266,72 272,64 273,55 269,44 257,36 262,31 264,20 261,11 251,4 245,0 134,0 124,8 108,24 97,40 89,60 86,75 85,88", 500)
#add_multi(matrix, "", 500)

parse_file('script2', face, transform2, screen2, color2)
parse_file('script2', hand, transform2, screen2, orange)
