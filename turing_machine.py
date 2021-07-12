class Turing_Machine:
    def __init__(
        self,
        states,
        input_alphabet,
        tape_alphabet,
        initial_state,
        blank_symbol,
        final_states,
        id='generated_mt'
    ):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states
        self.id = id

    def __str__(self):
        return f'MT(\n' \
               f'\t{[id for id in self.states]},\n' \
               f'\t{self.input_alphabet}\n' \
               f'\t{self.tape_alphabet}\n' \
               f'\tdeltas,\n' \
               f'\t{self.blank_symbol},\n' \
               f'\t{self.initial_state.id},\n' \
               f'\t{[state.id for state in self.final_states]},\n' \
               f')'

    def accept(self, original_tape, initial_index=0, verbose=False):
        if not self.validate_tape(original_tape):
            return False
        current_index = initial_index
        head = None
        tape = [smbl for smbl in original_tape]
        current_state = self.initial_state

        while current_state not in self.final_states:
            if verbose:
                print(f'State: {current_state.id}\nLookin to: {tape[current_index]}\nTape: {tape}\n')

            symbol_read = tape[current_index]
            trio = current_state.deltas[symbol_read]
            if trio is None:
                continue

            next_state, write_symbol, direction = trio
            tape[current_index] = write_symbol
            current_state = self.states[next_state]
            if current_index == 0 and direction == 'L':
                aux = ['B']
                aux.extend(tape)
                tape = aux
            if current_index == (len(tape) - 1) and direction == 'R':
                tape.append('B')
            current_index += 1 if direction == 'R' else -1
        return True

    def validate_tape(self, tape):
        return all([symbol in self.input_alphabet for symbol in tape])
