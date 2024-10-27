from Car import car

car1 = car('ABC-123', 142)
print(f"""
Registration number: {car1.registration_number}
Maximum speed: {car1.maximum_speed}
Current speed: {car1.current_speed}
Travelled distance: {car1.travelled_distance}
"""
)
