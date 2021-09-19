

init python:
    def set_comment_def(post, text, who):
        global comment
        if type(comment) == type(['', '', '']):
            comment = {}
        
        
        if who not in comment:
            comment.update({who:['', '', '']})
        
        comment[who][int(post)-1] = text

    def check_len_comment(who, n_image):
        if type(comment) == type({1:2}) and comment.get(who):
            if comment[who][int(n_image)]:
                return True


    def set_like(li, po, who):
        global like
        if type(like) == type(['', '', '']):
            like = {}
        
        
        if who not in like:
            like.update({who:[False, False, False]})
        
        like[who][int(li)-1] = po

    tutor = False

screen lustagram_screen(pn='list'):
    zorder 220
    if not mp.tutorial['LUSTOGRAM']:
        timer .01 action SetVariable('tutorial_bb', 0), Hide('tutorial_screen'), Show('tutorial_screen', what_tutor = 'LUSTOGRAM')
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('lustagram_screen', transition = Dissolve(.5))
    default page_now = pn
    viewport xalign .5 yalign .5:
        xmaximum 375
        ymaximum 805
        add '#fff'
        imagebutton:
            idle '#0000'
            hover '#0000'
            action NullAction()
        viewport:
            xmaximum 375
            ymaximum 82
            if page_now not in ['list', 'feed']:
                add '#FAFAFA'
            else:
                add '#fff'
            add 'lustogram_up_interface'
            viewport:
                xmaximum 115
                ymaximum 34
                add 'lustogram_buttons_0'
                if not tutor:
                    hbox:
                        imagebutton:
                            if page_now == 'feed':
                                idle Crop((0, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png')

                            else:
                                idle Transform(Crop((0, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png'), alpha = .01)
                            hover Crop((0, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png')
                            action SetScreenVariable('page_now', 'feed')
                        imagebutton:
                            if page_now != 'feed':
                                idle Crop((38, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png')

                            else:
                                idle Transform(Crop((38, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png'), alpha = .01)
                            hover Crop((38, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png')
                            action SetScreenVariable('page_now', 'list')
                        imagebutton:
                            idle Transform(Crop((38*2, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png'), alpha = .01)
                            hover Crop((38*2, 0, 38, 32), 'phone_interface/lustogram_interface/lustogram_buttons_1.png')
                            if page_now in ['list', 'feed']:
                                action Hide('lustagram_screen', transition = Dissolve(.5))
                            else:
                                action SetScreenVariable('page_now', 'list')
                xalign .95 yalign .7






        if page_now == 'list':
            viewport ypos 83:
                ymaximum 812-83

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                has vbox xpos 12
                if tutor:
                    $ i = 'Elijah'


                    viewport:
                        ymaximum 100
                        xmaximum 346
                        imagebutton:
                            idle '#0000'
                            hover 'lustogram_rectangle_button'
                            at AlphaEffect
                            action [
                                Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), 
                                SetScreenVariable('page_now', i)]
                        add 'lustogram_rectangle_button' at tutor_phone_transform_2
                        add 'phone_interface/avatars/' + i + '.png' zoom 1.25 xpos 10 yalign .5
                        add 'new_quest_icon_2' xpos 10 ypos 10 zoom .6 at tutor_phone_transform
                        text str(i) xpos 117 ypos 33 font "fonts/SF_UI_semibold.ttf" size 18 color '#000'


                        text str(lustagrams_posts[i]['description']) xpos 117 ypos 60 font "fonts/SF_UI_regular.ttf" size 13 color '#000'

                else:
                    for i in lustagrams_posts:
                        if (i not in ['Amelie', 'Sabrina', 'Molly'] or getattr(store, 'Q_' + i, 1) > 0 or i == 'Ashley'):


                            viewport:
                                ymaximum 100
                                xmaximum 346
                                imagebutton:
                                    idle '#0000'
                                    hover 'lustogram_rectangle_button'
                                    at AlphaEffect
                                    action [
                                        Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), 
                                        SetScreenVariable('page_now', i)]
                                add 'phone_interface/avatars/' + i + '.png' zoom 1.25 xpos 10 yalign .5
                                text str(i) xpos 117 ypos 33 font "fonts/SF_UI_semibold.ttf" size 18 color '#000'


                                text str(lustagrams_posts[i]['description']) xpos 117 ypos 60 font "fonts/SF_UI_regular.ttf" size 13 color '#000'

        elif page_now == 'feed':
            viewport ypos 83 xpos 14:
                ymaximum 812-83
                xmaximum 375-14


                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                has vbox:
                    spacing 2

                if True:
                    for avatar, img in mp.lustagrams_posts_content_shuffle:
                        if avatar not in ['Amelie', 'Sabrina', 'Molly'] or getattr(store, 'Q_' + avatar, 1) > 0:
                            if lustagrams_posts.get(avatar):
                                viewport:
                                    ymaximum 500
                                    add '#0000'
                                    imagebutton:
                                        idle Transform('phone_interface/avatars/'+avatar+'.png', zoom = .6)
                                        hover Transform(im.MatrixColor('phone_interface/avatars/'+avatar+'.png', im.matrix.brightness(.3)), zoom = .6)
                                        action [
                                            Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), 
                                            SetScreenVariable('page_now', avatar)]

                                        xpos 10 ypos 15
                                    text avatar font "fonts/SF_UI_regular.ttf" size 15 ypos 14 xpos 60 color '#000' bold True
                                    text lustagrams_posts[avatar]['description'] font "fonts/SF_UI_regular.ttf" size 15 ypos 34 xpos 60 color '#000'

                                    imagebutton:
                                        idle Crop((0, 100, 375, 500),'phone_interface/lg_'+str(avatar)+str(img)+'_mini.png')
                                        hover Crop((0, 100, 375, 500),im.MatrixColor('phone_interface/lg_'+str(avatar)+str(img)+'_mini.png', im.matrix.brightness(.3)))

                                        action Show(

        'lustagram_photo_now', photo = str(img), n_comments = lustagrams_posts_content[avatar][img]['n_comments'], 
        date = '27 ', 
        gg_n_comments = lustagrams_posts_content[avatar][img]['gg_n_comments'], 
        n_post = lustagrams_posts_content[avatar][img]['n_post'], who = avatar, transition = Dissolve(.3))
                                        focus_mask True
                                    if type(like) == type({1:1}) and like.get(avatar) and like[avatar][int(img)-1]:
                                        imagebutton:
                                            idle "images/phone_interface/like_field.png"
                                            hover "images/phone_interface/like_field.png"
                                            action Function(set_like, li = img, po = False, who = avatar), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/Like_button.mp3')
                                            ypos 450-5 xpos 10
                                    else:
                                        imagebutton:
                                            idle "images/phone_interface/unlike_field.png"
                                            hover "images/phone_interface/unlike_field.png"
                                            action Function(set_like, li = img, po = True, who = avatar), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/Like_button.mp3')
                                            ypos 450-5 xpos 10

                                    imagebutton:
                                        idle "images/phone_interface/comment_field.png"
                                        hover "images/phone_interface/comment_field.png"
                                        action Show(

        'lustagram_photo_now', photo = str(img), n_comments = lustagrams_posts_content[avatar][img]['n_comments'], 
        date = '27 ', 
        gg_n_comments = lustagrams_posts_content[avatar][img]['gg_n_comments'], 
        n_post = lustagrams_posts_content[avatar][img]['n_post'], who = avatar, transition = Dissolve(.3))





                                        ypos 448-5 xpos 40











        else:
            viewport ypos 83:
                ymaximum 812-83


                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                viewport:
                    ymaximum 100
                    xmaximum 346
                    add '#0000'







                    add 'phone_interface/avatars/' + page_now + '.png' zoom 1.25 xpos 10 yalign .5
                    viewport yalign .5 xpos 120:
                        xmaximum 220
                        ymaximum 45
                        add '#0000'
                        viewport:
                            xmaximum 40
                            ymaximum 23
                            add '#0000'
                            ypos 10
                            text str(lustagrams_posts[page_now]['posts']) size 22 font 'fonts/SF_UI_bold.ttf' color '#000' yalign .0 xalign .5

                        viewport:
                            xmaximum 50
                            ymaximum 23
                            add '#0000'
                            ypos 10
                            xpos 85
                            text str(lustagrams_posts[page_now]['followers']) size 22 font 'fonts/SF_UI_bold.ttf' color '#000' yalign .0 xalign .5
                        viewport:
                            xmaximum 60
                            ymaximum 23
                            add '#0000'
                            ypos 10
                            xpos 160
                            text str(lustagrams_posts[page_now]['following']) size 22 font 'fonts/SF_UI_bold.ttf' color '#000' yalign .0 xalign .5

                        text 'Posts' font "fonts/SF_UI_semibold.ttf" size 13 color '#000' yalign 1.0
                        text 'Followers' xalign .5 font "fonts/SF_UI_semibold.ttf" size 13 color '#000' yalign 1.0
                        text 'Following' xalign 1.0 font "fonts/SF_UI_semibold.ttf" size 13 color '#000' yalign 1.0
                text str(page_now) xpos 18 ypos 105 font "fonts/SF_UI_semibold.ttf" size 18 color '#000'

                if lustagrams_posts.get(page_now):

                    text str(lustagrams_posts[page_now]['description']) xpos 18 ypos 130 font "fonts/SF_UI_regular.ttf" size 13 color '#000'
            if not lustagrams_posts.get(page_now):
                text 'This Account is {b}Private{/b}' ypos 280 xalign .5 color '#000' font 'fonts/lustagram_name.ttf' bold True size 20
            else:
                vpgrid cols 3 rows 4 xpos 3 ypos 215+70:
                    spacing 3
                    for i in range(1, lustagrams_posts[page_now]['posts']+1)[::-1]:

                        viewport:
                            xmaximum 120
                            ymaximum 120
                            if tutor:
                                add Frame('images/phone_interface/lg_'+page_now+str(i)+'.png') at tutor_phone_transform_2

                            else:
                                add Frame('images/phone_interface/lg_'+page_now+str(i)+'.png')
                            imagebutton:
                                idle '#0000'
                                hover '#000a'
                                action Show(

    'lustagram_photo_now', photo = str(i), n_comments = lustagrams_posts_content[page_now][i]['n_comments'], 
    date = '27 ', 
    gg_n_comments = lustagrams_posts_content[page_now][i]['gg_n_comments'], 
    n_post = lustagrams_posts_content[page_now][i]['n_post'], who = page_now, transition = Dissolve(.3))



                    for i in xrange(12):
                        viewport:
                            xmaximum 120
                            ymaximum 120
                            add '#c4c4c4'












    add 'phone_interface_frame' xalign .482 yalign .42

    hbox:
        style_prefix "quick"

        xalign .845
        yalign .99
        spacing 5


        # if renpy.get_screen('main_interface'):
        #     imagebutton:
        #         idle  Transform('main_interface/down_buttons/quest_button_0.png', alpha = .8)
        #         hover 'main_interface/down_buttons/quest_button_0.png'
        #         selected_idle 'main_interface/down_buttons/quest_button_0.png'


        #         action Show('tutorial_screen', 'LUSTOGRAM', False)





























screen lustagram_photo_now(photo=1, date='17', n_comments=[], gg_n_comments=[], n_post, who='Olivia'):
    zorder 220
    if not tutor:
        imagebutton:
            idle '#0000'
            hover '#0000'
            action Hide('lustagram_photo_now', transition = Dissolve(.3))
    add '#fff'
    add 'images/phone_interface/lg_' + who + str(photo) + '.png'










    add 'phone_interface/avatars/' + who + '.png' xpos 1150 ypos 40+30 zoom 1.2

    text who color '#000' font 'fonts/lustagram_name.ttf' bold True xpos 1250 ypos 40+50
    add 'images/phone_interface/tmp/olivia_xxxxx.png' xpos 1250 ypos 55+30 zoom 1.2

    if tutor:
        default trrt = False
    viewport xpos 1150 ypos 200:
        add '#0000'
        xmaximum 740
        vbox:
            for i in n_post:
                text i.replace('/emoji', '/emoji/big/') color '#000' size 25
            text '   '
            for i in n_comments:
                $ i = i.replace('/emoji', '/emoji/big/')
                $ name_go_s = i.find('{/b}')
                $ name_go   = i[3:name_go_s]
                hbox:
                    textbutton str('{b}' + name_go + '{/b}'):

                        text_color '#000' text_size 25 text_hover_color '#000a'
                        if not lustagrams_posts.get(name_go):
                            action NullAction()
                        else:
                            action [
                        Hide('lustagram_photo_now'),
                        Hide('olivia_post'),
                        Show('lustagram_screen', pn = name_go, transition = Dissolve(.3))
                        ]
                    text i[name_go_s+4:] color '#000' size 25 ypos 5 xpos -7

            if type(comment) != type('1'):
                if type(comment) != type(['', '', '']) and comment.get(who) and len(comment[who][int(photo)-1]):











                    vbox:
                        text unicode('{b}[gg]{/b}:') + '  ' + unicode(comment[who][int(photo)-1].replace('/emoji', '/emoji/big/')) color '#000' size 25
                        textbutton ' {color=#0007} (del) {/color}' action Function(set_comment_def, post = photo, text = '', who = who), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')
    if type(like) == type({1:1}) and like.get(who) and like[who][int(photo)-1]:
        imagebutton:

            idle "images/phone_interface/like.png"
            hover "images/phone_interface/like.png"
            action Function(set_like, li = photo, po = False, who = who), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/Like_button.mp3')
            ypos 1000 xpos 1150
    else:


        imagebutton:
            if tutor:
                at tutor_phone_transform_2
            idle "images/phone_interface/unlike.png"
            hover "images/phone_interface/unlike.png"
            action SetScreenVariable('trrt', True), Function(set_like, li = photo, po = True, who = who), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/Like_button.mp3')
            ypos 1000 xpos 1150
    if tutor and trrt:
        add 'phone_interface_arrow' yzoom -1 ypos 800 xpos 1200
    elif tutor:

        add 'phone_interface_arrow' yzoom -1 ypos 800 xpos 1145
    imagebutton:
        if tutor and trrt:
            at tutor_phone_transform_2
        idle "images/phone_interface/comment.png"
        hover "images/phone_interface/comment.png"

        if tutor and trrt:
            if type(comment == type(['', '', ''])) or not check_len_comment(who,int(photo)-1):
                action Show('set_comment_screen', transition = Dissolve(.3), gg_n_comments = gg_n_comments, post = photo, who = who), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')
            else:
                action Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')

        elif tutor and not trrt:

            action NullAction()
        else:
            if type(comment == type(['', '', ''])) or not check_len_comment(who,int(photo)-1):
                action Show('set_comment_screen', transition = Dissolve(.3), gg_n_comments = gg_n_comments, post = photo, who = who), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')
            else:
                action Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')

        ypos 1000 xpos 1200





screen set_comment_screen(gg_n_comments=[], post='1', who='Olivia'):
    zorder 220
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('set_comment_screen', transition = Dissolve(.3))
    vbox yalign .5 xalign .5:
        spacing 10
        for i in gg_n_comments:
            viewport:
                xmaximum 348
                ymaximum 40
                imagebutton:
                    idle Frame(im.Sepia('images/phone_interface/comment_bg.png'))
                    hover Frame('images/phone_interface/comment_bg.png')

                    if tutor:
                        action SetVariable('tutor', False), Hide('lustagram_photo_now'), SetScreenVariable('set_comment', False), Function(set_comment_def, post = post, text = unicode(i[1]), who = who), Hide('set_comment_screen', transition = Dissolve(.3)), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')

                    else:
                        action SetScreenVariable('set_comment', False), Function(set_comment_def, post = post, text = unicode(i[1]), who = who), Hide('set_comment_screen', transition = Dissolve(.3)), Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3')


                viewport:
                    xmaximum 320
                    xalign .5 yalign .5
                    add '#0000'
                    if len(unicode(i[0])) > 24:
                        ymaximum 90
                    else:
                        ymaximum 40
                    text unicode(i[0]):
                        font 'fonts/lustagram.ttf'
                        xalign .5 yalign .5
                        color '#000'
                        if len(unicode(i[0])) > 24:
                            size 18
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
