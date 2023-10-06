def singleton(cls):
    def wrapper(*args, **kwargs):
        print('Trying to create class')
        if not wrapper.singleton_instance:
            print('Creating new singleton')
            wrapper.singleton_instance = cls(*args, **kwargs)
        print('Returning instance')
        return wrapper.singleton_instance
    wrapper.singleton_instance = None
    return wrapper
