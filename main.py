import play
from random import randint
character = []
name = []
bar1 = 1
bar2 = 1
bar3 = 1
combo = 0 #еда
combo2 = 0 #кекать
combo3 = 0 #спать
#здесь есть секретная клавиша
#здесь есть еще одна секретная клавиша (от Вероники :) ) 
custom = play.new_text(words = None, x = 0, y = 200, size = 60)
#bars
eatbar = play.new_image(image = None, x = -310, y = 200)
slbar = play.new_image(image = None, x = -310, y = 120)
ppbar = play.new_image(image = None, x = -310, y = 45)
#hats
smile = play.new_image(image = None, x = 0, y = 0, size = 100)
hat = play.new_image(image = 'hat_choose.png', x =-280, y = 100, size = 100)
nothing = play.new_image(image = 'nothing_choose.png', x = -280, y = -20, size = 100)
capka = play.new_image(image = "cap_choose.png", x = -280, y = -150, size = 100)
#accessories
glasses = play.new_image(image = 'glas_choose.png', x = -280, y = 100, size = 100)
nothing2 = play.new_image(image = 'nothing2_choose.png', x = -280, y = -40, size = 100)
swag_glasses = play.new_image(image = "swag_choose.png", x = -280,  y = -150, size = 100 )
#entities
trash = play.new_image(image = 'trash.png', x = 200, y = -20, size = 70)
speech = play.new_text(words = None, x = 0, y = -100, font = None, font_size = 50)
#hide
trash.hide()
smile.hide()
glasses.hide()
nothing2.hide()
swag_glasses.hide()
eatbar.hide()
slbar.hide()
ppbar.hide()

@play.when_program_starts
def start():
    global custom
    custom = play.new_text(words = 'Выберите внешность для своего персонажа: ', x = 0, y = 200, size = 60)
    hat.show()
    tutorial = play.new_text(words = "Нажимай на клавиши для действия со мной: 1 - погладить, 2 - покормить, 3 - убрать за мной, 4 - положить спать", x = 0, y = 0, font = None, font_size = 19, color = 'plum')
    tutorial.y = play.screen.height/2 - 30
@play.when_key_pressed('l')
def egg(key):
    if key == 'l':
        hat.hide()
        capka.hide()
        nothing.hide()
        character.append("letov_")
        trash.image = 'pops.png'
        global name
        name = ''.join(character)
        smile.image = name + 'smile.png'
        eatbar.image = str(bar1) + 'eat_bar.png'
        slbar.image = str(bar2) + 'sleep_bar.png'
        smile.show()
        slbar.show()
        eatbar.show()
        custom.hide()
        print(name)

@hat.when_clicked
def do():
    hat.hide()
    nothing.hide()
    capka.hide()
    character.append("hat_")
    glasses.show()
    nothing2.show()
    swag_glasses.show()

@nothing.when_clicked
def do2():
    hat.hide()
    nothing.hide()
    capka.hide()
    glasses.show()
    nothing2.show()
    swag_glasses.show()

@capka.when_clicked
def do5():
    hat.hide()
    nothing.hide()
    capka.hide()
    glasses.show()
    nothing2.show()
    character.append("cap_")
    swag_glasses.show()


@glasses.when_clicked
def do3():
    glasses.hide()
    custom.hide()
    nothing2.hide()
    swag_glasses.hide()
    character.append("glas_")
    global name
    name = ''.join(character)
    smile.image = name + 'smile.png'
    slbar.image = str(bar2) + 'sleep_bar.png'
    eatbar.image = str(bar1) + 'eat_bar.png'
    ppbar.image = str(bar3) + 'poop_bar.png'
    eatbar.show()
    slbar.show()
    smile.show()
    ppbar.show()
    print(name)


@nothing2.when_clicked
def do4():
    glasses.hide()
    custom.hide()
    nothing2.hide()
    swag_glasses.hide()
    global name
    name = ''.join(character)
    smile.image = name + 'smile.png'
    slbar.image = str(bar2) + 'sleep_bar.png'
    eatbar.image = str(bar1) + 'eat_bar.png'
    ppbar.image = str(bar3) + 'poop_bar.png'
    eatbar.show()
    slbar.show()
    smile.show()
    ppbar.show()
    print(name)

