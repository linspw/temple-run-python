import OpenGL.GL as Gl
import OpenGL.GLU as Glu
import OpenGL.GLUT as Glut

class Scenario:
  def __init__(self, positionX = 0, positionY = 0, positionZ = 0):
    self.streetSizeX = 10.0
  
  def render(self):
    self.floor()
    self.left_wall()
    self.right_wall()

  def floor(self):
    Gl.glColor3f(0.47, 0.79, 0.47)
    Gl.glPushMatrix()
    Gl.glTranslate(0, 0, 0)
    Gl.glScaled(2.0, 0.1, self.streetSizeX)
    Glut.glutSolidCube(1.0)
    Gl.glPopMatrix()

  def left_wall(self):
    Gl.glColor3f(1.0, 0.72, 0.83)
    Gl.glPushMatrix()
    Gl.glTranslate(-1, 1, 0)
    Gl.glRotate(90, 0, 0, 1)
    Gl.glScaled(2.0, 0.05, self.streetSizeX)
    Glut.glutSolidCube(1.0)
    Gl.glPopMatrix()

  def right_wall(self):
    Gl.glColor3f(1.0, 0.72, 0.83)
    Gl.glPushMatrix()
    Gl.glTranslate(1, 1, 0)
    Gl.glRotate(90, 0, 0, 1)
    Gl.glScaled(2.0, 0.05, self.streetSizeX)
    Glut.glutSolidCube(1.0)
    Gl.glPopMatrix()
