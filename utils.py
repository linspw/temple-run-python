import OpenGL.GL as Gl
import OpenGL.GLU as Glu
import OpenGL.GLUT as Glut

class Utils:
  def render_text(self, string, x, y):
    Gl.glPushMatrix()
    Gl.glColor4f(0.4, 0.5, 0.7, 1.0)
    Gl.glRasterPos2f(-0.5, 1)

    for char in string:
      Glut.glutBitmapCharacter(Glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

    Gl.glPopMatrix()
