import os.path
import codecs
import configparser


def create(path, type='std'):
    if type == 'profile':
        config = configparser.ConfigParser()
        config.add_section('General')
        config.set('General', 'fullname', 'empty')
        config.set('General', 'status', 'empty')
        config.set('General', 'birthday', 'empty')
        config.set('General', 'line', 'empty')
        config.set('General', 'geoposition', 'empty')
        config.set('General', 'home', 'empty')
        config.add_section('Contacts')
        config.set('Contacts', 'phone', 'empty')
        config.set('Contacts', 'VK', 'empty')
        config.set('Contacts', 'Twitter', 'empty')
        config.set('Contacts', 'Ask', 'empty')
        config.set('Contacts', 'Instagram', 'empty')

        set(path, config_ref=config)
        # with codecs.open(path, "w", "utf-8") as config_file:
        #     config.write(config_file)


def get(path, section=None, setting=None):
    if not section:
        if not os.path.exists(path):
            print('Ooops')
            print(path)
            exit()
            # create(path)
        config = configparser.ConfigParser()
        # with codecs.open(path, "w", 'utf-8') as config_file:
        #     config.read_file(config_file)
        config.read(path)
        return config
    else:
        value = get(path).get(section, setting)
        # value = codecs.encode(value, 'utf-8')
        # value = get(path).read_file(section, setting)
        return value


def set(path, section=None, setting=None, value=None, config_ref=None):
    if not section and isinstance(config_ref, configparser.ConfigParser):
        with codecs.open(path, "w", 'utf-8') as config_file:
            config_ref.write(config_file)
    else:
        config = get(path)
        config.set(section, setting, value)
        set(path, config_ref=config)


def delete(path, section=None, setting=None):
    config = get(path)
    if section:
        if setting:
            config.remove_option(section, setting)
        else:
            config.remove_section(section)
        set(path, config_ref=config)
