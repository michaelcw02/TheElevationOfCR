import yaml

with open('env/config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    jawgToken = data.get('jawgToken')
    jawgEnpoint = data.get('jawgEnpoint')
    jawgEnpoint = jawgEnpoint.replace('your-access-token', jawgToken)
    