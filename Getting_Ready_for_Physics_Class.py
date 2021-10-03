# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
# point 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
# point 2
f_to_c(100)

# point 3
def c_to_f(c_temp):
  f_temp  = c_temp *(9/5) +32
  return f_temp
# point 4
c_to_f(0)
# point 5
def get_force(mass,acceleration):
  return mass*acceleration
# point 6
train_force = get_force(train_mass,train_acceleration)
print(train_force)
# point 7
print(f"The GE train supplies {train_force} Newtons of force.")
# point 8
def get_energy(mass,c=3 * 10**8):
  return mass*c**2
# point 9
bomb_energy = get_energy(bomb_mass)
# point 10 
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
# point 11
def get_work(force,distance):
  return force*distance
# point 12
train_work = get_work(train_force,train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance}")