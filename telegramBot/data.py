import simpleyaml as yaml

def configure():
    # Read configuration
    file = open("config/parameters.yml", "r")
    config = yaml.load(file)
    file.close()
    return config
