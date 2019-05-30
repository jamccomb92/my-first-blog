if 1 > 2:
    print('Hello Django Girls!')
else:
    print('Sorry')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi(name):
    print('Hi there ' + name + '!')
    print('How are you')

hi('joe')

girls = ['Rachel', 'Monica', 'Pheobe', 'Ola', 'Bridget']

for name in girls:
    hi(name)
    print('Next girl...')
