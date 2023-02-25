class vijayawada():
    def placename(self):
        print("vijayawada placename is KLU")
    def student(self):
        print("Yes - vijayawada")
    def which_year(self):
        print("3rd year")
class Hyd():
    def placename(self):
        print("Hyd placename is Hyd-KLU")
    def student(self):
        print("Yes - Hyd")
    def which_year(self):
        print("3rd Year - Hyd")
obj_vij = vijayawada()
obj_Hyd = Hyd()
for details in (obj_vij, obj_Hyd):
    details.placename()
    details.student()
    details.which_year()
