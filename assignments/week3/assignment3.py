#%%
import random

number_of_stars = int(input('You are going stargazing. How many stars do you expect to see? Give a number.'))
height = int(input('What is your camera setting for the height of the frame? Give a value without a comma.'))
width = int(input('What is your camera setting for the width of the frame? Give a value without a comma.'))

list_stars = ['x', '*', '+', ' ']
probabilities0 = [0.02, 0.2, 0.02, 0.76]

list_weather = ['clear', 'cloudy']
probabilities1 =[0.7, 0.3]
weather_condition = random.choices(list_weather, weights = probabilities1, k=1)[0]

location = input('Type in a location.')

if weather_condition == 'cloudy':
    print('The sky is cloudy tonight, sadly you won´t be able to see stars. :(')
else:
    print ('''What a wonderful sky over ''' + location + '''!''')

    star_count = 0

    for row in range(height):
        for col in range(width):
            star = random.choices(list_stars, weights = probabilities0, k=1)[0]
            print(star, end=' ')
            if star in ['x', '*', '+']:
                star_count += 1
        print()

    if star_count < number_of_stars:
        print ('Sadly, you only got to see '+ str(star_count) + ' stars. I hope you are not too disappointed.')
    elif star_count > number_of_stars:
        print ('You got to see '+ str(star_count) + ' stars! So much more than what you expected!')
    elif star_count == number_of_stars:
        print ('You got to see '+ str(star_count) + ' stars! You guessed the exact amount of stars in the sky.')
#%%
