import OpenGL.GL as Gl
import OpenGL.GLU as Glu
import OpenGL.GLUT as Glut
import sys
from character import *
from utils import *
from scenario import *
from blocks import *

class Game:
  def __init__(self):
    self.windowPositionX = 50
    self.windowPositionY = 10
    self.viewWidth = 800
    self.viewHeight = 800
    self.SCENARIO = Scenario()
    self.CHARACTER = Character()
    self.UTILS = Utils()
    self.BLOCKS = Blocks()
    self.screenAngleZoom = 30
    self.screenAngleX = 0
    self.screenAngleY = 0
    self.screenSpectatorX = 0
    self.screenSpectatorY = 3
    self.screenSpectatorZ = 10
    self.fAspect = 1
    self.gameStatus = "to_start"
    self.scenarioBorderLimit = 0.7
    self.velocity = 0.0009

  def initialize(self):
    self.score = 0.0

  def display(self):
    Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
    self.SCENARIO.render()
    self.CHARACTER.render()
    self.BLOCKS.render()
  
    if(self.gameStatus == "to_start"):
      text = str("Use Menu to Start")
      self.UTILS.render_text(text, self.viewWidth/2, self.viewHeight/2)

    if(self.gameStatus == "started" or self.gameStatus == "paused"):
      text = str('%.2f' % self.score)
      self.UTILS.render_text(text, 20, self.viewHeight - 40)

    if(self.gameStatus == "loose"):
      text = str('You loose! - %.2f meters' % self.score)
      self.UTILS.render_text(text, self.viewWidth/2, self.viewHeight/2)

    Gl.glFlush()

  def moveCamera(self, key, x1, y1):
    if (key == Glut.GLUT_KEY_UP):
        self.screenSpectatorY -= 1
    elif (key == Glut.GLUT_KEY_DOWN):
        self.screenSpectatorY += 1
    elif (key == Glut.GLUT_KEY_LEFT):
        self.screenSpectatorX -= 1
    elif (key == Glut.GLUT_KEY_RIGHT):
        self.screenSpectatorX += 1

    self.screen_vision()

  def screen_vision(self):
    Gl.glMatrixMode(Gl.GL_PROJECTION)
    Gl.glLoadIdentity()
    #Especifica a projeção perspectiva
    Glu.gluPerspective(self.screenAngleZoom, self.fAspect, 0.1, 700)
    #Especifica sistema de coordenadas do modelo
    Gl.glMatrixMode(Gl.GL_MODELVIEW)
    # Inicializa sistema de coordenadas do modelo
    Gl.glLoadIdentity()
    Glu.gluLookAt(self.screenSpectatorX, self.screenSpectatorY, self.screenSpectatorZ , 0, 1, 4, 0.0, 1.0, 0.0)


  def screen_resize(self, w, h):
    Gl.glViewport(0, 0, w, h)
    self.viewWidth = w
    self.viewHeight = h
    self.screen_vision()

  def setup_ilumination(self):
    luzAmbiente = [0.2, 0.2, 0.2, 1]
    luzDifusa = [1, 1, 1, 1]
    luzEspecular = [1, 1, 1, 0]
    posicaoLuz = [0,0,1,0]
    especularidade = [0.4, 1, 0.4, 0.4]
    especMaterial = 50
    Gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    Gl.glShadeModel(Gl.GL_SMOOTH)
    Gl.glMaterialfv(Gl.GL_FRONT, Gl.GL_SPECULAR, especularidade)
    Gl.glMateriali(Gl.GL_FRONT, Gl.GL_SHININESS, especMaterial)
    Gl.glLightModelfv(Gl.GL_LIGHT_MODEL_AMBIENT, luzAmbiente)
    Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_AMBIENT, luzAmbiente)
    Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_DIFFUSE, luzDifusa)
    Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_SPECULAR, luzEspecular)
    Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, posicaoLuz)
    Gl.glEnable(Gl.GL_COLOR_MATERIAL)
    Gl.glEnable(Gl.GL_LIGHTING)
    Gl.glEnable(Gl.GL_LIGHT0)
    Gl.glEnable(Gl.GL_DEPTH_TEST)
    Gl.glEnable(Gl.GL_NORMALIZE)


  def setup_window(self):
    Glut.glutInit(sys.argv)
    Glut.glutInitDisplayMode(Glut.GLUT_SINGLE | Glut.GLUT_RGB | Glut.GLUT_DEPTH)
    Glut.glutInitWindowSize(self.viewWidth, self.viewHeight)
    Glut.glutInitWindowPosition(self.windowPositionX, self.windowPositionY)
    Glut.glutCreateWindow("Temple Run")
    Glut.glutReshapeFunc(self.screen_resize)
    Glut.glutSpecialFunc(self.moveCamera)
    Glut.glutKeyboardFunc (self.character_commands)
    Glut.glutIdleFunc(self.game_running)
  
  def setup_screen(self):
    Gl.glClearColor(239.0, 232.0, 226.0, 1.0)

  def setup_display(self):
    Glut.glutDisplayFunc(self.display)    
  
  def setup_menu(self):
    Glut.glutCreateMenu(self.process_menu_events)  
    Glut.glutAddMenuEntry("Start", 0)  
    Glut.glutAddMenuEntry("Pause", 1)
    Glut.glutAddMenuEntry("Exit", 2)
    Glut.glutAttachMenu(Glut.GLUT_RIGHT_BUTTON)

  def process_menu_events(self, option):
    if(option == 0):
      self.initialize()
      self.gameStatus = "started"
    elif(option == 1 and self.gameStatus != "to_start"):
      if not(self.gameStatus == "paused"):
        self.gameStatus = "paused"
      else:
        self.gameStatus = "started"
    elif(option == 2):
      Glut.glutLeaveMainLoop()
    
    return 0
  
  def character_commands(self, key, x, y):
    if(key == b'a'):
      if(self.CHARACTER.positionX > -self.scenarioBorderLimit): self.CHARACTER.move_right()
           
    if(key == b'd'):
      if(self.CHARACTER.positionX < self.scenarioBorderLimit): self.CHARACTER.move_left()
    
    self.screen_vision()

  def game_running(self):
    if (self.gameStatus == "started"):
      self.BLOCKS.move(self.velocity)
      self.BLOCKS.auto_generate_block()
      self.score += 0.01
      if(self.BLOCKS.check_if_collide(self.CHARACTER.positionX, self.CHARACTER.positionZ, self.CHARACTER.sizeRadius)):
        self.gameStatus = "loose"

    Glut.glutPostRedisplay()


  def render(self):
    self.setup_window()
    self.setup_screen()
    self.setup_menu()
    self.setup_display()
    self.setup_ilumination()
    Glut.glutMainLoop()
