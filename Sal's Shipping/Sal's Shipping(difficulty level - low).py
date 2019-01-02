# finding the cheapest shipping method
flat_charge = 20
prem_ground_ship = 125.00

def cost_of_ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + flat_charge
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + flat_charge
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + flat_charge
    return cost
  elif weight > 10:
    cost = weight * 4.75 + flat_charge
    return cost
  
def cost_of_drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00 
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00 
    return cost
  elif weight > 10:
    cost = weight * 14.25 
    return cost
  
def cheapest_method(weight):
  ground_ship = cost_of_ground_shipping(weight)
  drone_ship = cost_of_drone_shipping(weight)
  if drone_ship > ground_ship and prem_ground_ship > ground_ship:
    return 'The cheapest method is ground shipping = ' + str(ground_ship)
  elif ground_ship > drone_ship and prem_ground_ship > drone_ship:
    return 'The cheapest method is drone shipping = ' + str(drone_ship)
  else:
    return prem_ground_ship
    
#example  
print(cheapest_method(41.5))