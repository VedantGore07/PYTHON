import yaml

yaml_string = """
name: Alice
age: 30
city: New York
"""

data = yaml.safe_load(yaml_string)
print(data)