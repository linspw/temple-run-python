import OpenGL.GL as Gl
import OpenGL.GLU as Glu
import OpenGL.GLUT as Glut

class Character:
  def __init__(self, positionX = 0, positionY = 0.5, positionZ = 4):
    self.positionX = positionX
    self.positionY = positionY
    self.positionZ = positionZ
    self.sizeX = 0.1
    self.sizeY = 0.1
    self.sizeZ = 0.1
    self.sizeRadius = 0.1
  
  def render(self):
    Gl.glColor3f(0.96, 0.96, 0.96)
    Gl.glPushMatrix()
    Gl.glTranslate(self.positionX, self.positionY, self.positionZ)
    Gl.glRotated(0, 0, 1, 0)
    Glut.glutSolidSphere(self.sizeRadius, 60, 60)
    Gl.glPopMatrix()


  def move_left(self, pixels = 0.1):
    self.positionX = self.positionX + pixels
  
  def move_right(self, pixels = 0.1):
    self.positionX = self.positionX - pixels

