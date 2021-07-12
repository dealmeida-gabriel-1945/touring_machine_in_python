from turing_machine_builder import create_mt_01

mt = create_mt_01()
tape = ['0', '0', '0', '1', '1', '1']
initial_index = 0
print(mt)
if mt.accept(tape, initial_index=initial_index, verbose=True):
    print('This Turing Machine accepted the tape!')
else:
    print("This Turing Machine didn't accept the tape!")
