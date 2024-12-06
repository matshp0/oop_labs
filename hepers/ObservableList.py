class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event, callback):
        if event not in self._events:
            self._events[event] = []
        self._events[event].append(callback)

    def emit(self, event, *args, **kwargs):
        if event in self._events:
            for callback in self._events[event]:
                callback(*args, **kwargs)


class ObservableList(EventEmitter):
    def __init__(self, initial_data=None):
        super().__init__()
        self._data = initial_data if initial_data else []

    def append(self, item):
        self._data.append(item)
        self.emit('add', len(self._data) - 1)

    def remove(self, index):
        """Remove item by index."""
        if 0 <= index < len(self._data):
            removed_item = self._data.pop(index)
            self.emit('remove', index)
        else:
            print("Index out of range")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value
        self.emit('update', index, value)

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)  # Returns the length of the internal list
