# https://martin-thoma.com/configuration-files-in-python/
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.Loader)

for section in cfg:
    print(section)
print(cfg["mysql"])
print(cfg["other"])