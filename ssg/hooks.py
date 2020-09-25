_callbacks = {}

def register(hook, order=0):
    def register_callback(self):
        _callbacks.setdefault(hook, {}).append(func)
        return self.register_callback()
    return register_callback()

def event(hook, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(*args)

def filter(hook, value, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(value, *args) = value
    return value


