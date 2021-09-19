init 1000 python:
    if mp.tutorial is None:
        mp.tutorial = {
        'CHARACTER INFO':False,
        'LUSTOGRAM'     :False,
        'HUD INTERFACE' :False,
        'CAFE'          :False,
        'DUELING ARENA' :False,
        'CALENDAR'      :False,
     
        }
        mp.save()
    def set_tutorial(what):
        global mp
        mp.tutorial[what] = True
        mp.save()

    tutorials = {

    'CHARACTER INFO': [
    '{size=15}Here you can find information about every character you’ve met: their description,{/size}\n {size=15}relationship towards your hero, quest logs, and list of interesting scenes{/size}',
    '{size=15}List of all characters in game, sorted from A to Z and their current route progression. You can click on any character from the list to get more detailed info.{/size}', 
    


    #'Use the star icon to mark favorite characters. They will always appear at the top of the list.',
    'Click here to find a short character description, including full name, age, etc.',
    'This bar represents the history of the relationship with this character. You can click on the completed steps to refresh your memory.',
    #'This icon means that at this step, the story of the relationship with the character is suspended in the current release of the game but will continue in the future.',
    'Learn the requirements for the next step of this route, as well as the place and time for the next scene.',
    #'When the requirements are met, this status bar will turn green and you’ll get access to the fast travel button that will get you to the scene.',
    'You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!'

    ],


    'LUSTOGRAM':[
    

    '{size=15}This app is for sharing and discussing photos.{/size}\n{size=15}Here you can see new photos{/size}\n{size=15}of people you’ve met and leave your comments.{/size}',
    'Here is the list of all people you’ve already met. They are sorted by the follower count, starting with the most popular. You can chose anyone from the list to open his or her profile.',
    'Click on this icon to return to the character list',
    'Click on this photo to expand it to fullscreen.',
    'Here’s authors caption with hashtags you can use to find similar photos in the app.',
    'Here are the comments other people left for this photo. You can click on any name to open their personal page.',
    'Here you can leave a like and write your own comment.',
    'You can choose one of the suggested options to leave a comment. Sometimes choices may afflict your relationship, but most of the time they have no consequences. ',
    'Click on the photo if you want to return to the previous page.',
    'Click on this button to open your live feed and see all photos in app.',
    'This feed features all the photos from people you’ve already met. Scroll down and up tho view them all.',
    'To go the person’s personal page click on his/her avatar.',
    'Click on the photo to switch to the fullscreen view.',
    'To exit the app and turn off your phone, tap this button or just click past the smartphone screen.',
    'You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!'



    ],


    'HUD INTERFACE':[
    


    '{size=20}We recommend a short introductory tutorial{/size}\n{size=20} to learn the purpose of all{/size}\n{size=20} the elements of the main interface{/size}\n{size=20} and how to use them to simplify the game.{/size}',
    "{size=13}Here you can see the current time of day. Altogether there are four: morning, afternoon, evening and night. There are special events and activities for each time. Keep an eye on the time so you don't miss your appointments.{/size}",
    'If you want to accelerate the events, click on the "Skip Time" button, which is available in any location between scenes',
    'Here are the main buttons to find all the useful information and statistics.',
    "This is your phone You can use it to view your friend's photos in the Lustagram app. We may add new features to the smartphone in future releases.",
    "This is your inventory. All useful items obtained in the game end up here. Here you can also find out the amount of money available.",
    "{size=13}This is your notebook - a store of information about everything that can be interesting and useful. The notebook is divided into several sections: a description of the characters and their progress, a menu of shortcuts to available scenes, and the main character's traits.{/size}",
    "Here is the map, which allows you to quickly move between the available game zones.",
    "{size=14}Each game zone is divided into several locations. This panel is responsible for moving quickly between locations within the zone. You can move from room to room in the usual way - through doors or signs.{/size}",
    "The navigation bar can be minimized by pressing this button.",
    "To expand the navigation bar again, use this button.",
    "And here are shortcut buttons to control some of the settings.",
    "This button allows you to go back to the previous frame. It’s only available within scenes.",
    "This is a fast-forward button used within scenes. Works similarly to the Tab button on the keyboard, and is adjustable in Skip Settings on the main menu.",
    "This is a shortcut button for accessing the dialog log. It can be useful if you want to refresh your memory and review previous lines of the characters.",
    "These are the buttons to quickly save and load the game.",
    "Use this button to quickly turn off the sounds in the game and then quickly turn them back on again. The volume of the sounds can be adjusted in the game settings.",
    "This button is only available in open locations and helps to highlight all active and interactive objects.",
    "In order to get a quick access to the settings in the game's main menu, this use this button.",
    "You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!",

    ],


    'CAFE':[
    


    '{size=13}Working in Cafe allows you to earn some money and get points for your school.{/size}\n{size=13}This tutorial will tell you how to do the job right and get more money.{/size}',
    "This is the first out of five possible orders. Remember the sequence of dishes. When you're ready, click Start.",
    'You only have  5 seconds to complete the order.',
    'Right here is a complete list of all the dishes available on the menu. Click on the items you need to add to the order.',
    "If you manage to serve the dishes on time and without mistakes, you'll get an extra $5 tip for each order.",
    "You can complete the minigame at any time by clicking on this button. You'll get a minimum reward of $10 either way, and $5 for each order you manage to complete.",
    "You can get to work now. You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!"
    ],


    'DUELING ARENA':[
    


    "{size=13}Welcome to the arena. {/size}\n{size=13}Here's a quick guide to the mini-game, so you can play without any hassle{/size}",
    "This is your opponent's hitbar. The goal of the game is to bring his stamina level to zero. The first one who manages to do so is declared the winner.",
    "{size=13}Here is your character's hitbar. Watch your stamina level and use elixirs and healing spells on time. If you have them in your arsenal, of course. Here you will also see all the buffs and debuffs on your character.{/size}",
    "All of your character's combat elixirs are shown here. You can use one of the available elixirs before each spell. The turn order is not lost.",
    "{size=13}These are the combat spells available to you. Combat Bolt can be used without restriction, and the others no more often than once every two turns. You can learn the missing spells in Victoria's lessons.{/size}",
    "{size=13}Watch the slider on the magic glyph to stop it at the moment of maximum coloring. The more area of the glyph is painted, the more powerful the spell will be. Castl power is also affected by the level of the spell.{/size}",
    "Now you can try it on your own!. You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!. ",
    ],



    'CALENDAR':[
    "{size=13}In this menu, you can easily find all the {/size}\n{size=13}characters in the game that offer a quest or activity throughout the game day. Here’s {/size}\n{size=13}the best part: you can instantly navigate to them right from the list.{/size}",
    "The characters' avatars are located opposite the time icons. This means that this is the time of day when you can interact with them.",    
    "For example, all the characters whose activities are available in the night are shown here. This principle applies to any time of the day.",
    "Select the avatar of the character you plan to meet and click this button. You will immediately teleport to the location where that character is located.",
    "If you select a character whose interaction is available later in the day, you will be warned that this choice leads to a timeskip. This is done to protect you from accidentally clicking on it.",
    "{size=13}If the time of day is over, the avatars become unavailable until the next morning. It still shows all the characters available at that time, but you can't access them directly from this menu until the new day arrives.{/size}",
    "You can use this button anytime to watch this tutorial again and refresh your memory. Good luck!",
    ],





    }
    tutorial_bb = 0

