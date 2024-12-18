# combo operands
# i enjoyed CPU architecture in college

class ChronospatialComputer:
    
    def __init__(self, ai, bi = 0, ci = 0):
        self.instructions = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        self.a = ai
        self.b = bi
        self.c = ci
        self.pc = 0 # program counter
        self.output = []
        print('A: {}\tB: {}\t C:{}'.format(ai,bi,ci))
    
    def run_program(self, program):
        print(program)
        while self.pc != len(program):
            print(int(program[self.pc]), int(program[self.pc+1]))
            self.cycle(int(program[self.pc]), int(program[self.pc+1]))
            
    def flush(self):
        print(','.join(self.output))
        
    # clock cycle, call an opcode    
    def cycle(self, opcode, operand):    
        self.instructions[opcode](operand)
    
    def get_combo(self, val):
        if val in [0, 1, 2, 3]:
            return val
        elif val == 4:
            return self.a
        elif val == 5:
            return self.b
        elif val == 6:
            return self.c
        else:
            print("Program error!")
        
    # below are opcode instructions
    def adv(self, combo):
        self.a = int(self.a / pow(2, self.get_combo(combo)))
        self.pc += 2

    def bxl(self, literal):
        self.b = self.b ^ literal
        self.pc += 2

    def bst(self, combo):
        self.b = self.get_combo(combo) % 8
        self.pc += 2

    def jnz(self, literal):
        if self.a == 0:
            self.pc += 2
        else:
            self.pc = literal

    def bxc(self, literal):
        # literal not used in this
        self.b = self.b ^ self.c
        self.pc += 2

    def out(self, combo):
        self.output.append(str(self.get_combo(combo) % 8))
        self.pc += 2

    def bdv(self, combo):
        self.b = int(self.a / pow(2, self.get_combo(combo)))
        self.pc += 2

    def cdv(self, combo):
        self.c = int(self.a / pow(2, self.get_combo(combo)))
        self.pc += 2

if __name__ == '__main__':
    with open('input.txt') as f:
        _, a = f.readline().strip().split(':')
        _, b = f.readline().strip().split(':')
        _, c = f.readline().strip().split(':')
        _, ops = f.read().strip().split(':')
        ops = ops.split(',')
    
    pc = ChronospatialComputer(int(a), int(b), int(c))
    pc.run_program(ops)
    pc.flush()

# part 2 requires more brain power than i currently have