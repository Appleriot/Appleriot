alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alein)
# Makes a empty list of alien
alien = []
# Make 30 alien
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien == 'green':
        alien['color'] = 'red'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien == 'red':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 alien
for alien in aliens[:5]:
    print(alien)
    print("...")
#S Show how many has been created
print(f"This is the number of aliens: {len(aliens)}")

print(alien_0)

alien_0['x positon'] = 0
alien_0['y positon'] = 25
print(alien_0)

new_points = alien_0['points']
print(f"You just earned {new_points} points.")

print(alien_0['color'])
print(alien_0['points'])