transform -1 tutorial_alpha_effect:
    on show:
        alpha  .0
        linear 0.2 alpha 1.0
        
   # on hide:
   #     alpha 1.0
   #     linear 0.2 alpha .0
screen tutorial_screen(what_tutor, rtrn = True):
    zorder 1000
    viewport:
        at tutorial_alpha_effect 
        xmaximum 1920
        ymaximum 1080
        image    '#0000'
        $ message  = tutorials[what_tutor][0]
        #text 'TUTORIAL DEBUG' size 40 
        if not tutorial_bb:
            imagebutton:
                idle   '#0000'
                hover  '#0000'
                action NullAction()

            use confirm(
                message, 
                SetVariable('tutorial_bb', 1), SetVariable('tutorial_bb', len(tutorials[what_tutor])-1), yes_text = _("Continue"), no_text = _("Close"))
        if what_tutor == 'CHARACTER INFO':
            if tutorial_bb == 1:
                viewport:
                    xpos 325-25
                    ypos 230-25
                    xmaximum 215+40
                    ymaximum 670+25
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 540
                    ypos 395
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)
            elif tutorial_bb == 2:
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)
                viewport:
                    xpos 860
                    ypos 220
                    xmaximum 670
                    ymaximum 220
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8))
                
                hbox:
                    xpos 860+660
                    ypos 360
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

            elif tutorial_bb == 3:
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)
                viewport:
                    xpos 860
                    ypos 550
                    xmaximum 150
                    ymaximum 70
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png')#, Borders(15, 8, 15, 8))
                
                hbox:
                    xpos 860+150
                    ypos 550
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5


            elif tutorial_bb == 4:
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)
                hbox:
                    xpos 860
                    ypos 650
                    vbox:
                        viewport:
                            xmaximum 722
                            ymaximum 63
                            image '#fff0'
                            image Frame('tutorial/tutorial_max_selection_u_05.png')#, Borders(15, 8, 15, 8))
                        viewport:
                            xmaximum 722
                            ymaximum 63
                            image '#fff0'
                            image Frame('tutorial/tutorial_max_selection_u_05.png') yzoom -1#, Borders(15, 8, 15, 8))
                        
                        #viewport:
                    #    xmaximum 200
                    #    ymaximum 70
                    #    image '#fff0'
                    #    image Frame('tutorial/tutorial_max_selection_r_05.png') xzoom -1#, Borders(15, 8, 15, 8))
                    
                vbox:
                    xpos 860+150
                    ypos 520
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xpos 10 rotate -90  
            elif tutorial_bb == 5:
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action [Hide('tutorial_screen'), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'CHARACTER INFO')]
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 998
                    xpos 1557
                vbox:
                    xpos 1555
                    ypos 880
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xpos 20 rotate -90 ypos -10

        elif what_tutor == 'LUSTOGRAM':
            if tutorial_bb == 1:
                viewport:
                    xpos 400+352
                    ypos 140
                    xmaximum 215+200
                    ymaximum 670+90
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_2.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 650+500
                    ypos 395
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)

            elif tutorial_bb == 2:
                image 'tutorial_elijah' xalign .5 yalign .5
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 133
                    xpos 1070
                hbox:
                    xpos 650+500
                    ypos 395
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)
            elif tutorial_bb == 3:
                image 'tutorial_elijah' xalign .5 yalign .5
                viewport:
                    xmaximum 160
                    ymaximum 150
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection.png', Borders(15, 8, 15, 8)) yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 405
                    xpos 755
                hbox:
                    xpos 650+500
                    ypos 395
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)

            elif tutorial_bb == 4:
                image 'tutorial_elijah_photo'
                hbox:
                    xpos 1100
                    ypos 165
                    viewport:
                        xmaximum 420
                        ymaximum 225
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                
                    viewport:
                        xmaximum 420
                        ymaximum 225
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 650+500
                    ypos 380
                    image 'tutorial_arrow' ypos 10 rotate 90
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)


            elif tutorial_bb == 5:
                image 'tutorial_elijah_photo'
                hbox:
                    xpos 1100
                    ypos 165+200
                    viewport:
                        xmaximum 420
                        ymaximum 180
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                
                    viewport:
                        xmaximum 420
                        ymaximum 180
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 650+500
                    ypos 380+150
                    image 'tutorial_arrow' ypos 10 rotate 90
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 6)

            elif tutorial_bb == 6:
                image 'tutorial_elijah_photo'
                hbox:
                    xpos 1120
                    ypos 970
                    viewport:
                        xmaximum 65
                        ymaximum 80
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                
                    viewport:
                        xmaximum 65
                        ymaximum 80
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 650+500
                    ypos 840
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' ypos -10 xpos 5 rotate -90

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 7)

            elif tutorial_bb == 7:
                image 'tutorial_elijah_photo_comments'
                hbox:
                    xpos 735
                    ypos 160+260
                    viewport:
                        xmaximum 230
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                
                    viewport:
                        xmaximum 230
                        ymaximum 230

                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                

                vbox:
                    xpos 650+400
                    ypos 620
                    image 'tutorial_arrow' ypos 10 rotate 90
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 8)

            elif tutorial_bb == 8:
                image 'tutorial_elijah_photo'
                image 'tutorial_max_selection_3'

                hbox:
                    xpos 665+400
                    ypos 620
                    image 'tutorial_arrow' ypos 10 #rotate 90
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 9)


            elif tutorial_bb == 9:
                image 'tutorial_elijah' xalign .5 yalign .5
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 133
                    xpos 980
                hbox:
                    xpos 650+405
                    ypos 170
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 10)


            elif tutorial_bb == 10:
                image 'tutorial_feed' xalign .5 yalign .5
                viewport:
                    xmaximum 400
                    ymaximum 815
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_3.png') yzoom -1#, Borders(15, 8, 15, 8))
                    xalign .5
                    yalign .5
                hbox:
                    xpos 720+403
                    ypos 180
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 11)

            elif tutorial_bb == 11:
                image 'tutorial_feed' xalign .5 yalign .5
                viewport:
                    xmaximum 130
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    xpos 750
                    ypos 184
                hbox:
                    xpos 650+200
                    ypos 200
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 12)

            elif tutorial_bb == 12:
                image 'tutorial_feed' xalign .5 yalign .5
                viewport:
                    xmaximum 400
                    ymaximum 450
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_3.png') yzoom -1#, Borders(15, 8, 15, 8))
                    xalign .5
                    yalign .4
                hbox:
                    xpos 720+435
                    ypos 250
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 13)
            elif tutorial_bb == 13:
                image 'tutorial_feed' xalign .5 yalign .5
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 133
                    xpos 980+90
                hbox:
                    xpos 650+405+90
                    ypos 170
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 14)

            elif tutorial_bb == 14:
                image 'tutorial_feed' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    
                    action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'LUSTOGRAM'), Hide('tutorial_screen', transition=Dissolve(.5))]
                    
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                    ypos 998
                    xpos 1557
                vbox:
                    xpos 1555
                    ypos 880
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xpos 20 rotate -90 ypos -10

        elif what_tutor == 'HUD INTERFACE':
            if tutorial_bb == 1:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos -15
                    ypos -9
                    xmaximum 340
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 310
                    ypos 10
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 350
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)

            elif tutorial_bb == 2:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos -15
                    ypos -9
                    xmaximum 340
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 220
                    ypos 27
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)



            elif tutorial_bb == 3:
                image 'tutorial_hud_interface_1'
                viewport:
                    xalign 1.0
                    ypos -9
                    xmaximum 360
                    ymaximum 90
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180
                    ypos 27
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 10
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)

            elif tutorial_bb == 4:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1555
                    ypos -27
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180
                    ypos 27
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 10
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)

            elif tutorial_bb == 5:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1640
                    ypos -27
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1260
                    ypos 27
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 10
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 6)


            elif tutorial_bb == 6:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1640+85
                    ypos -27
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1260+85
                    ypos 27
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 10
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 7)
            elif tutorial_bb == 7:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1636+85*2
                    ypos -27
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1260+85*2
                    ypos 27
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 10
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 8)



            elif tutorial_bb == 8:
                image 'tutorial_hud_interface_1'
