import play
character = []
name = []
#здесь есть секретная клавиша
#здесь есть еще одна секретная клавиша
custom = play.new_text(words = None, x = 0, y = 200, size = 60)
# smile = play.new_image(image = 'smile.png', x = 0, y = 0, size = 100)
eat = play.new_image(image = 'apple.png', x = 0, y = 0, size = 90)
hand = play.new_image(image = 'hand2.png', x = 0, y = 0, size = 90)
smile = play.new_image(image = None, x = 0, y = 0, size = 100)
hat = play.new_image(image = 'hat_choose.png', x =-200, y = 80, size = 100)
glasses = play.new_image(image = 'glas_choose.png', x = -200, y = -80, size = 100)
nothing = play.new_image(image = 'nothing_choose.png', x = -200, y = -160, size = 100)
trash = play.new_image(image = 'trash.png', x = 60, y = -40, size = 70)
trash.hide()
eat.hide()
smile.hide()
glasses.hide()
hand.hide()
speech = play.new_text(words = None, x = 0, y = -80, font = None, font_size = 50)

@play.when_program_starts
def start():
    custom = play.new_text(words = 'Выберите внешность для своего персонажа: ', x = 0, y = 200, size = 60)
    hat.show()
    tutorial = play.new_text(words = "Нажимай на клавиши для действия со мной: 1 - погладить, 2 - покормить, 3 - убрать за мной, 4 - положить спать", x = 0, y = 0, font = None, font_size = 19, color = 'plum')
    tutorial.y = play.screen.height/2 - 30

@hat.when_clicked
def do():
    hat.hide()
    character.append("hat_")
    glasses.show()
    nothing.hide()

@nothing.when_clicked
def do2():
    hat.hide()
    glasses.show()
    nothing.hide()

@glasses.when_clicked
def do3():
    glasses.hide()
    character.append("glas_")
    global name
    name = ''.join(character)
    smile.image = name + 'smile.png'
    smile.show()
    print(name)

@play.repeat_forever
async def game():
    if play.key_is_pressed('1'):
        smile.hide()
        hand.show()
        speech.words = ('Мне приятно')
        await play.timer(seconds = 2)
        smile.show()
        speech.words = ('Это всё? А можна ещё?')
    
    if play.key_is_pressed('2'):
        smile.image = name + 'wow.png'
        eat.show()
        speech.words=('Ням ням ням')
        await play.timer(seconds = 1)
        eat.hide()
        smile.image =(name + 'yummy.png')
        speech.words = ('Как вкусно!')
        await play.timer(seconds = 2)
        smile.image = (name + 'mmh.png')
        trash.show()
        speech.words = ("Нажми 3 чтобы убрать за мной")
    
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
        trash.hide()
        smile.image= (name + 'wow.png')
        speech.words = ("Спасибо...")
        await play.timer(seconds=1)
        smile.image = (name + 'smile.png')
        await play.timer(seconds=3)
        speech.words=("Я хочу спать")
        smile.image=(name + 'sleepy.png')
        await play.timer(seconds=1)
        speech.words=("Нажми 4 чтобы положить меня спать")
    if play.key_is_pressed('4'):
        smile.image=(name + 'sleep.png')
        speech.words = ('zZzZzZz')


play.start_program()