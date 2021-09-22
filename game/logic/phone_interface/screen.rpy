image phone_button:

    on idle:
        "images/main_interface/phone_button_circle.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/phone_button_circle.png", im.matrix.brightness(.3)) with Dissolve(.2)


image lustagram_button:

    on idle:
        "images/phone_interface/lustagram_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/lustagram_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)

image none_button:

    on idle:
        "images/phone_interface/none_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/none_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)



image notes_button:

    on idle:
        "images/phone_interface/notes_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/notes_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)

image settings_button:
    on idle:
        "images/phone_interface/settings_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/settings_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)


image homes_button:
    on idle:
        "images/phone_interface/homes_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/homes_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)


image patreon_button:
    on idle:
        "images/phone_interface/patreon_icon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/patreon_icon.png", im.matrix.brightness(.3)) with Dissolve(.2)



image phone_lustagram_polygon_button:

    on idle:
        "images/phone_interface/phone_lustagram_polygon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/phone_interface/phone_lustagram_polygon.png", im.matrix.brightness(.7)) with Dissolve(.2)


init -100 python:
    import copy
image phone_lustagram_unlike_button:

    on idle:
        "images/phone_interface/like.png" with Dissolve(.2)
    on hover:
        "images/phone_interface/unlike.png" with Dissolve(.2)

image phone_lustagram_like_button:

    on idle:
        "images/phone_interface/unlike.png" with Dissolve(.2)
    on hover:
        "images/phone_interface/like.png" with Dissolve(.2)

transform tutor_phone_transform:
    linear .5 alpha 0

    pause .5

    linear .5 alpha 1.0

    pause .5

    linear .5 alpha 0

    pause .5

    linear .5 alpha 1.0

    pause .5

    linear .5 alpha 0.0

    pause .5

    linear .5 alpha 1.0


    pause 5

    repeat



transform tutor_phone_transform_2:

    linear .5 alpha 0

    pause .5

    linear .5 alpha 1.0

    pause .5

    linear .5 alpha 0

    pause .5

    linear .5 alpha 1.0

    pause .5

    linear .5 alpha 0.0

    pause .5

    linear .5 alpha 1.0

    repeat



screen phone_interface_screen(Func=[Function(renpy.play,channel = 'sound', filename = 'audio/Iphone.mp3'), Hide('phone_interface_screen', transition = Dissolve(.3))], time='EVENING'):
    zorder 215
    $ time_now_texts = {
    1:'MORNING',
    2:'DAY',
    3:'EVENING',
    4:'NIGHT',
    }

























    if renpy.get_screen('main_interface'):
        imagebutton:
            idle '#000a'
            hover '#000a'
            action Func
    else:
        imagebutton:
            idle '#000a'
            hover '#000a'
            action Return()

    add 'phone_interface_main_bg' xalign .5 yalign .5
    add 'phone_interface_frame' xalign .482 yalign .42
    viewport xalign .5 yalign .5:
        xmaximum 375
        ymaximum 812
        add '#0000'
        imagebutton:
            idle '#0000'
            hover '#0000'
            action NullAction()
        button xpos 15 ypos 718:
            add 'lustagram_button'
            action Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), Show('lustagram_screen', transition = Dissolve(.3))
        if tutor:

            add 'new_quest_icon_2' xpos 15 ypos 718 zoom .6 at tutor_phone_transform
            add 'phone_interface_arrow' xpos 33 ypos 540 yzoom -1
        else:
            button xpos 105 ypos 718:
                add 'notes_button'


                action NullAction() #Show('notes_screen', transition = Dissolve(.5)), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')

            if hasattr(store, 'new_cnq_2') and new_cnq_2:
                add 'new_quest_icon_2' xpos 100 ypos 710 zoom .6

            button xpos 195 ypos 718:
                add 'homes_button'
                action Show('houses_screen', transition = Dissolve(.5)), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')


            button xpos 284 ypos 718:
                add 'patreon_button' xzoom 1.02
                action OpenURL('https://www.patreon.com/bearinthenight')















        add 'main_interface/old_day_panel.png' xpos 25+35 ypos 20+130

        viewport xpos 125+35 ypos 25+130:
            add '#fff0'
            xmaximum 125
            ymaximum 70

            text _(time_now_texts[time_now].title()) bold True xpos 15 ypos 10 size 19
            text _(str(dow).title()) bold True xpos 15 ypos 35 size 19
    key "rollback" action NullAction()



