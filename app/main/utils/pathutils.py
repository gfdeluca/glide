from os.path import dirname, join

MAIN_DIRECTORY = dirname(dirname(__file__))


def get_full_path(*path):
    return join(MAIN_DIRECTORY, *path)


def get_resources_path():
    return get_full_path('../resources')
