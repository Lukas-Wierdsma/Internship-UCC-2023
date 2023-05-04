# https://martin-thoma.com/configuration-files-in-python/
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.Loader)

for section in cfg:
    print(section)
    # mysql
    # other
print(cfg["mysql"])
# {'host': 'localhost', 'user': 'root', 'passwd': 'my secret password', 'db': 'write-math'}
print(cfg["other"])
# {'preprocessing_queue': ['preprocessing.scale_and_center', 'preprocessing.dot_reduction', 'preprocessing.connect_lines'], 'use_anonymous': True} """