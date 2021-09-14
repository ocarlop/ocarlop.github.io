import yaml

# iterate recursively to create _data files based on img/albuns trees

# img/albuns/
input_img_folder = 'img/albuns/'

[{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(r'E:\data\store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)