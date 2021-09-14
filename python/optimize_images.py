import os
from pathlib import Path
from glob import glob
from PIL import Image

maximum_size_full = 1920, 1920
maximum_thumbnail = 400, 400

def get_maximuns(collection):
  return {
    '_collections/'+'_'+collection:(maximum_size_full, '.jpg'),
    'assets/img/'+collection:(maximum_thumbnail, '.400.jpg')}

def optimize(file, maximuns, input_path):
  print(file, ': was ', os.stat(file).st_size)
  image = Image.open(file)
  for root, (size, extension) in maximuns.items():
    output_file = os.path.splitext(file.replace(input_path, root))[0]+extension
    Path(os.path.dirname(output_file)).mkdir(parents=True, exist_ok=True)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(output_file,dpi=[300,300],optimize=True,quality=70)
    print(output_file, ': now ', os.stat(output_file).st_size)

if __name__ == '__main__':
  collections = [
    'album',
    'ensaio',
    'ensaio-fotografico',
    'posts',
    'single']

  for collection in collections:
    maximuns = get_maximuns(collection)
    input_path = '/home/cpicanco/pictures/'+'_'+collection
    search_pattern = input_path+'/**/*.jpg'
    files = glob(search_pattern, recursive = True)
    for file in files:
      optimize(file, maximuns, input_path)
