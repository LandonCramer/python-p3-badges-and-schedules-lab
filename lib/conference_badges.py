def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    list_names = []
    for name in names:
        list_names.append(f"Hello, my name is {name}.")
    return list_names
def assign_rooms(names):
    rooms = range(1,9)
    
    room_assign = []
    for room in rooms:
        room_assign.append(f"Hello, {names[room -1]}! You'll be assigned to room {room}!")
    return room_assign    

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assign in assign_rooms(names):
        print(assign)