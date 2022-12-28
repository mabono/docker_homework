import yaml

with open('config/config.yaml') as f:
    data_dict = yaml.load(f, Loader=yaml.SafeLoader)


if data_dict['isWeatherGoodToday']:
    print("The weather is good today")
else:
    print("The weather is bad today")