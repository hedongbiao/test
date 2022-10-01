#全局变量


_global_dict = {}


def _init():
    global _global_dict



def set_value(key,value):
    _global_dict[key] = value

def get_value(key,defvalue=None):

    try:

        return  _global_dict[key]
    except KeyError:
        return defvalue