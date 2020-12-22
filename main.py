def rozciagniecie(plansza, x, y):
  list_of_x = range(-1,2)
  list_of_y = range(-1,2)
  for row in list_of_y:
    for col in list_of_x:
      ix = col
      iy = row
      while plansza[y][x] == ".":
        x += ix
        y += iy
    

  return x, y