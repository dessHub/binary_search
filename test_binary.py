def __init__(self, a, b):
    super(BinarySearch, self).__init__(range(b, a * b + b, b))

    self.length = a

  def search(self,value):
    index = 0
    dict_obj = {"count":0,"index": 0}

    first = 0
    last  = self.length - 1

    while last >= first :

      dict_obj["count"] = dict_obj.get("count") + 1

      mid_value = (last + first) / 2

      if value == self[mid_value]:
        dict_obj[index] = mid_value
        break
      elif value < self[mid_value]:
        last = mid_value - 1
        break
      else:
        first = mid_value + 1

    return dict_obj
