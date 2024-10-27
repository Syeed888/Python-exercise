from Car import car

car1 = car('ABC-123', 142)
print(f"""
Registration number: {car1.registration_number}
Maximum speed: {car1.maximum_speed}
Current speed: {car1.current_speed}
Travelled distance: {car1.travelled_distance}
"""
)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"Current speed: {car1.current_speed}")
car1.accelerate(-200)
print(f"Final speed after brake : {car1.current_speed}")