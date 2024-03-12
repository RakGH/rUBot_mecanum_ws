#!/usr/bin/env python3
import rospy
from rubot_nav import move_rubot
from math import sqrt,sin,cos, radians


def square_path(v,td):
    move_rubot(v,0,0,td)
    move_rubot(0,v,0,td)
    move_rubot(-v,0,0,td)
    move_rubot(0,-v,0,td)


def triangular_path(v, td):
    move_rubot(v,0,0,td)
    move_rubot(-v,v,0,td/sqrt(2))
    move_rubot(-v,-v,0,td/sqrt(2))

def hourglass_path(v, td):    
    angle_radians = radians(60)
    v_x = v * cos(angle_radians)
    v_y = v * sin(angle_radians)

    move_rubot(v,0,0,td)
    move_rubot(-v_x, v_y, 0, td)
    move_rubot(-v_x, v_y, 0, td)
    move_rubot(v,0,0,td)
    move_rubot(-v_x, -v_y, 0, td)
    move_rubot(-v_x, -v_y, 0, td)

def rombe_path(v, td):
    angle_radians = radians(60)
    v_x = v * cos(angle_radians)
    v_y = v * sin(angle_radians)

    move_rubot(-v_x, v_y, 0, td)
    move_rubot(-v_x, -v_y, 0, td)
    move_rubot(v_x, -v_y, 0, td)
    move_rubot(v_x, v_y, 0, td)

def triangular_spiral_path(v, w, td):
    move_rubot(v,0,0,td*5)
    move_rubot(0,0,-w,td*7)
    move_rubot(v,0,0,td*8.25)
    move_rubot(0,0,-w,td*7)
    move_rubot(v,0,0,td*11)
    move_rubot(0,0,-w,td*7.3)
    move_rubot(v,0,0,td*13.5)
    move_rubot(0,0,-w,td*7)
    move_rubot(v,0,0,td*13.5)

if __name__ == '__main__':
    try:
        rospy.init_node('rubot_nav', anonymous=False)
        v= rospy.get_param("~v")
        w= rospy.get_param("~w")
        td= rospy.get_param("~td")
        path= rospy.get_param("~path")

        if path == "Square":
            square_path(v, td)

        elif path == "Triangular":
            triangular_path(v, td)

        elif path == "Spiral":
            triangular_spiral_path(v, w, td)

        elif path == "Hourglass":
            hourglass_path(v, td)

        elif path == "Rombe":
            rombe_path(v, td)

        else:
            print('Error: unknown movement')

    except rospy.ROSInterruptException:
        pass
