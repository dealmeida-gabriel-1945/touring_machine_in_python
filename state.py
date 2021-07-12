class State:
    def __init__(self, id, deltas, initial, final):
        self.id = id
        self.deltas = deltas
        self.initial = initial
        self.final = final

    def deltas_to_string(self):
        return f'{[self.deltas[symbol] for symbol in self.deltas]}'
