init python:
    for fn in renpy.list_files():
        if fn.startswith("images/prologue/") and (fn.endswith((".webp")) or fn.endswith((".png")) or fn.endswith((".jpg"))):
            
            name = fn[::-1]
            b = name.find('.')
            c = name[b+1:].find('/')
            name = name[b+1:][:c][::-1]
            
            renpy.image('sc i_' + name, fn)
    def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=None, start=1, ext='png', **properties):
        args = []
        
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = renpy.easy.displayable(img_name + str(i))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                
                args.append(effect)
        if reverse: 
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = renpy.easy.displayable(img_name + str(i))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)



image mm_bg:
    'prologue/1_069.webp' with Dissolve(1.5)
    5
    'prologue/1_002.webp' with Dissolve(1.5)
    5
    'prologue/1_026_4.webp' with Dissolve(1.5)
    5
    'prologue/1_047.webp' with Dissolve(1.5)
    5
    'prologue/1_065_2.webp' with Dissolve(1.5)
    5
    'prologue/1_084.webp' with Dissolve(1.5)
    5
    'prologue/1_072_8.webp' with Dissolve(1.5)
    5
    repeat





image sc i_dueling_1_3 = Movie(play='images/video/dueling_1_3.webm')

image sc i_dueling_1_10 = Movie(play='images/video/dueling_1_10.webm')

image sc i_dueling_1_10R = Movie(play='images/video/dueling_1_10R.webm')

image sc i_dueling_1_11 = Movie(play='images/video/dueling_1_11.webm')

image sc i_dueling_1_12 = Movie(play='images/video/dueling_1_12.webm')





image sc i_Naomi_3_anim_1 = Movie(play='images/video/Naomi_3_anim_1.webm')

image sc i_Naomi_3_anim_2 = Movie(play='images/video/Naomi_3_anim_2.webm')


image sc i_Amelie_1_anim_1a = Movie(play='images/video/Amelie_1_anim_1.webm', loop = False)


image sc i_Amelie_1_anim_1:
    'sc i_Amelie_1_anim_1a'
    pause 9.96
    'images/video/Amelie_1_anim_1_z.webp'





image sc i_Victoria_1_anim_1 = Movie(play='images/video/i_Victoria_1_anim_1.webm')

image sc i_Victoria_4_anim_1 = Movie(play='images/video/i_Victoria_1_anim_1.webm')



image sc i_dueling_anim_1a = Movie(play='images/video/dueling_anim_1.webm')

image sc i_dueling_anim_1:
    'sc i_dueling_anim_1a'
    pause 3
    'images/video/dueling_anim_1_z.webp'


image sc i_Molly_1_anim_1a = Movie(play='images/video/Molly_1_anim_1.webm')


image sc i_Molly_1_anim_1:
    'sc i_Molly_1_anim_1a'
    pause 8.96
    'images/video/Molly_1_anim_1_z.webp'


image sc i_Sabrina_1_anim_1a = Movie(play='images/video/Sabrina_1_anim_1.webm')



image sc i_Sabrina_1_anim_1:
    'sc i_Sabrina_1_anim_1a'
    pause 9.83
    'images/video/Sabrina_1_anim_1_z.webp'






image sc i_Leona_1_anim_1 = Movie(play='images/video/Leona_1_anim_1.webm')

image sc i_Leona_1_anim_2 = Movie(play='images/video/Leona_1_anim_2.webm')
image sc i_Leona_1_anim_3 = Movie(play='images/video/Leona_1_anim_3.webm')
image sc i_Leona_1_anim_4 = Movie(play='images/video/Leona_1_anim_4.webm')
image sc i_Leona_1_anim_5 = Movie(play='images/video/Leona_1_anim_5.webm')
image sc i_Leona_1_anim_6 = Movie(play='images/video/Leona_1_anim_6.webm')
image sc i_Leona_1_anim_7 = Movie(play='images/video/Leona_1_anim_7.webm')
image sc i_Leona_1_anim_8 = Movie(play='images/video/Leona_1_anim_8.webm')
image sc i_Leona_1_anim_8_a = 'images/video/Leona_1_anim_8_a.webp'
image sc i_Leona_1_anim_9 = Movie(play='images/video/Leona_1_anim_9.webm')
image sc i_Leona_1_anim_10 = Movie(play='images/video/Leona_1_anim_10.webm')



