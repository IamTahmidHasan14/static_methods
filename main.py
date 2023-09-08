class Students3:

  def __init__(self, num):
    self.num = num

  def addwithnum(self, n):
    self.num = self.num + n

  @staticmethod
  def add(a, b):
    return a + b


s3 = Students3(5)
print(s3.num)
s3.addwithnum(7)
print(s3.num)

# print(Students3.add(6, 9))
print(s3.add(6, 9))