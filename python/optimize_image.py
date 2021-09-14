from optimize_images import get_maximuns, optimize

collection = 'single'
path = '/home/cpicanco/pictures/carlop/'
maximuns = get_maximuns(collection)
files = [path+collection+'/quando-a-vi-passar/01.jpg']
for file in files:
  optimize(file, maximuns, path+collection)