image sc i_Lily_5_anim_1 = Movie(play='images/video/Lily_5_anim_1.webm')



image sc i_Lily_5_anim_10 = Movie(play='images/video/Lily_5_anim_10.webm')
image sc i_Lily_5_anim_11 = Movie(play='images/video/Lily_5_anim_11.webm')
image sc i_Lily_5_anim_12 = Movie(play='images/video/Lily_5_anim_12.webm')


image sc i_Lily_NV_anim_1 = Movie(play='images/video/Lily_NV_anim_1.webm')
image sc i_Lily_NV_anim_2 = Movie(play='images/video/Lily_NV_anim_2.webm')


image sc i_Audrey_NV_anim_1 = Movie(play='images/video/Audrey_NV_anim_1.webm')
image sc i_Audrey_NV_anim_2 = Movie(play='images/video/Audrey_NV_anim_2.webm')



image sc i_Lily_5_anim_2 = Movie(play='images/video/Lily_5_anim_2.webm')
image sc i_Lily_5_anim_3 = Movie(play='images/video/Lily_5_anim_3.webm')
image sc i_Lily_5_anim_4 = Movie(play='images/video/Lily_5_anim_4.webm')
image sc i_Lily_5_anim_5 = Movie(play='images/video/Lily_5_anim_5.webm')
image sc i_Lily_5_anim_6 = Movie(play='images/video/Lily_5_anim_6.webm')
image sc i_Lily_5_anim_7 = Movie(play='images/video/Lily_5_anim_7.webm')
image sc i_Lily_5_anim_8 = Movie(play='images/video/Lily_5_anim_8.webm')
image sc i_Lily_5_anim_9 = Movie(play='images/video/Lily_5_anim_9.webm')


image sc i_Samantha_NV_anim_1 = Movie(play='images/video/Samantha_NV_anim_1.webm')

image sc i_Samantha_NV_anim_2 = Movie(play='images/video/Samantha_NV_anim_2.webm')

image sc i_Haley_NV_anim_1 = Movie(play='images/video/Haley_NV_anim_1.webm')


image sc i_Haley_NV_anim_2 = Movie(play='images/video/Haley_NV_anim_2.webm')



image sc i_Sabrina_1_anim_1 = Movie(play='images/video/Sabrina_1_anim_1.webm')

image sc i_dueling_anim_1as = Movie(play='images/video/dueling_anim_1.webm', loop = False)


image sc i_dueling_anim_1:
    'sc i_dueling_anim_1as'
    pause 3
    'video/dueling_anim_1_z.webp'


image sc i_dueling_anim_2as = Movie(play='images/video/dueling_anim_2.webm', loop = False)


image sc i_dueling_anim_2:
    'sc i_dueling_anim_2as'
    pause 5.96
    'video/dueling_anim_2_z.webp'


image sc i_1_008a = Movie(play='images/video/1_008.webm', loop = False)

image sc i_1_008:
    'sc i_1_008a'
    pause 9
    'video/1_008_z.webp'



image sc i_1_014a = Movie(play='images/video/1_014.webm', loop = False)
image sc i_1_014:
    'sc i_1_014a'
    pause 5.16
    'images/video/1_014_z.webp'


image sc i_1_023a = Movie(play='images/video/1_023.webm', loop = False)


image sc i_1_023:
    'sc i_1_023a'
    pause 11.96
    'video/1_023_z.webp'


image sc i_1_043_1 = Movie(play='images/video/1_043_1.webm', loop = True)

image sc i_1_043_2 = Movie(play='images/video/1_043_2.webm', loop = True)

image sc i_1_043_3 = Movie(play='images/video/1_043_3.webm', loop = True)


