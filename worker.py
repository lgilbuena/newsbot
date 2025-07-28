import config

def modify_data(setting,val):
    if setting == 0:
        config.query.append(val)
    elif setting == 1:
        config.channel_id = val

def get_data(setting):
    if setting == 0:
        return config.query
    elif setting == 1:
        return config.channel_id