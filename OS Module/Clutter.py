# import os
# class clear_clutter:
#     def __init__(self,list, png):
#         self.list = list
#         self.png = png
#         print(f"{self.list}","\n", f"{self.png}")

#     def clear(self):
#         os.system(f"rm {self.list} {self.png}")
#         print("Clutter cleared")
# a=clear_clutter(list=(1,2,3,4,5),png=("C:\Users\Lenovo\Pictures\Saved Pictures"))
# a.clear()

class company:
    company= "Google"
    def __init__(self, name):
        self.name = name
        self.founder= "Sergey Brin"
        self.ceo = "Sundar Pichai"
        self.industry = "Technology"
        print(f"\nIndustry: {self.industry}\n\nCompany name: {self.name}\n\nFounded By: {self.founder}\n\nNow Ceo is: {self.ceo} ")
    @classmethod
    def ChangeName(cls,name):
        cls.name = name
a=company("android")
print(a.name)
a.ChangeName("Microsoft")
print(a.name)