image sc i_1_051a = Movie(play='images/video/1_051.webm', loop = True)
image sc i_1_051:
    'sc i_1_051a'
    pause 10.66
    'video/1_051_z.webp'


image sc i_1_061_a1 = Movie(play='images/video/1_061_a1.webm', loop = True)

image sc i_1_061_a2 = Movie(play='images/video/1_061_a2.webm', loop = True)

image sc i_1_061_a3 = Movie(play='images/video/1_061_a3.webm', loop = True)

image sc i_1_061_a4 = Movie(play='images/video/1_061_a4.webm', loop = True)

image sc i_1_061_a5 = Movie(play='images/video/1_061_a5.webm', loop = True)

image sc i_1_061_a6 = Movie(play='images/video/1_061_a6.webm', loop = True)


image sc i_1_072_5a = Movie(play='images/video/1_072_5.webm')

image sc i_1_072_5:
    'sc i_1_072_5a'
    pause 10.13
    'video/1_072_5_z.webp'

image sc i_1_082a = Movie(play='images/video/1_082.webm')

image sc i_1_082:
    'sc i_1_082a'
    pause 9.83
    'video/1_082_z.webp'

image sc i_1_138_0 = Movie(play='images/video/ep2/2.webm')

image sc i_1_138_2 = Movie(play='images/video/ep2/2.webm')

image 1_130_a = Movie(play='images/video/ep2/1_130.webm')


image 1_130_victoria:
    '1_130_a'
    pause 6.0
    'video/1_130_0.webp'



image i_1_256_1 = Movie(play='images/video/ep2/sheet_28/1_256_1.webm')
image sc i_1_256_2 = Movie(play='images/video/ep2/sheet_28/1_256_2.webm')
image sc i_1_259_3 = Movie(play='images/video/ep2/sheet_28/1_259_3.webm')
image sc i_1_259_4 = Movie(play='images/video/ep2/sheet_28/1_259_4.webm')
image sc i_1_261_1 = Movie(play='images/video/ep2/sheet_28/1_261_1.webm')
image sc i_1_261_2 = Movie(play='images/video/ep2/sheet_28/1_261_2.webm')
image sc i_1_261_3 = Movie(play='images/video/ep2/sheet_28/1_261_3.webm')
image sc i_1_263_11_1 = Movie(play='images/video/ep2/sheet_28/1_263_11_1.webm')
image sc i_1_263_11_2 = Movie(play='images/video/ep2/sheet_28/1_263_11_2.webm')
image sc i_1_263_11_3 = Movie(play='images/video/ep2/sheet_28/1_263_11_3.webm')
image sc i_1_263_11_4 = Movie(play='images/video/ep2/sheet_28/1_263_11_4.webm')
image sc i_1_264_5 = Movie(play='images/video/ep2/sheet_28/1_264_5.webm')
image sc i_1_264_6 = Movie(play='images/video/ep2/sheet_28/1_264_6.webm')
image sc i_1_264_7 = Movie(play='images/video/ep2/sheet_28/1_264_7.webm')


image sc i_1_172_2_video = Movie(play = 'images/video/ep2/sheet_27/1_172_2.webm')

image i_1_172_2_tmp = Movie(play = 'images/video/ep2/sheet_27/1_172_2.webm')


image sc i_1_172_2_video:
    'i_1_172_2_tmp'
    8.99
    'images/video/1_172_3.webp'
image sc i_1_222_x = Movie(play='images/video/ep2/sheet_27/1_222_X.webm')
image sc i_1_222_xx = Movie(play='images/video/ep2/sheet_27/1_222_XX.webm')

image sc i_1_225_x = Movie(play='images/video/ep2/sheet_27/1_225_X.webm')
image sc i_1_225_xx = Movie(play='images/video/ep2/sheet_27/1_225_XX.webm')


image 1_219_XX = Movie(play='images/video/ep2/sheet_27/1_219_XX.webm')
image 1_228_X = Movie(play='images/video/ep2/sheet_27/1_228_X.webm')
image 1_228_XX = Movie(play='images/video/ep2/sheet_27/1_228_XX.webm')
image 1_228_XXX_a = Movie(play='images/video/ep2/sheet_27/1_228_XXX.webm', loop = False)


