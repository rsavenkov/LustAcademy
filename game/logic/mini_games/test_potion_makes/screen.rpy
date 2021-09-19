screen test_potion_makes:
    default return_reagents = []
    vpgrid:
        cols 4
        rows 3
        xalign .5
        yalign .8
        for i in reagents_shuffle:

            viewport:
                xmaximum 285
                ymaximum 60

                imagebutton:
                    hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))

                    if i in return_reagents:
                        idle im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))
                        action Function(return_reagents.remove, i)
                    else:
                        idle 'order_start_button'
                        action Function(return_reagents.append, i)

                text reagents[i] font 'fonts/h_font.ttf' size 20 color '#FFFFFF' xalign .5 yalign .45
    viewport:
        xmaximum 285
        ymaximum 60
        xalign .5 yalign .9
        imagebutton:
            idle 'order_start_button'
            hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))

            action Return(return_reagents)

        text 'Placed' font 'fonts/h_font.ttf' size 30 color '#FFFFFF' xalign .5 yalign .45
    viewport:
        xmaximum int(285*.71)
        ymaximum int(60*.71)
        imagebutton:
            idle Transform('mini_games/caffe/order_start_button.png', zoom = .7)
            hover Transform(im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3)), zoom = .7)

            action Return('Skip')

        xalign .95 yalign .935
        text 'Skip' font 'fonts/h_font.ttf' size 20 color '#FFFFFF' xalign .5 yalign .45
    













label test_potion_makes_label:
    $ reagents = {

1:'Unicorn hair powder',
2:'Tears of woodland deer',
3:'Icelandic cetraria',
4:'Dragon scales powder',
5:'Bouncing berries',
6:'Fireblossom leaves',
7:'Mermaid blood',
8:'Butterfly wings',
9:'Manticore lard',
10:'Dryad leaves',
11:'Dry vampire blood',
12:'Dandelion dust',

}
    $ reagents_wins    = [1, 2, 3]
    $ reagents_shuffle = reagents.keys()
    $ renpy.random.shuffle(reagents_shuffle)

    hide screen main_interface
    show sc i_Sabrina_0_1
    with Dissolve(.5)
    "[Name]" "Miss Spellman, I'd like to practice my potions."
    show sc i_Sabrina_0_3 with my_dissolve
    "Sabrina" "That's great! Do you remember the safety rules?"
    show sc i_Sabrina_0_3 with my_dissolve
    "[Name]" "Of course! No sticking your head in the cauldron, no pissing on charcoal, no sniffing powders."
    show sc i_Sabrina_0_9 with my_dissolve
    "Sabrina" "That's about right, [Name]. Well, please, to the boiler."
    show sc i_Sabrina_1_44 with my_dissolve
    "Sabrina" "So, what's on the menu today, chef?"

    menu:
        "Lesser Heal Potion" if True:
            $ potion_tmp = 'Lesser Heal Potion'
    $ ShowMessage("Recipe of the Lesser Heal Potion: \nTears of woodland deer\nUnicorn hair powder\nIcelandic cetraria")
    show sc i_Sabrina_1_44 with my_dissolve
    "[Name]" "Today we are going to make [potion_tmp], ma'am."
    show sc i_Sabrina_1_44 with my_dissolve
    "Sabrina" "That's a great idea. Proceed with the choice of reagents."
label test_potion_makes_label_begin:
    scene sc i_Sabrina_1_44 with Dissolve(.5)
    $ tss = renpy.call_screen('test_potion_makes')
    if type(tss) != type('!'):
        $ tss.sort()
    if tss == 'Skip':

        scene sc i_Sabrina_1_40 with Dissolve(.5)
        "Sabrina" "Unfortunately, you didn't succeed today, [Name]."
        "Sabrina" "I hope you'll be better prepared next time."
        show sc i_Sabrina_1_45 with my_dissolve

        if hasattr(store, 'tmpsss'):
            $ del tmpsss
        "Sabrina" "That concludes our lesson! I look forward to seeing you all at the next class!"
        jump exit_from_event

    if tss == reagents_wins:
        if hasattr(store, 'potions'):
            $ potions['Lesser Heal'] += 1
        scene sc i_Sabrina_1_37 with Dissolve(.5)

        #if not hasattr(store, 'receive_lesser_heal'): 
        $ ShowMessage(['images/potion_mini.png', "         You receive {b}Lesser Heal{/b}"])
        $ receive_lesser_heal = True
        "Sabrina" "Congratulations. You've got a pretty good [potion_tmp]."
        show sc i_Sabrina_1_41 with my_dissolve
        "Sabrina" "As is tradition, you can keep the potion you've made."
        jump test_potion_makes_label_final_2
    elif True:

        if hasattr(store, 'tmpsss'):
            jump test_potion_makes_label_final
        scene sc i_Sabrina_1_39 with Dissolve(.5)

        "Sabrina" "Um... That's no way to boil [potion_tmp]."

        show sc i_Sabrina_1_43 with my_dissolve
        "Sabrina" "Try again from the beginning."
        $ reagents = {

1:'Unicorn hair powder',
2:'Tears of woodland deer',
3:'Icelandic cetraria',
4:'Dragon scales powder',
5:'Bouncing berries',
6:'Fireblossom leaves',
7:'Mermaid blood',
8:'Butterfly wings',
9:'Manticore lard',
10:'Dryad leaves',
11:'Dry vampire blood',
12:'Dandelion dust',

}
        $ reagents_wins    = [1, 2, 3]
        $ reagents_shuffle = reagents.keys()
        $ renpy.random.shuffle(reagents_shuffle)

        $ tmpsss = 1


        jump test_potion_makes_label_begin
    scene sc i_Sabrina_1_45 with Dissolve(.5)
    $ tss = renpy.call_screen('test_potion_makes')
    $ tss.sort()
    if tss == 'Skip':
        jump test_potion_makes_label_final
    if tss == reagents_wins:

        #if not hasattr(store, 'receive_lesser_heal'): 
        $ ShowMessage(['images/potion_mini.png', "          You receive {b}Lesser Heal{/b}"])
        $ receive_lesser_heal = True

        show sc i_Sabrina_1_37 with my_dissolve
        "Sabrina" "That's perfect! There's just one little touch left. And that would be...?"
    elif True:
        jump test_potion_makes_label_final
    scene sc i_Sabrina_1_45 with Dissolve(.5)

    $ tss = renpy.call_screen('test_potion_makes')
    $ tss.sort()

    show sc i_Sabrina_1_47 with my_dissolve

    if tss == reagents_wins:
        if hasattr(store, 'potions'):
            $ potions['Lesser Heal'] += 1
        "Sabrina" "Congratulations. You've got a pretty good [potion_tmp]."

    "Sabrina" "As is tradition, you can keep the potion you've made."

    jump test_potion_makes_label_final_2
label test_potion_makes_label_final:

    scene sc i_Sabrina_1_36 with Dissolve(.5)
    "Sabrina" "It's a shame to make a mistake at the end."
label test_potion_makes_label_final_1:
    show sc i_Sabrina_1_40 with my_dissolve
    "Sabrina" "Unfortunately, you didn't succeed today, [Name]."
    "Sabrina" "I hope you'll be better prepared next time."
    show sc i_Sabrina_1_45 with my_dissolve
label test_potion_makes_label_final_2:
    if hasattr(store, 'tmpsss'):
        $ del tmpsss
    "Sabrina" "That concludes our lesson! I look forward to seeing you all at the next class!"
    jump exit_from_event
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