@swag_glasses.when_clicked
def do6():
    glasses.hide()
    custom.hide()
    nothing2.hide()
    swag_glasses.hide()
    character.append("swag_")
    global name
    name = ''.join(character)
    smile.image = name + 'smile.png'
    eatbar.image = str(bar1) + 'eat_bar.png'
    slbar.image = str(bar2) + 'sleep_bar.png'
    ppbar.image = str(bar3) + 'poop_bar.png'
    smile.show()
    eatbar.show()
    slbar.show()
    ppbar.show()
    print(name)

@play.repeat_forever
async def game():
    if play.key_is_pressed('1'):
        global combo
        global combo3
        global bar1
        global bar2
        global bar3
        bar1 = int(bar1) + 1
        bar2 = int(bar2) + 1
        combo = combo + 1
        combo3 = combo3 + 1
        eatbar.image = str(bar1) + 'eat_bar.png'
        slbar.image = str(bar2) + 'sleep_bar.png'      
        smile.image = name + 'hand.png'
        speech.words = ('Мне приятно')
        await play.timer(seconds = 2)
        smile.image = name + 'smile.png'
        speech.words = ('Это всё? А можна ещё?')
    
    if combo == 3:
        smile.image = name + 'sad.png'
        speech.words = ('Я голоден!')
        await play.timer(seconds=1)
        smile.image = name + 'pokerface.png'
        speech.words = ('Покорми меня')
        combo = 0
    
    if play.key_is_pressed('2'):
        global combo2
        print(str(bar2) + 'lalala')
        combo3 = combo3 + 1
        combo2 = combo2 + 1
        bar2 = int(bar2) + 1
        bar3 = int(bar3) + 1
        slbar.image = str(bar2) + 'sleep_bar.png'
        ppbar.image = str(bar3) + 'poop_bar.png'
        smile.image = name + 'eat.png'
        speech.words=('Ням ням ням')
        await play.timer(seconds = 1)
        bar1 = 1
        eatbar.image = str(bar1) + 'eat_bar.png'
        smile.image =(name + 'yummy.png')
        speech.words = ('Спасибо! Очень вкусно!')
    
    if combo2 == 4:
        await play.timer(seconds=1)
        ppbar.image = str(bar3) + 'poop_bar.png'
        smile.image = (name + 'mmh.png')
        trash.size = (randint(20,150))
        trash.show()
        speech.words = ("Нажми 3 чтобы убрать за мной")
        combo2 = 0
        bar3 = 1
        ppbar.image = str(bar3) + 'poop_bar.png'
    
    if play.key_is_pressed('9'):
        smile.image =('easteregg.png')
        speech.words=('Вероника молодчина!')
        await play.timer(seconds=1)
        speech.words = ''
        await play.timer(seconds=1)
        smile.image = ('smile.png')

    if play.key_is_pressed('8'):
        smile.image =('easteregg1.png')
        speech.y = -140
        speech.words=('Андрей умничка:3')
        await play.timer(seconds=2)
        speech.words = ''
        await play.timer(seconds=1)
        smile.image =('easteregg2.png')
        await play.timer(seconds=1)
        smile.image = (name + 'smile.png' )
        speech.y = -80

    if play.key_is_pressed('3'):
        combo3 = combo3 + 11
        print(str(bar2) + 'azaza')
        bar2 = int(bar2) + 1
        slbar.image = str(bar2) + 'sleep_bar.png'
        trash.hide()
        smile.image= (name + 'wow.png')
        speech.words = ("Спасибо...")
        await play.timer(seconds=2)
        smile.image = (name + 'smile.png')

    if combo3 == 8:
        await play.timer(seconds=1)
        speech.words=("Я хочу спать")
        smile.image=(name + 'sleepy.png')
        await play.timer(seconds=1)
        speech.words=("Нажми 4 чтобы положить меня спать")
        combo3 = 0
        slbar.image = str(bar2) + 'sleep_bar.png'

    if play.key_is_pressed('4'):
        smile.image=(name + 'sleep.png')
        speech.words = ('zZzZzZz')
        await play.timer(seconds=4)
        bar2 = 1
        slbar.image = str(bar2) + 'sleep_bar.png'
        smile.image = name + 'sleepy.png'
        speech.words = ('Доброе утро!')
        await play.timer(seconds=1)
        smile.image = name + 'smile.png'
        speech.words =('')

play.start_program()