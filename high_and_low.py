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
    
    def ArrayDiff(list1, list2):
        list_temp = list1
        for elem2 in list2:
            for elem1 in list1:
                if elem2 == elem1:
                    list1.remove(elem1)
        return list1
                


Kata.HighAndLow(inp="1 2 3 4 5")
ans = Kata.ArrayDiff(list1=[1, 2, 3, 4, 5], list2=[0, -9, 3])
print(ans)