image sc i_Leona_1_anim_11tmp = Movie(play='images/video/Leona_1_anim_11.webm', loop = False)


image sc i_Leona_1_anim_11:
    'sc i_Leona_1_anim_11tmp'
    pause 8.1
    'images/video/Leona_1_anim_11_z.webp'



image end_video = Movie(play='images/video/end_video.webm')


image 1_228_XXX:
    '1_228_XXX_a'
    pause 4
    'prologue/19-32/1_229.webp'


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

image sc i_Arthur_3_20_1= Movie(play="images/video/ep3/Arthur_3_20_1.webm", loop = True)

image sc i_Lily_6_anim_1_tmp= Movie(play="images/video/ep3/Lily_6_anim_1.webm")

image sc i_Lily_6_anim_1:
    'sc i_Lily_6_anim_1_tmp'
    pause 1.5
    'images/video/ep3/Lily_6_anim_1_z.png'


image sc i_Lily_6_anim_7_tmp= Movie(play="images/video/ep3/Lily_6_anim_7.webm")


image sc i_Lily_6_anim_7:
    'sc i_Lily_6_anim_7_tmp'
    pause 2
    'images/video/ep3/Lily_6_anim_7_z.png'



image sc i_Lily_6_anim_10= Movie(play="images/video/ep3/Lily_6_anim_10.webm", loop = True)
image sc i_Lily_6_anim_11= Movie(play="images/video/ep3/Lily_6_anim_11.webm", loop = True)
image sc i_Lily_6_anim_12= Movie(play="images/video/ep3/Lily_6_anim_12.webm", loop = True)
image sc i_Lily_6_anim_13= Movie(play="images/video/ep3/Lily_6_anim_13.webm", loop = True)
image sc i_Lily_6_anim_14= Movie(play="images/video/ep3/Lily_6_anim_14.webm", loop = True)
image sc i_Lily_6_anim_15= Movie(play="images/video/ep3/Lily_6_anim_15.webm", loop = True)
image sc i_Lily_6_anim_16= Movie(play="images/video/ep3/Lily_6_anim_16.webm", loop = True)
image sc i_Lily_6_anim_17= Movie(play="images/video/ep3/Lily_6_anim_17.webm", loop = True)
image sc i_Lily_6_anim_18= Movie(play="images/video/ep3/Lily_6_anim_18.webm", loop = True)
image sc i_Lily_6_anim_19= Movie(play="images/video/ep3/Lily_6_anim_19.webm", loop = True)
image sc i_Lily_6_anim_2= Movie(play="images/video/ep3/Lily_6_anim_2.webm", loop = True)
image sc i_Lily_6_anim_3= Movie(play="images/video/ep3/Lily_6_anim_3.webm", loop = True)
image sc i_Lily_6_anim_4= Movie(play="images/video/ep3/Lily_6_anim_4.webm", loop = True)
image sc i_Lily_6_anim_5= Movie(play="images/video/ep3/Lily_6_anim_5.webm", loop = True)
image sc i_Lily_6_anim_6= Movie(play="images/video/ep3/Lily_6_anim_6.webm", loop = True)
image sc i_Lily_6_anim_8= Movie(play="images/video/ep3/Lily_6_anim_8.webm", loop = True)
image sc i_Lily_6_anim_9= Movie(play="images/video/ep3/Lily_6_anim_9.webm", loop = True)
image sc i_Naomi_8_anim_1= Movie(play="images/video/ep3/Naomi_8_anim_1.webm", loop = True)
image sc i_Naomi_8_anim_2= Movie(play="images/video/ep3/Naomi_8_anim_2.webm", loop = True)
image sc i_Naomi_8_anim_3= Movie(play="images/video/ep3/Naomi_8_anim_3.webm", loop = True)
image sc i_Naomi_8_anim_4= Movie(play="images/video/ep3/Naomi_8_anim_4.webm", loop = True)
image sc i_Naomi_8_anim_5= Movie(play="images/video/ep3/Naomi_8_anim_5.webm", loop = True)
image sc i_Naomi_8_anim_6= Movie(play="images/video/ep3/Naomi_8_anim_6.webm", loop = True)
image sc i_Victoria_8_7= Movie(play="images/video/ep3/Victoria_8_7.webm", loop = True)


