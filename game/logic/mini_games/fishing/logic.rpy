init python:
    import os
    import random
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['images/mini_games/fishing']
    flash  = Fade(.25, 0, .5, color="#fff")
    flash2 = Fade(.25, 0, .5, color="#222")
    max_points = 100
    circlehealth = 5
    timergame = 60
    img_name = "n"
    points_minus = 1.0
    ani_time = .1
    animationcircle = 1
    animationcounter = 0
    number = 0
    plus = 1
    points = 0
    fishes = 0
    xposition = 20
    yposition = 570
    def restart():
        global timergame, fishes
        timergame = 60
        fishes = 0
    def circlerespawn():
        global circlehealth, xposition, yposition
        circlehealth = random.randint(5, 7)
        xposition = random.randint(20, 1667)
        yposition = random.randint(570, 790)
    # недавно был клик
    clicked = True
    # смена кадров анимации, если клик был недавно
    # и перерисовка экрана, чтобы увидеть изменения
    def NextFrameF():
        global points, number, plus, timergame, ani_time, animationcounter, circlehealth, fishes, animationcircle, clicked
        timergame -= ani_time
        animationcounter += 1
        # если клик был недавно, то продолжаем анимацию,
        # иначе следующего кадра не будет. пауза
        if animationcounter == 5:
            animationcircle += 1
            animationcounter = 0
            if animationcircle == 5:
                animationcircle = 1
        if clicked:
            circlehealth -= 1
        if circlehealth <= 0:
            fishes += 1
            circlerespawn()
        # уменьшение шкалы, если давно не было клика
        clicked = False
        # перерисовка экрана
        renpy.restart_interaction()
    # функция → action
    NextFrame = renpy.curry(NextFrameF)

screen clicker:
    add 'background'
    modal True
    # сбрасываем настройки игры при появлении экрана
    on "show" action [SetVariable("number", 0), SetVariable("clicked", True)] 
    # меняем кадр, если клик был недавно,
    # и проверяем на проигрыш
    timer ani_time repeat True action [NextFrame(), If(timergame <= 0, true=Return(False), false=NullAction())]
    # картинка с анимацией
    # отображаем невидимую кнопку для кликов
    # по нажатию прибавляем шкалу и устанавливаем флаг клика
    viewport:
            add '#FFF0'
            text str(int(round(timergame))) + '{color=#FFEEDE}{size=20}S{/size}{/color}' font 'fonts/h_font.ttf' size 25 xalign 0.40 yalign 0.078 color '#FFEEDE'
            text str(fishes) font 'fonts/h_font.ttf' size 25 xalign 0.922 yalign 0.078 color '#476683'
            
    imagebutton:
            idle 'fishing_circle' + str(animationcircle)
            xpos xposition
            ypos yposition
            action SetVariable('clicked', True)
    imagebutton:
            idle 'skipleft'
            xpos 1730
            ypos 150
            action SetVariable('timergame', 0)

label fishing_start:
    # всякие ненужные штуки для оформления
    pause .5
    hide txt
#    respawn()
    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
    call screen clicker # ←  игра
    # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑

    # дальше снова пошли всякие ненужные вещи:
    # показываем результаты игры
    if _return:
        # перематываем анимацию до последнего кадра
        scene expression (img_name + str(maxN))
    else:
        # перематываем анимацию до первого кадра
        $ renpy.pause(ani_time, hard=True)
        if fishes >= 0 and fishes <= 6:
            $ money += 5
            scene sc i_Fishing_1_9 with Dissolve(.5)
            "Gordon" "And you call that a catch? I can catch that much with my bare hands!"
            "[Name]" "What can I say? No bite..."
            "Gordon" "All right, just like we agreed, $ per fish."
            "Gordon" "Don't go crazy with that kind of crazy money, kid."
        if fishes >= 7 and fishes <= 20:
            $ money += 10
            scene sc i_Fishing_1_10 with Dissolve(.5)
            "Gordon" "Now that's what I'm talking about! This fish already looks delicious!"
            "Gordon" "Good job, boy!"
            "[Name]" "Thank you, I've tried my best."
            "Gordon" "Here's your reward!"
        if fishes >= 21:
            $ money += 21
            scene sc i_Fishing_1_11 with Dissolve(.5)
            "Gordon" "Mother of God! How many of them are there? Unbelievable!"
            "[Name]" "He-he-heh, I've tried my best."
            "Gordon" "I'm gonna get rich with your help, boy!"
            "Gordon" "Here's your payment. Good job!"

    hide txt
    with dissolve
    return