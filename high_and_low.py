class Kata:
    def __init__(self):
        self.string = ''
        self.max = -10000000
        self.min = 10000000

    def HighAndLow(inp):
        numbers = inp.split()
        max = -10000000
        min = 10000000
        for num in numbers:
            if int(num) > max:
                max = int(num)
            if int(num) < min:
                min = int(num)
        print(f"{min} {max}")

Kata.HighAndLow(inp="1 2 3 4 5")
