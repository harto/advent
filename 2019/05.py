class Program:
    def __init__(self, mem):
        self.mem = mem
        self.ip = 0

    def exec(self):
        while True:
            op = self.mem[self.ip] % 100
            if op == 99: break
            method, arity = {
                1: (self._add, 3),
                2: (self._mult, 3),
                3: (self._store, 1),
                4: (self._print, 1),
                # 5: (self._jump_if_true, 2),
            }[op]
            method(*self._read_params(arity))
            self.ip += arity + 1

    def _read_params(self, n):
        modes = self.mem[self.ip] // 100
        params = []
        for i in range(n):
            params.append((self.mem[self.ip + 1 + i], modes % 10))
            modes //= 10
        return params

    def _resolve(self, param):
        val, mode = param
        return self.mem[val] if mode == 0 else val

    def _add(self, x, y, loc):
        self.mem[loc[0]] = self._resolve(x) + self._resolve(y)

    def _mult(self, x, y, loc):
        self.mem[loc[0]] = self._resolve(x) * self._resolve(y)

    def _store(self, loc):
        self.mem[loc[0]] = int(input('input: '))

    def _print(self, x):
        print(self._resolve(x))

with open('input/05') as f:
    prog = Program([int(x) for x in f.read().strip().split(',')])
    prog.exec()
