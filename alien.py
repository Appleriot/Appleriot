alien_0 = {'x positon': 0, 'y positon': 25, 'speed': 'medium'}
print(f"Your orignal positon: {alien_0['speed']}")

if alien_0['speed'] == 'slow':
    x_increation = 1
elif alien_0['speed'] == 'medium':
    x_increation = 2
else:
    # This nust be a fast alien
    x_increation = 3
alien_0['x positon'] = alien_0['x positon'] + x_increation

print(f"The new positon of alien: {alien_0['x positon']}")
