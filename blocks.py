import OpenGL.GL as Gl
import OpenGL.GLU as Glu
import OpenGL.GLUT as Glut
import random

class Blocks:
  def __init__(self):
    self.sizeX = 2
    self.sizeY = 0.5
    self.sizeZ = 0.1
    self.borderHorizontalLimit = 0.75
    self.blockMaxDistance = 4
    self.geralPositionX = 0
    self.geralPositionY = 1
    self.geralPositionZ = -4
    self.intervalBetweenBlocks = 1.5
    color1 = self.rand_color()
    color2 = self.rand_color()
    color3 = self.rand_color()
    self.items = [[self.geralPositionX, self.geralPositionZ, color1, color2, color3]]

  def render(self):
    for block in self.items:
      positionX = block[0]
      positionZ = block[1]
      Gl.glColor3f(block[2], block[3], block[4])
      Gl.glPushMatrix()
      Gl.glTranslate(positionX, self.geralPositionY, positionZ)
      Gl.glRotate(90, 0, 0, 1)
      Gl.glScaled(self.sizeX, self.sizeY, self.sizeZ)
      Glut.glutSolidCube(1.0)
      Gl.glPopMatrix()

  def rand_color(self):
    return round(random.uniform(0, 1), 2)

  def count_of_blocks(self):
    return len(self.items)

  def remove_block(self, index = 0):
    self.items.pop(index)

  def add_new_block(self):
    newBlockX = round(random.uniform(-self.borderHorizontalLimit, self.borderHorizontalLimit), 2)
    newBlockZ = -(self.blockMaxDistance * self.intervalBetweenBlocks)
    color1 = self.rand_color()
    color2 = self.rand_color()
    color3 = self.rand_color()
    newBlock = [newBlockX, newBlockZ, color1, color2, color3]
    self.items.append(newBlock)

  def check_if_collide(self, positionX, positionZ, sizeDiametro):
    sizeRadius = sizeDiametro
    block = self.items[0]
    blockPositionX = block[0]
    blockPositionZ = block[1]

    blockIntervalX = [(blockPositionX - (self.sizeY / 2)), (blockPositionX + (self.sizeY / 2))]
    blockIntervalZ = [(blockPositionZ - (self.sizeZ / 2)), (blockPositionZ + (self.sizeZ / 2))]

    shockLeft = self.is_in_interval(blockIntervalX[0], blockIntervalX[1], (positionX + sizeRadius))
    shockRight = self.is_in_interval(blockIntervalX[0], blockIntervalX[1], (positionX - sizeRadius))

    shockZ = self.is_in_interval(blockIntervalZ[0], blockIntervalZ[1], (positionZ - sizeRadius))

    if(shockLeft or shockRight):
      if(shockZ):
        return True
    return False

  def is_in_interval(self, interval1, interval2, value):
    return (interval1 <= value <= interval2)

  def move(self, pixels):
    itemsUpdated = []
    for block in self.items:
      blockPositionX = block[0]
      blockPositionZ = block[1]
      itemsUpdated.append([blockPositionX, blockPositionZ + pixels, block[2], block[3], block[4]])
    self.items = itemsUpdated

  def auto_generate_block(self):
    if (len(self.items) == 0): return

    firstBlockPositionZ = self.items[0][1]
    lastBlockPositionZ = self.items[-1][1]

    if not(self.block_is_in_scenario(firstBlockPositionZ)):
      self.remove_block(0)
    if (self.block_is_in_scenario(lastBlockPositionZ)):
      self.add_new_block()

  def block_is_in_scenario(self, positionZ):
    if(positionZ > -self.blockMaxDistance and positionZ < (1.2 * self.blockMaxDistance)):
      return True
    else:
      return False