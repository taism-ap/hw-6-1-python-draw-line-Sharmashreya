def draw_horizontal_lines():
  import random as rand
  img = Image.new("1",[100,100])
  pixels = img.load()
  for i in range(rand.randint(0,10)):
    x1 = rand.randint(0,100)
    x2 = rand.randint(0,100)
    y = rand.randint(0,100)
    if x2 > x1:
      for i in range(x2 - x1):
        pixels[(x1 + i), y] = (1)
      if x1 > x2:
        for i in range(x1 - x2):
          pixels[(x2 + i), y] = (1)
  img.save('horizontal_lines.png')
  img.close()

y = draw_horizontal_lines
print(y)
