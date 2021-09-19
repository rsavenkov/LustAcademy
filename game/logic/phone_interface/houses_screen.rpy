init python:
    def get_homes_great():
        
        d = {}
        for i in range(4):
            d.update({homes.items()[i][0]:homes.items()[i][1].items()[2][1]})
        list_d = list(d.items())
        list_d.sort(key=lambda i: i[1])
        d = []
        for i in list_d:
            d.append(i[0])
        return d[::-1]



screen houses_screen:
    default get_homes_great = get_homes_great()
    default get_homes_great_number = {
    1 : 'st',
    2 : 'nd',
    3 : 'rd',
    4 : 'th',


    }

    default ghg_adderin = get_homes_great.index('Adderin')+1
    default ghg_leonheart = get_homes_great.index('Leonheart')+1
    default ghg_martenden = get_homes_great.index('Martenden')+1
    default ghg_crowhive = get_homes_great.index('Crowhive')+1

    zorder 215
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('houses_screen', transition = Dissolve(.5))
    viewport xalign .5 yalign .5:
        xmaximum 375
        ymaximum 812
        add '#0000'
        add 'houses_bg' xalign .5 yalign .5

        viewport:
            xpos 25
            ypos 652
            xmaximum 65
            ymaximum 20
            add '#0000'
            text str(homes['Adderin']['now']) size 16 xalign .5 yalign .5 font 'fonts/h_font.ttf' color '#684B30'

        viewport:
            xmaximum 54
            ymaximum int(int((float(homes['Adderin']['now'])/350.0)*353))
            add '#506817' alpha .8
            xpos 30
            ypos 650
            yalign 1.0
        add 'phone_interface/home_0.png' ypos 580-int(int((float(homes['Adderin']['now'])/350.0)*353)) xpos 40




        viewport:
            xpos 25
            ypos 120
            xmaximum 65
            ymaximum 20
            add '#0000'
            if ghg_adderin == 1:
                add Text(
                    str(ghg_adderin) + get_homes_great_number[ghg_adderin], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 24,
                    color = '#FFC062'
                    ) alpha .8 xalign .5 yalign .5
            else:
                add Text(
                    str(ghg_adderin) + get_homes_great_number[ghg_adderin], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 18,
                    color = '#FFE3BA'
                    ) alpha .4 xalign .5 yalign .5





        viewport:
            xpos 110
            ypos 652
            xmaximum 65
            ymaximum 20
            add '#0000'
            text str(homes['Leonheart']['now']) size 16 xalign .5 yalign .5 font 'fonts/h_font.ttf' color '#684B30'

        viewport:
            xmaximum 54
            ymaximum int(int((float(homes['Leonheart']['now'])/350.0)*353))
            add '#8f2b18' alpha .8
            xpos 115
            ypos 650
            yalign 1.0
        add 'phone_interface/home_1.png' ypos 580-int(int((float(homes['Leonheart']['now'])/350.0)*353)) xpos 125




        viewport:
            xpos 110
            ypos 120
            xmaximum 65
            ymaximum 20
            add '#0000'
            if ghg_leonheart == 1:
                add Text(
                    str(ghg_leonheart) + get_homes_great_number[ghg_leonheart], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 24,
                    color = '#FFC062'
                    ) alpha .8 xalign .5 yalign .5
            else:
                add Text(
                    str(ghg_leonheart) + get_homes_great_number[ghg_leonheart], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 18,
                    color = '#FFE3BA'
                    ) alpha .4 xalign .5 yalign .5




        viewport:
            xpos 193
            ypos 652
            xmaximum 65
            ymaximum 20
            add '#0000'
            text str(homes['Martenden']['now']) size 16 xalign .5 yalign .5 font 'fonts/h_font.ttf' color '#684B30'


        viewport:
            xmaximum 54
            ymaximum int(int((float(homes['Martenden']['now'])/350.0)*353))
            add '#a88b33' alpha .8
            xpos 200
            ypos 651
            yalign 1.0
        add 'phone_interface/home_2.png' ypos 583-int(int((float(homes['Martenden']['now'])/350.0)*353)) xpos 197+13


        viewport:
            xpos 193
            ypos 120
            xmaximum 65
            ymaximum 20
            add '#0000'
            if ghg_martenden == 1:
                add Text(
                    str(ghg_martenden) + get_homes_great_number[ghg_martenden], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 24,
                    color = '#FFC062'
                    ) alpha .8 xalign .5 yalign .5
            else:
                add Text(
                    str(ghg_martenden) + get_homes_great_number[ghg_martenden], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 18,
                    color = '#FFE3BA'
                    ) alpha .4 xalign .5 yalign .5



        viewport:
            xpos 280
            ypos 652
            xmaximum 65
            ymaximum 20
            add '#0000'
            text str(homes['Crowhive']['now']) size 16 xalign .5 yalign .5 font 'fonts/h_font.ttf' color '#684B30'







        viewport:
            xmaximum 54
            ymaximum int(int((float(homes['Crowhive']['now'])/350.0)*353))
            add '#173a70' alpha .8
            xpos 285
            ypos 650
            yalign 1.0
        add 'phone_interface/home_3.png' ypos 583-int(int((float(homes['Crowhive']['now'])/350.0)*353)) xpos 275+10+10

        viewport:
            xpos 280
            ypos 120
            xmaximum 65
            ymaximum 20
            add '#0000'
            if ghg_crowhive == 1:
                add Text(
                    str(ghg_crowhive) + get_homes_great_number[ghg_crowhive], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 24,
                    color = '#FFC062'
                    ) alpha .8 xalign .5 yalign .5
            else:
                add Text(
                    str(ghg_crowhive) + get_homes_great_number[ghg_crowhive], 
                    font  = 'fonts/h_font.ttf', 
                    size  = 18,
                    color = '#FFE3BA'
                    ) alpha .4 xalign .5 yalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
