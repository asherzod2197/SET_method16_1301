# ISSUPERSET
class MySet:
    def __init__(self):
        self.data = []

    def issuperset(self, other):
        for item in other.data:
            if item not in self.data:
                return False
        return True

    def show(self):
        print(self.data)

s3 = MySet()
s3.data = [2, 5]

print(s1.issuperset(s3))  