#tutorial_max_selection_r_05
                viewport:
                    xpos -15
                    ypos 970
                    xmaximum 600
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 580
                    ypos 940
                    image 'tutorial_arrow' ypos 40
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 9)

            elif tutorial_bb == 9:
                image 'tutorial_hud_interface_1'
#tutorial_max_selection_r_05
                viewport:
                    xpos 500
                    ypos 960
                    xmaximum 100
                    ymaximum 150
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection_2.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 580
                    ypos 940
                    image 'tutorial_arrow' ypos 40
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 10)


            elif tutorial_bb == 10:
                image 'tutorial_hud_interface_0'
#tutorial_max_selection_r_05
                viewport:
                    xpos -20
                    ypos 960
                    xmaximum 90
                    ymaximum 150
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection_2.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 100
                    ypos 940
                    image 'tutorial_arrow' ypos 40
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 11)


            elif tutorial_bb == 11:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1470
                    ypos 1000
                    xmaximum 455
                    ymaximum 90
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1100
                    ypos 950
                    viewport:
                        xmaximum 355
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' ypos 60 xzoom -1
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 12)

            elif tutorial_bb == 12:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1547
                    ypos 985
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 13)


            elif tutorial_bb == 13:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1547+45
                    ypos 985
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180+45
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 14)


            elif tutorial_bb == 14:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1549+45*2
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180+50*2
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 15)

            elif tutorial_bb == 15:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1548+45*3
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180+46*3
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 16)

            elif tutorial_bb == 16:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1547+46*5
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1180+50*5
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 17)

            elif tutorial_bb == 17:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1500
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1130
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 18)

            elif tutorial_bb == 18:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1822
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1450
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 50
                imagebutton:
                    idle  '#0000'
                    hover '#0000'

                    action SetVariable('tutorial_bb', 19)

            elif tutorial_bb == 19:
                image 'tutorial_hud_interface_1'
                viewport:
                    xpos 1455
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1080
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 60
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    if rtrn:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'HUD TUTORIAL'), Return()]
                        
                    else:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'HUD TUTORIAL'), SetVariable('hide_interface', False), Hide('tutorial_screen', transition=Dissolve(.5))]
                    
                    #action [Hide('tutorial_screen'), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'LUSTOGRAM')]

        elif what_tutor == 'CAFE':
            if tutorial_bb:
                image 'tutorial_cafe'
            if tutorial_bb == 1:
                image 'tutorial_cafe_selection_0'
                hbox:
                    xpos 1300
                    ypos 360
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)

            if tutorial_bb == 2:
                image 'tutorial_cafe_selection_0'
                hbox:
                    xpos 1300
                    ypos 360
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)

            if tutorial_bb == 3:
                image 'tutorial_cafe_selection_3'
                hbox:
                    xpos 1450
                    ypos 850
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)

            if tutorial_bb == 4:
                image 'tutorial_cafe_selection_0'
                hbox:
                    xpos 1300
                    ypos 360
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)


            if tutorial_bb == 5:
                image 'tutorial_cafe_selection_5'
                hbox:
                    xpos 1470
                    ypos 830
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 6)
            
            if tutorial_bb == 6:
                viewport:
                    xpos 1500
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1125
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 60
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    if rtrn:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'CAFE'), Return()]
                    
                    else:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'CAFE'), SetVariable('hide_interface', False), Hide('tutorial_screen', transition=Dissolve(.5))]
                    
                    #action [Hide('tutorial_screen'), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'LUSTOGRAM')]
        elif what_tutor == 'DUELING ARENA':
            if tutorial_bb == 1:
                image 'tutorial_battle_0'
                viewport:
                    xpos 100
                    ypos 50
                    xmaximum 300
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 380
                    ypos 60
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)

            elif tutorial_bb == 2:
                image 'tutorial_battle_0'
                viewport:
                    xpos 1600-60
                    ypos 50
                    xmaximum 260
                    ymaximum 100
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1220-70
                    ypos 60
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 20
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)


            elif tutorial_bb == 3:
                image 'tutorial_battle_0'
                viewport:
                    xpos 947
                    ypos 915
                    xmaximum 360
                    ymaximum 120
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 570
                    ypos 930
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 30
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)



            elif tutorial_bb == 4:
                image 'tutorial_battle_0'
                viewport:
                    xpos 950-380
                    ypos 920-8
                    xmaximum 400
                    ymaximum 120
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_r.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 570-380
                    ypos 930-10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 30
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)


            elif tutorial_bb == 5:
                image 'tutorial_battle_5'
                hbox:
                    xpos 1480
                    ypos 750
                    image 'tutorial_arrow' ypos 30
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 6)

            elif tutorial_bb == 6:
                image 'tutorial_battle_0'
                viewport:
                    xpos 1500
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1125
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 60
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    if rtrn:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'DUELING ARENA'), Return()]

                    else:
                        action [SetVariable('tutorial_bb', 0), Function(set_tutorial, 'DUELING ARENA'), Hide('tutorial_screen', transition=Dissolve(.5))]
                    
                    #action [Hide('tutorial_screen'), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'LUSTOGRAM')]

        elif what_tutor == 'CALENDAR':
            if tutorial_bb == 1:
                #image 'tutorial_battle_0'
                viewport:
                    xpos 290
                    ypos 255
                    xmaximum 210
                    ymaximum 660
                    image '#fff0'
                    image Frame('tutorial/tutorial_max_selection_2.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                
                hbox:
                    xpos 500
                    ypos 270
                    image 'tutorial_arrow' ypos 10
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 2)


            elif tutorial_bb == 2:
                hbox:
                    xpos 420
                    ypos 690
                    viewport:
                        xmaximum 320
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                    viewport:
                        xmaximum 400
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                        
                    viewport:
                        xmaximum 320
                        ymaximum 230

                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 860+150
                    ypos 550
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xpos 10 rotate -90 ypos -10 

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)

            elif tutorial_bb == 3:

                hbox:
                    xpos 420
                    ypos 690
                    viewport:
                        xmaximum 320
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                    viewport:
                        xmaximum 400
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                        
                    viewport:
                        xmaximum 320
                        ymaximum 230

                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 550
                    ypos 670
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xpos 10 rotate -90 ypos -10 

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 3)


                # viewport:
                #     xmaximum 100
                #     ymaximum 100
                #     image '#fff0'
                #     image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                #     ypos 998
                #     xpos 1557


                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 4)

            elif tutorial_bb == 4:
                $ yes_action = [

                    NullAction()
                    ]
                $ message = _('{size=20}This route is not available at this time of the day.{/size}\n{size=20}Chosing this option will lead to a time skip.{/size}\n{size=20}Continue?{/size}')
                $ dont_ask_again = [
                SetField(persistent, 'quest_log_screen_warning', True),
                SetField(persistent, 'quest_log_screen_warning', None),
                persistent.quest_log_screen_warning
                ]
                use confirm(message, yes_action, Hide('quest_log_screen_warning', transition = Dissolve(.5)), yes_text = _("Accept"), no_text = _("Decline"), dont_ask_again = dont_ask_again)


                image 'tutorial_calendar_4'
                vbox:
                    xpos 700
                    ypos 680
                    image 'tutorial_arrow' rotate 90 xpos 50 ypos 10 
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5



                # viewport:
                #     xmaximum 100
                #     ymaximum 100
                #     image '#fff0'
                #     image Frame('tutorial/tutorial_mini_selection.png') yzoom -1#, Borders(15, 8, 15, 8))
                #     ypos 998
                #     xpos 1557


                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 5)

            elif tutorial_bb == 5:

                hbox:
                    xpos 420
                    ypos 200+40
                    viewport:
                        xmaximum 320
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                    viewport:
                        xmaximum 400
                        ymaximum 230
                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05_05.png', Borders(15, 8, 15, 8))#, Borders(15, 8, 15, 8))
                        
                    viewport:
                        xmaximum 320
                        ymaximum 230

                        image '#fff0'
                        image Frame('tutorial/tutorial_max_selection_r_05.png', Borders(15, 8, 15, 8)) xzoom -1#, Borders(15, 8, 15, 8))
                
                vbox:
                    xpos 860+150
                    ypos 400+40
                    image 'tutorial_arrow' rotate 90 xpos 50 ypos 10 
                    
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    

                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    action SetVariable('tutorial_bb', 6)

            if tutorial_bb == 6:
                #$ tmp_time_now = copy.copy(time_now)
                #$ time_now     = 2
                viewport:
                    xpos 1500+46
                    ypos 983
                    xmaximum 120
                    ymaximum 130
                    image '#fff0'
                    image Frame('tutorial/tutorial_mini_selection.png', Borders(15, 8, 15, 8), tile=gui.frame_tile)
                hbox:
                    xpos 1125+46
                    yalign 1.0
                    viewport:
                        xmaximum 366
                        ymaximum 114
                        image 'tutorial_message'
                        text tutorials[what_tutor][tutorial_bb] color '#305B2F' size 16 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    image 'tutorial_arrow' xzoom -1 ypos 60
                imagebutton:
                    idle  '#0000'
                    hover '#0000'
                    
                    action [SetVariable('time_now', copy.copy(tmp_time_now)), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'CALENDAR'),  Hide('tutorial_screen', transition=Dissolve(.5))]
                    
                    #action [Hide('tutorial_screen'), SetVariable('tutorial_bb', 0), Function(set_tutorial, 'LUSTOGRAM')]
