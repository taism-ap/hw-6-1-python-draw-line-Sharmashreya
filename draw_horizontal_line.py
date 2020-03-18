from PIL import Image

def draw_horizontal_line(start, y1, finish, y2):
  img = Image.new("1",[100,100])
  pixels = img.load()
  if y1 == y2:
    if finish > start:
      for i in range(finish - start):
        pixels[(start + i), y1] = (1)
    if start > finish:
      for i in range(start - finish):
        pixels[(finish + i), y1] = (1)
  if y1 != y2:
    print("intended line would not be horizontal")
  img.save('horizontal_line.png')
  img.close()

x = draw_horizontal_line(20,10,50,10)
print(x)
