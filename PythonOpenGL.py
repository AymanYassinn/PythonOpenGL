from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

academicNumber = ""
name = ""
sectionNumber = ""

def drawImage():
    academicNumberInt = int(academicNumber)
    if academicNumberInt == 1:
        glBegin(GL_TRIANGLES)
        glColor3f(0.3, 0.2, 0.1)  
        glVertex2f(0.0, 0.0)
        glVertex2f(-0.1, 0.5)
        glVertex2f(0.1, 0.5)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.5, 0.0)
        glVertex2f(-0.25, 0.5)
        glVertex2f(0.0, 0.75)
        glVertex2f(0.25, 0.5)
        glEnd()

    elif academicNumberInt == 2:  
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 0.0) 
        glVertex2f(-0.1, 0.1)
        glVertex2f(0.1, 0.1)
        glVertex2f(0.1, 0.3)
        glVertex2f(-0.1, 0.3)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.5, 0.0)
        glVertex2f(-0.05, 0.0)
        glVertex2f(0.05, 0.0)
        glVertex2f(0.05, 0.1)
        glVertex2f(-0.05, 0.1)
        glEnd()

    elif academicNumberInt == 3:
        glBegin(GL_TRIANGLES)
        glColor3f(0.5, 0.5, 0.5)  
        glVertex2f(-0.5, -0.5)
        glVertex2f(0.0, 0.5)
        glVertex2f(0.5, -0.5)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 0.0)  
        for i in range(360):
            theta = i * 3.14159 / 180
            x = 0.2 * math.cos(theta)
            y = 0.2 * math.sin(theta)
            glVertex2f(x, y)
        glEnd()
    else:
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 0.0) 
        for i in range(5):
            theta = 2.0 * math.pi * i / 5.0
            x = math.sin(theta)
            y = math.cos(theta)
            glVertex2f(x, y)
        glEnd()

def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT) 
    glRasterPos2f(-0.9, 0.9)
    heading = "ACADEMIC NUMBER: {}    NAME: {}    SECTION NUMBER: {}    MINI PROJECT".format(academicNumber, name, sectionNumber)
    for c in heading:
     glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))
    drawImage()
    glFlush()


def main():
    global academicNumber, name, sectionNumber

    academicNumber = input("Enter Academic Number: ")
    name = input("Enter Name: ")
    sectionNumber = input("Enter Section Number: ")
    glutInit(sys.argv)
  
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Mini Project")

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
