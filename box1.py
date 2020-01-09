class area():
    length, width

class box ():
    length, width
    #type = row of the excel file
    mass = box.length * box.width
    x,y
    read_from_file
    randomize_location
    def compute_force (critical_box,constants)
        force_x , force_y = 0
        for box in boxes - box:
            dist = sqrt ((critical_box.x - box.x )^2 + (critical_box.y - box.y )^2 )
            # repulsion
                temp = repulsion_constant * box.mass / dist^3
                force_x = temp * (critical_box.x - box.x )
                force_y = temp * (critical_box.y - box.y )
            # attraction
                if box.type == critical_box.type:
                    temp = repulsion_constant * box.mass / dist^3                    
                    force_x = attraction_constant * box.mass * (box.x - critical_box.x) / dist^3 
                    force_y = attraction_constant * box.mass * (box.y - critical_box.y) / dist^3 
            # noise
                force_x = noise_constant * random_unform (-1,+1),
                force_y = noise_constant * random_unform (-1,+1),
def move(force)
    box.x += force_x
        box.y += force_y

boxes = boxes.read_from_file ('filename.xlxs')
boxes = boxes.randomize_location (boxes, area)
plot(boxes,area)
for box in boxes:
    constants = evolve_constants()
    force = boxes.compute_force (box,constants)
    boxes.move(force)