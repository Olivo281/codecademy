class School:
  def __init__(self,name,level,numberofstudents):
    self.name = name
    self.level = level
    self.numberofstudents = numberofstudents
  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_numberofstudents(self):
    return self.numberofstudents
  
  def set_numberofstudents(self, students):
    self.numberofsudents = students

  def __repr__(self):
    return "A {} school named {} with {} students".format(self.level,self.name,self.numberofstudents)

Northbrook = School("Northbrook", "High", 1000)
print(Northbrook.get_name())
print(Northbrook.get_numberofstudents())
print("")

class PrimarySchool(School):
  def __init__(self,name,numberofstudents,pickuppolicy):
    super().__init__(name,"Primary",numberofstudents)
    self.pickuppolicy = pickuppolicy
  def get_pickuppolicy(self):
    return self.pickuppolicy
  def __repr__(self):
    return super().__repr__() + " | Pick up policy: {}".format(self.pickuppolicy)

class HighSchool(School):
  def __init__(self,name,numberofstudents,sportsteam):
    super().__init__(name,"High",numberofstudents)
    self.sportsteam = sportsteam
  def get_sportsteam(self):
    return self.sportsteam
  def __repr__(self):
    return super().__repr__() + " | Sports team : {}".format(self.sportsteam)
  
housman = PrimarySchool("Housman",2000,"Parent or guardian must pick up students")
print(housman.__repr__())
print("")
Stradford = HighSchool("Stradford",5000, 'Spartans')
print(Stradford.__repr__())
