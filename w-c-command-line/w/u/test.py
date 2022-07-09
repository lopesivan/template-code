import yaml
config_file = open("1.yml", 'r')
data_model = yaml.load(config_file, Loader=yaml.BaseLoader)
config_file.close()
print(data_model)