init python:
    log_message_text = { 
    'QLOG_Victoria':
{   
    1:  "Victoria won't let me into her lectures until I get my books to Library.",
    2:  'I can try to get Victoria to like me by showing interest in her lectures.',
    3:  'Victoria suggested that I find my own source of power. I wish I knew where to look...',
    4:  "Victoria's story for this version has come to an end, but you can still visit practice lessons.",

},
    'QLOG_Sabrina': 
{
    1:  'Sabrina would be happy to see me in her classes after the first lesson with Victoria.',
    2:  'I can try to get Sabrina to like me by showing interest in her classes.',
    3:  "Sabrina's story for this version has come to an end. ",
        },



'QLOG_Haley':
{   
    1:  "Haley promised that she would be happy to chat in the morning before Victoria's class.",
    2:  "Haley will be waiting for me in her room tonight. I hope it's a date!",
    3:  "Haley is getting ready for Victoria's private classes, I gotta find out what progress she's made.",
    4:  "Haley is always very busy. I'll try to talk to her in the morning before the lecture.",
    5:  "Haley's too wrapped up in her studies. I don't want to intrude. I'll let her make a move on her own.",
    6:  "Haley's story for this version has come to an end. ",
    7:  "Haley's story for this version has come to an end. ",
},


    
'QLOG_Samantha':    
{
    1:  "Samantha suggested we meet in the living room in the morning.",
    2:  "Samantha expects me to talk to Jacob about her problem.",
    3:  "Samantha needs a compress, which I have to get from Victoria.",
    4:  "Samantha is waiting for my help, I have to give her the compress in the morning.",
    5:  "Samantha's story for this version has come to an end. ",
},
        
'QLOG_Audrey':  
{
    1:  "Audrey only talks to men who can take her to a restaurant.",
    2:  "Audrey is reserved in the evening. I'll see if I can pick her up in the living room in the morning.",
    3:  "Audrey has already shared a smile with me. I shouldn't put off the next step for long.",
    4:  "Audrey will be waiting for me in the living room tonight. I wonder if that's a hint.",
    5:  "Audrey's story for this version has come to an end. ",
    6:  "Audrey and Sam are hiding something. I wish I could discreetly eavesdrop on their conversation.",
},


'QLOG_Lily':{
    1:  "Lily promised she'd be ready to chat with me in the morning before Victoria's class.",
    2:  "I can try to get Lily to like me by attending class and earning points for Leonhart.",
    3:  "Lily expects me to find at least three lost books and turn them in to the library.",
    4:  "Lily doesn't believe that I will be able to defeat my opponent from Adderin in a duel.",
    5:  "Lily will be waiting for me tonight at the fountain. I hope it will be worth it.",
    6:  "Lily will visit my room herself tonight. I'd better get dressed and ready.",
    7:  "Lily's story for this version has come to an end. ",
    },


    
'QLOG_Naomi':   
    {
    1:  "Naomi hinted that she'd be ready to chat with me in the morning before Victoria's class.",
    2:  "Naomi can be found by the fountain tonight.",
    3:  "Naomi's a tricky one. I'll see if I can get a hold of her in class this afternoon.",
    4:  "Naomi can only be taken by storm. I'll try before alchemy class.",
    5:  "Naomi will be waiting for me at the fountain tonight.",
    6:  "Naomi is waiting for the pictures, we should meet in the morning before class.",
    7:  "Naomi's story for this version has come to an end. ",
    },


'QLOG_Amelie':
{   
    1:  "Amelia seems to be interested only in books. So I'll look for books for her and wait for my moment.",
    2:  "Amelia's story for this version has come to an end, but you can still bring her new books.",
    },


    
    
'QLOG_Molly':{  
    1:  "Molly has offered me a job at her cafe during the day and evening.",
    2:  "Molly's story for this version has come to an end, but you can still work in her Cafe.",
    3:  "Molly's story for this version has come to an end.",
        },


'QLOG_Elijah':  
{
    1:  'Elijah should give me a "student card." I can catch him in the living room in the morning.',
    2:  'Elijah gave me a "student card" to get my textbooks from the library.',
    3:  "Elijah recommended that I attend both classes and then find him in the café in the evening.",
    4:  "Elijah's story for this version has come to an end. "
    },


'QLOG_Jacob':   
{
    1:  'Jacob will only admit me to the dueling club when I learn a fighting spell.',
    2:  "Jacob's story for this version has come to an end, but you can still participate in duels.",
    3:  "Jacob's story for this version has come to an end, but you can still participate in duels.",
    4:  "Jacob's story for this version has come to an end, but you can still participate in duels."

    },
}
        
    q_to_p = {
'Victoria': {0:0, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 7, 8: 8, 9: 9, 10: 10}, 
'Sabrina':  {0:0, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, 
'Haley':    {0:0, 2: 1, 1: 2, 3: 3, 6: 4, 7: 5, 10: 6, 11: 7, 12: 8}, 
'Samantha': {0:0, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 6}, 
'Audrey':   {0:0, 1: 1, 3: 2, 4: 3}, 
'Lily':     {0:0, 2: 3, 1: 2, 3: 4, 4: 5, 5: 6, 6: 7}, 
'Naomi':    {0:0, 2: 3, 1: 2, 3: 4, 5: 5, 6: 6, 8: 7}, 
'Amelie':   {0:0, 1: 1, 2: 2}, 
'Molly':    {0:0, 1: 1, 2: 2}, 
'Elijah':   {0:0, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, 
'Jacob':    {0:0, 1: 1, 2: 2}
}

    def p_up(who, what):
        global p_variables        
        if who not in p_variables:
            p_variables.update({who:what})
        if what-1 >= 0:
            p_variables[who] = what-1     
        else:
            p_variables[who] = 0


    log_message_p = {
    'Victoria':[
        "Victoria's waiting for students in her class. It's probably the one where I've passed my exam.",
        "Victoria won't let me into her lectures until I get my books to Library.",
        "I can try to get Victoria to like me by showing interest in her lectures.",
        "Victoria suggested that I find my own source of power. I wish I knew where to look...",
        "Today we talked about different sources of power. I could not tell about Leona, so I had to lie about my source. I need to visit next lessons if I want to learn more.",
        "Victoria told us about creating bolts of magic energy. I think  she'll teach us our first spell soon.", 
        "Victoria showed us how to create a Combat Bolt. Now I can join Duel Club and try in in action. I can also practice Combat Bolt on her lessons to make it stronger.",
        "I've helped Victoria to her books to the library and had an excellent opportunity to check out her divine curves. I think she's starting to like me. Maybe I should visit her lesson more often?",
        "In this lesson, we learned Incendio, and now I can practice it too. On the other hand, there's a lot of new theory to learn as well.",
        "I've now studied Episkey, and it's now available for practical lessons. Or I can go for more theory.",
        "Rictusempra is now available in duels amd practical classes. At this version of Lust Academy there's no more theory or scenes for Victoria.",
],
    
    'Sabrina':[
"Sabrina would be happy to see me in her classes after the first lesson with Victoria.",
"First potions lessons were all about safety. I should visit another one to learn more.",
"This time we've talked about healing potions and why do mages need potions. To learn more, I have to visit more lessons.",
"Sabrina taught us how to prepare a workspace before brewing potions properly. The next lesson should be interesting!",
"At this lesson, students try to brew potions for themselves for the first time. I can visit practice lessons to brew healing potions now.",
"Sabrina's story for this version has come to an end, but you can still visit practice lessons.",
],

    'Haley':[
"I should catch up with Haley. She's probably studying already.",
"Haley promised that she would be happy to chat in the morning before Victoria's class.",
"Haley will be waiting for me in her room in the evening. I hope it's a date!",
"Haley is getting ready for Victoria's private classes, I gotta find out what progress she's made. 'll try to talk to her in the morning before the lecture.",
"Haley's too wrapped up in her studies. I don't want to intrude. I'll let her make a move on her own.",
"Haley found something in her textbook. I'll go to her room after class.",
"Together, Haley and I tried to unwrap the mystery about E.Bloom's notes in her book. Elijah seemed disturbed when we asked him questions. I need to meet Haley before classes to find out what's her plan.",
"We were alone in the courtyard, and Haley showed that she doesn't mind getting closer to me. She also asked me to spy on Amelie until I find a secret room in the library.",
"I saw a strange portal hidden on the second floor or the library. I need to tell Haley about this. Haley's story for this version has come to an end.",

    ],


    'Samantha':[
"",
"Samantha suggested we meet in the living room in the morning.",
"Sam told me that nurse could heal my leg when she gets back from her vacation. She also seemed distressed because new spells were too hard for her. I think I'll know more if we have this kind of morning chit-chat more often.",
"Samantha expects me to talk to Jacob about her problem.",
"I've talked to Jacob.. He told me that Samantha needs a compress, which I have to get from Victoria.",
"Samantha is waiting for my help, I have to give her the compress in the morning.",
"I've solved Samanthas problem for now, but I need to find the source of those wounds before it's too late for her. Samantha's story for this version has come to an end.",
],


    'Audrey':[
"She's in Leonheart too, so I can probably meet her in our campus in the morning.",
"Audrey only talks to men who can take her to a restaurant.",
"I've helped Audrey get milk for her morning coffee, and I hope it'll melt some ice between us. Audrey will be waiting for me in the living room in the evening. I wonder if that's a hint.",
"I've tried to get Sam and Audrey to tell me if they're hiding something, but they told me nothing. Audrey's story for this version has come to an end.",
   ],


   'Lily':[
"Lily promised she'd be ready to chat with me in the morning before Victoria's class.",
"I can try to get Lily to like me by attending class and earning points for Leonhart.",
"Lily expects me to find at least three lost books and turn them in at the library. I wonder if I can just lie about it. How would she know?",
"Lily doesn't believe that I will be able to defeat my opponent from Adderin in a duel. Lily will be waiting for me in the evening at the fountain. I hope it will be worth it.",
"I won at the duel. That means Lily owes me a date. She'll visit my room herself in the evening. I'd better get dressed and ready.",
"We had some fun with Lily and then decided to discuss other house-related plans next time.",
"I've agreed to help Sabrina and Lily to harvest some herbs. Lily and I got lost and had an unbelievable adventure. Lily's story for this version has come to an end.",

   ],


   'Naomi':[
"Naomi hinted that she'd be ready to chat with me in the morning before Victoria's class.",
"Naomi turned out to be arrogant and over-self-confident. I'm sure I can make her more obedient in time. Naomi can be found at the fountain in the evening.",
"I've tried to get her interested in me, but Naomi's a tricky one. I'll see if I can get a hold of her in Potions class this afternoon.",
"Naomi tries to manipulate me into getting test answers for her. Let's see who'll end up outsmarted here. Naomi can be found at the fountain in the evening.",
"Naomi failed to delay Sabrina, and I've got trapped in her class for several hours! I'll tell Naomi how 'fun' that was in the morning! ",
"Naomi fooled with me, and now she needs to earn my forgiveness to get the test results she needs so desperately. I'll meet her in the evening to see what I can get out of this.",
"I took Naomi to the library, and we had some fun time together. I think she finally earned to get those test results... Naomi's story for this version has come to an end. ",


   ],

   'Amelie':

   [
"Amelia only seems to be interested only in books. So I'll look for books for her and wait for my moment.",
"Amelia's story for this version has come to an end, but you can still bring her new books to earn more house-points.",

   ],


   'Molly':[
"Molly has offered me a job at her cafe during the day and evening.",
"Molly's story for this version has come to an end, but you can still work in her Cafe.",
],

    'Elijah':[
'Elijah should give me a "student card." I can catch him in the living room in the morning.',
'Elijah gave me a "student card" to get my textbooks from the library.',
"Elijah recommended that I attend both classes and then find him in the café in the evening.",
"Elijah offered me some sketchy side-job. If I want to find out more I can meet him in the café in the evening.",
"Elijah asked me to get some nectar from Willow in Chompski Shop in Dale. To get to Dale, our house has to win the weekly competition.",
"Willow showed me her magic grove and gave nectar for Elijah. Elijah's story for this version has come to an end.",
],
    'Jacob':[
"Jacob will only admit me to the dueling club when I learn a fighting spell.",
"I was accepted into the dueling club, so I can come to the Academy lobby every night and take part in duels. + Jacob's story for this version has come to an end.",
],
    'Arthur':[
"",
"Arthur told me that if our house wins the weekly competition, I can visit Dale. I wonder what's there?",
"Arthur told us that every week winning house gets to go to Dale. I have to win to check out what opportunities do I have there.",
"When I traveled to Dale, Katrina invaded my mind and tortured me. I don't know how she did it, but I have to find out how to stop it.",
],
    }
screen notes_screen():
    zorder 220
    imagebutton:
        idle '#000a'
        hover '#000a'
        if hasattr(store, 'new_cnq_2') and new_cnq_2:

            action [SetVariable('new_cnq_2', False), Function(renpy.play,channel = 'sound', filename = 'audio/Iphone.mp3'), Hide('notes_screen'), Hide('phone_interface_screen', transition = Dissolve(.3))]


        else:


            action [Function(renpy.play,channel = 'sound', filename = 'audio/Iphone.mp3'), Hide('notes_screen'), Hide('phone_interface_screen', transition = Dissolve(.3))]


    default adden = None
    if not adden:
        add 'notes_bg' xalign .5 yalign .5
    else:
        add 'notes_bg_2' xalign .5 yalign .5
    add 'phone_interface_frame' xalign .482 yalign .42

    viewport:
        xalign .5 ypos 270



        xmaximum 330
        ymaximum 650



        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        has vbox:
            xalign .5
            spacing 15
        if hasattr(store, 'new_cnq') and new_cnq_2:
            viewport:
                add 'notes_bg_button'




                add 'phone_interface/avatars/' + new_cnq_2 + '.png' xpos 15 yalign .5
                if log_message_text.get('QLOG_'+str(new_cnq_2)) and log_message.get('QLOG_'+str(new_cnq_2))  and log_message_text['QLOG_'+str(new_cnq_2)].get(log_message['QLOG_'+str(new_cnq_2)]):
                    viewport:
                        xmaximum 230
                        ymaximum 140
                        xalign 1.0
                        ypos 10
                        add '#0000'
                        text log_message_text['QLOG_'+str(new_cnq_2)][log_message['QLOG_'+str(new_cnq_2)]] color '#000' size 20 yalign .5
                xmaximum 325
                ymaximum 150
        for i in log_message:

            if hasattr(store, 'new_cnq_2') and 'QLOG_'+str(new_cnq_2) != i:
                viewport:
                    add 'notes_bg_button'




                    add 'phone_interface/avatars/' + i[5:] + '.png' xpos 15 yalign .5
                    if log_message_text.get(i) and log_message.get(i) and log_message_text[i].get(log_message[i]):
                        viewport:
                            xmaximum 230
                            ymaximum 140
                            xalign 1.0
                            ypos 10
                            add '#0000'
                            text log_message_text[i][log_message[i]] color '#000' size 20 yalign .5
                    xmaximum 325
                    ymaximum 150
        viewport:
            xmaximum 325
            ymaximum 15
            add '#0000'





































    button ypos 175 xpos 785:


        add 'phone_lustagram_polygon_button'

        if hasattr(store, 'new_cnq') and new_cnq_2:
            action [
            SetVariable('new_cnq_2', False), 
        
        Hide('notes_screen', transition = Dissolve(.3)),
        Function(renpy.play,channel = 'sound', filename = 'audio/Iphone.mp3'),
        
       ]
        else:
            action [
        
        Hide('notes_screen', transition = Dissolve(.3)),
        Function(renpy.play,channel = 'sound', filename = 'audio/Iphone.mp3'),
        
       ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
