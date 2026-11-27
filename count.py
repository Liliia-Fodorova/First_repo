from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for value in self.data:
            if value.isdigit():
               count += 1
        return count  
     
text = NumberString("Hello123World45")
print(text.number_count())