class circle:
  def __init__(self,r):
    self.r=r
    if r.isalpha()==True:
     raise ValueError('r is not int')

circleof=circle('helloo')
