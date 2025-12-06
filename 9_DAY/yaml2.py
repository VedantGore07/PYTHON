import yaml

python_data = {
    'product' : 'Laptop',
    'price' : 1200,
    'features' : ['SSD','8GB RAM', 'FullHD']
}

# To a string
yaml_output = yaml.dump(python_data)
print(yaml_output)

# to a file
with open('output.yaml','w') as file:
    yaml.dump(python_data, file)


    






