image sc i_Chompski_1_anim_1_tmp= Movie(play="images/video/ep3/Chompski_1_anim_1.webm")
image sc i_Chompski_1_anim_1:
    'sc i_Chompski_1_anim_1_tmp'
    pause 1.5
    'images/video/ep3/Chompski_1_anim_1_z.webp'

image sc i_Chompski_1_anim_2_tmp= Movie(play="images/video/ep3/Chompski_1_anim_2.webm")

image sc i_Chompski_1_anim_2:
    'sc i_Chompski_1_anim_2_tmp'
    pause 6
    'images/video/ep3/Chompski_1_anim_2_z.webp'

image sc i_Naomi_8_anim_7= Movie(play="images/video/ep3/Naomi_8_anim_7.webm", loop = True)
image sc i_Naomi_8_anim_8= Movie(play="images/video/ep3/Naomi_8_anim_8.webm", loop = True)
image sc i_Naomi_8_anim_9= Movie(play="images/video/ep3/Naomi_8_anim_9.webm", loop = True)
image sc i_VIP_Lucy_1_anim_1= Movie(play="images/video/ep3/VIP_Lucy_1_anim_1.webm", loop = True)
image sc i_VIP_Lucy_1_anim_2= Movie(play="images/video/ep3/VIP_Lucy_1_anim_2.webm", loop = True)
image sc i_VIP_Lucy_1_anim_3= Movie(play="images/video/ep3/VIP_Lucy_1_anim_3.webm", loop = True)
image sc i_VIP_Lucy_1_anim_4= Movie(play="images/video/ep3/VIP_Lucy_1_anim_4.webm", loop = True)
image sc i_VIP_Lucy_1_anim_5= Movie(play="images/video/ep3/VIP_Lucy_1_anim_5.webm", loop = True)
image sc i_VIP_Lucy_1_anim_6= Movie(play="images/video/ep3/VIP_Lucy_1_anim_6.webm", loop = True)
image sc i_VIP_Sadira_1_anim_1= Movie(play="images/video/ep3/VIP_Sadira_1_anim_1.webm", loop = True)
image sc i_VIP_Sadira_1_anim_2= Movie(play="images/video/ep3/VIP_Sadira_1_anim_2.webm", loop = True)
image sc i_VIP_Sadira_1_anim_3= Movie(play="images/video/ep3/VIP_Sadira_1_anim_3.webm", loop = True)
image sc i_VIP_Sadira_1_anim_4= Movie(play="images/video/ep3/VIP_Sadira_1_anim_4.webm", loop = True)
image sc i_VIP_Sadira_1_anim_5= Movie(play="images/video/ep3/VIP_Sadira_1_anim_5.webm", loop = True)
image sc i_VIP_Sadira_1_anim_6= Movie(play="images/video/ep3/VIP_Sadira_1_anim_6.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_1= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_1.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_2= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_2.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_3= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_3.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_4= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_4.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_5= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_5.webm", loop = True)
image sc i_VIP_Sadira_T_1_anim_6= Movie(play="images/video/ep3/VIP_Sadira_T_1_anim_6.webm", loop = True)
image sc i_Vanessa_anim_1       = Movie(play="images/video/ep3/Vanessa_anim_1.webm", loop = False)
image sc i_Jill_1_anim_1_tmp    = Movie(play="images/video/ep3/Jill_1_anim_1.webm", loop = True)

image sc i_Jill_1_anim_1:
    'sc i_Jill_1_anim_1_tmp'
    pause 8
    'images/video/ep3/Jill_1_anim_1_z.webp'

