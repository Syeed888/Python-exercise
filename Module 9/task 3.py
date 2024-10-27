from Car import car

car1 = car('ABC-123', 142, 0, 2000)
print(f"""
Registration number: {car1.registration_number}
Maximum speed: {car1.maximum_speed}
Current speed: {car1.current_speed}
Travelled distance: {car1.travelled_distance}
"""
)
car1.accelerate(60)
car1.drive(1.5)

print(f"Current speed: {car1.current_speed}")
print(f"Travelled distance: {car1.travelled_distance}")