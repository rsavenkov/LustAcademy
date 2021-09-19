










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















init python:





    colors_names = {
    "Ring, ring...": "#FFF",
    "Arthur"       : "#1467e3",
    "Sabrina"      : "#ba5a55",
    "Amelie"       : "#aa6400",
    "Molly"        : "#00c120",
    "Gabriella"    : "#005412",
    "Grace"        : "#f15621",
    "Carter"       : "#f12b31",
    "Joshi"        : "#f1ab41",
    "Frida"        : "#3b366e",

    "Gordon"       : "#3bf21e",

    "Jill"         : "#f241fa",
    "Mushroom Girl": "#02150f",

    "Mina"         : "#ffaa3a",
    

    'Adele'        : '#5fff20',
    "Jaina"        : "#FFFF00",
     "Katrina"     : "#0F0",

    "Leona"     : "#F00",
    "Vanessa"   : "#aaaaff",
    
    '[gg]'    : '#8b00ff',
    '[Name]'    : '#8b00ff',
    
    'Olivia'  : '#ffc0cb',
    "Ashlie"    : '#fa2a55',
    
    "Ashley"    : '#fa2a55',
    "Don"     : '#f0a100',

    "Victoria" : "#e75480",
    "victoria" : "#e75480",

    "Jacob"   : "#006400",

    "Unknown Man"  : "#006400",

    "Lily"         : "#024096",

    'Elijah' : '#8b0000',

    "Samantha" : '#d1f010',
    "Naomi"  : "#5ccc00",
    


    "???"     : '#fff',

    "Audrey"       : '#d10025',
    "Hayley"       : '#32a852',

    "Haley"   : '#32a852',

    "Unknown Girl" : '#32a852',

    "Knock-Knock"  : '#fff',

    "KNOCK-KNOCK"  : '#fff',

    "Radio"        : '#fff',

    "Jill"         : '#b20000',
    "Faith"        : '#b20000',
    
    }






screen say(who, what):
    style_prefix "say"
    if hasattr(store, 'say_stop'):
        zorder 999
        timer .1 action Return()
        imagebutton:
            idle '#000'
            hover '#000'
            action Return()
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                if hasattr(store, 'gg'):
                    if who != str(gg) and colors_names.get(who):
                        text unicode(who) id "who" bold True color colors_names[who] outlines [(3, "#000", 0, 0)]

                    else:
                        text unicode(who) id "who" bold True color '#8b00ff' outlines [(3, "#000", 0, 0)]
                else:
                    text unicode(who) id "who" bold True outlines [(3, "#000", 0, 0)]
        text what id "what" color persistent.dialogue_color outlines [(3, "#000", 0, 0)]




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    if persistent.from_gallery:
        key "game_menu" action Jump('end_gallery')
    if hasattr(store, 'nothing_ll'):
        imagebutton:
            idle '#0000'
            hover '#0000'
            action Return()

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos











init 499 image my_img:
    "images/main_interface/caret.png"
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.0
    repeat

init -1:
    $ style.input.caret = "my_img"
init -3 python:
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)




















screen input(prompt="", someText="", label="", win='', pc=False, n_deffault=''):
    default shelp = False

    style_prefix "choice"
    imagebutton idle '#0338' hover '#0338' action NullAction()

    vbox:

        textbutton prompt text_yalign 0.5 action GetText("input","input") text_color '#fff' text_size 24

        textbutton '' yminimum 100 text_color '#FFCA42' text_size 24




    input id "input" default str(someText) xalign 0.5 yalign 0.41 length 10 color '#FFf' allow " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"





















style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










label not_now_label:
    #hide screen main_interface 
    hide screen black_tmp_screen_menu
    with Dissolve(.5)
    "[Name]" "{i}(There's nothing we can talk about right now.){/i}"

    show screen show_hide_locations_2
    show screen main_interface 
    hide screen black_tmp_screen_menu

    with Dissolve(.5)
    jump main_interface_label




init python:
    def get_items_choice(items):
        r_items = []
        for i in items:
            
            if hasattr(store, 'set_now'):
                if i.caption not in set_now:
                    r_items.append(i)
            
            else:
                
                r_items.append(i)
        return(r_items)

    def get_items_choice_debug(items, set_now):
        r_items = []
        for i in items:
            if i not in set_now:
                r_items.append(i)
            
            else:
                
                r_items.append(i)
        return(r_items)



screen choice(items):
    style_prefix "choice"
    zorder 350
    default mmmf = None
    if renpy.get_screen('main_interface'):
        timer .1 action Hide('black_tmp_screen_menu')
        timer .3 action Show('black_tmp_screen_menu')



    if len(get_items_choice(items)) == 1 and items[len(items)-1].caption == 'Not now':
        timer .01 action Jump('not_now_label')
    else:
        vbox yalign .8:
            spacing 5
            for i in items:

                if hasattr(store, 'set_now'):
                    if i.caption not in set_now:
                        if i.caption[:2] in ['10', '20', '30', '40', '50', '60', '70', '80', '90']:
                            textbutton i.caption[2:] action Hide('black_tmp_screen_menu', transition = Dissolve(.5)), i.action:
                                if mmmf == i:
                                    text_color "FFEEDE"
                                else:
                                    text_color '#d9cbbb'
                                text_font "fonts/h_font.ttf" 
                                hovered SetScreenVariable("mmmf", i)
                                unhovered SetScreenVariable("mmmf", None)
                                text_size 18 text_yalign .5

                        elif i.caption[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                            textbutton i.caption[1:] action Hide('black_tmp_screen_menu', transition = Dissolve(.5)), i.action:
                                if mmmf == i:
                                    text_color "FFEEDE"
                                else:
                                    text_color '#d9cbbb'
                                text_font "fonts/h_font.ttf" 
                                hovered SetScreenVariable("mmmf", i)
                                unhovered SetScreenVariable("mmmf", None)
                                text_size 18 text_yalign .5
                        elif i.caption[0] in ['!']:
                            viewport:
                                xmaximum 450
                                ymaximum 45
                                image Frame('gui/button/choice_idle_background.png', borders = Borders(15, 8, 15, 8)) alpha .5
                                image Text(i.caption[1:], size = 18, color = "FFEEDE", font ="fonts/h_font.ttf" ):
                                    #outlines [(1, '#fff', 0, 0)]
                                    yalign .5 
                                    xalign .5
                                    alpha .5
                        else:
                            textbutton i.caption action Hide('black_tmp_screen_menu', transition = Dissolve(.5)), i.action:
                                if mmmf == i:
                                    text_color "FFEEDE"
                                else:
                                    text_color '#d9cbbb'
                                text_font "fonts/h_font.ttf" 
                                hovered SetScreenVariable("mmmf", i)
                                unhovered SetScreenVariable("mmmf", None)
                                text_size 18 text_yalign .5

                else:

                    if i.caption[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:

                        textbutton i.caption[1:] action Hide('black_tmp_screen_menu', transition = Dissolve(.5)), i.action:
                            if mmmf == i:
                                text_color "FFEEDE"
                            else:
                                text_color '#d9cbbb'
                            text_font "fonts/h_font.ttf" 
                            hovered SetScreenVariable("mmmf", i)
                            unhovered SetScreenVariable("mmmf", None)
                            text_size 18 text_yalign .5
                    elif i.caption[0] in ['!']:
                        viewport:
                            xmaximum 450
                            ymaximum 45
                            image Frame('gui/button/choice_idle_background.png', borders = Borders(15, 8, 15, 8)) alpha .5
                            image Text(i.caption[1:], size = 18, color = "FFEEDE", font ="fonts/h_font.ttf" ):
                                #outlines [(1, '#fff', 0, 0)]
                                yalign .5 
                                xalign .5
                                alpha .5
                        #textbutton i.caption[1:] action NullAction():
                        #    image_idle 'gui/button/choice_hover_background.png'
                        #    text_color '#505050'
                        #    text_font "fonts/h_font.ttf" 
                        #    hovered SetScreenVariable("mmmf", i)
                        #    unhovered SetScreenVariable("mmmf", None)
                        #    text_size 18 text_yalign .5
                    else:
                        textbutton i.caption action Hide('black_tmp_screen_menu', transition = Dissolve(.5)), i.action:
                            if mmmf == i:
                                text_color "FFEEDE"
                            else:
                                text_color '#d9cbbb'
                            text_font "fonts/h_font.ttf" 
                            hovered SetScreenVariable("mmmf", i)
                            unhovered SetScreenVariable("mmmf", None)
                            text_size 18 text_yalign .5



    if persistent.from_gallery:
        key "game_menu" action Jump('end_gallery')




define -1 config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")




init python:
    def my_show_settings():
        
        set_button_menu_now_2('Settings')
        
        ShowMenu('preferences')()


    def my_show_history():
        set_button_menu_now_2('History')
        
        ShowMenu('history')()
    tmp_time_now = 1
screen quick_menu():


    zorder 230

    if quick_menu and not persistent.from_gallery and not hide_interface:

        hbox:
            style_prefix "quick"

            xalign .99
            yalign .99
            spacing 5

            if hasattr(store, 'battle_tutorial') and battle_tutorial:
                imagebutton:
                    idle  Transform('main_interface/down_buttons/quest_button_0.png', alpha = .8)
                    hover 'main_interface/down_buttons/quest_button_0.png'
                    selected_idle 'main_interface/down_buttons/quest_button_0.png'


                    action Show('tutorial_screen', 'DUELING ARENA', False)

            if hasattr(store, 'caffe_tutorial') and caffe_tutorial:
                imagebutton:
                    idle  Transform('main_interface/down_buttons/quest_button_0.png', alpha = .8)
                    hover 'main_interface/down_buttons/quest_button_0.png'
                    selected_idle 'main_interface/down_buttons/quest_button_0.png'


                    action SetVariable('hide_interface', True), Show('tutorial_screen', what_tutor= 'CAFE', rtrn= False)

            if renpy.get_screen('main_interface'):
                if hasattr(store, 'ep2start'):
                    imagebutton:
                        idle  Transform('main_interface/down_buttons/quest_button_0.png', alpha = .8)
                        hover 'main_interface/down_buttons/quest_button_0.png'
                        selected_idle 'main_interface/down_buttons/quest_button_0.png'
                        if   renpy.get_screen('quest_log_screen') and quest_log_menu_now == 'CHARACTER INFO':
                            action Show('tutorial_screen', what_tutor= 'CHARACTER INFO', rtrn=False)
                        elif renpy.get_screen('quest_log_screen') and quest_log_menu_now == 'CALENDAR':
                            action [SetVariable('tutorial_bb', 0), SetVariable('tmp_time_now', copy.copy(time_now)), SetVariable('time_now', 2), Hide('quest_log_screen'), Show('quest_log_screen'), Show('tutorial_screen', what_tutor= 'CALENDAR', rtrn=False)]
                        elif renpy.get_screen('lustagram_screen'):
                            action SetVariable('tutorial_bb', 0), Show('tutorial_screen', what_tutor= 'LUSTOGRAM', rtrn=False)
                        else:
                            action SetVariable('hide_interface', True), Show('tutorial_screen', what_tutor= 'HUD INTERFACE', rtrn= False)

                imagebutton:


                    if lightning:
                        idle  Transform('main_interface/down_buttons/hide_1_0.png', alpha = .8)
                        hover 'main_interface/down_buttons/hide_1_0.png'
                        action SetVariable('lightning', False)

                    else:

                        idle  Transform('main_interface/down_buttons/hide_0_0.png', alpha = .8)
                        hover 'main_interface/down_buttons/hide_0_0.png'

                        action SetVariable('lightning', True)
            else:
                imagebutton:
                    idle  Transform('main_interface/down_buttons/back_0.png', alpha = .8)
                    hover 'main_interface/down_buttons/back_0.png'
                    selected_idle 'main_interface/down_buttons/back_0.png'


                    action Rollback()

                imagebutton:
                    idle  Transform('main_interface/down_buttons/skip_0.png', alpha = .8)
                    hover 'main_interface/down_buttons/skip_0.png'
                    selected_idle 'main_interface/down_buttons/skip_0.png'
                    if hasattr(store, 'mmg'):

                        action Jump('sheet_24_end_game')
                    else:

                        action Skip() alternate Skip(fast=True, confirm=True)


            imagebutton:
                idle  Transform('main_interface/down_buttons/menu_0.png', alpha = .8)
                hover 'main_interface/down_buttons/menu_0.png'
                selected_idle 'main_interface/down_buttons/menu_0.png'


                action Function(my_show_history)

            imagebutton:
                idle Transform('main_interface/down_buttons/save_0.png', alpha = .8)
                hover 'main_interface/down_buttons/save_0.png'
                selected_idle 'main_interface/down_buttons/save_0.png'


                action QuickSave()

            imagebutton:
                idle Transform('main_interface/down_buttons/load_0.png', alpha = .8)
                hover 'main_interface/down_buttons/load_0.png'
                insensitive Transform('main_interface/down_buttons/load_0.png', alpha = .5)
                selected_idle 'main_interface/down_buttons/load_0.png'

                action QuickLoad()
            imagebutton:
                idle  Transform('main_interface/down_buttons/sounds_on_1.png', alpha = .8)
                hover 'main_interface/down_buttons/sounds_on_1.png'
                selected_idle  Transform('main_interface/down_buttons/sounds_off_0.png', alpha = .8)
                selected_hover 'main_interface/down_buttons/sounds_off_0.png'
                action Preference("all mute", "toggle")

            imagebutton:
                idle  Transform('main_interface/down_buttons/settings_0.png', alpha = .8)
                hover 'main_interface/down_buttons/settings_0.png'
                selected_idle 'main_interface/down_buttons/settings_0.png'


                action Function(my_show_settings)
















init python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
















init python:
    tmp_button_1 = False
    def on_start_fix_alpha(trans, st, at):
        global tmp_button_1
        if not tmp_button_1:
            trans.alpha = 0.0 
        return None

    def on_start_fix_ypos(trans, st, at):
        global tmp_button_1
        if not tmp_button_1:
            trans.ypos = 43 
        else:
            trans.ypos = 23
        return None
transform -1 UpAlphaEffect:



    ypos 43
    linear 0.2 alpha 1.0 ypos 23

transform -1 DownAlphaEffect:



    function on_start_fix_ypos
    linear 0.2 alpha 1.0 ypos 43



transform -1 UpAlphaImageEffect:



    ypos +20
    linear 0.2 alpha 1.0 ypos 0

transform -1 DownAlphaImageEffect:


    function on_start_fix_alpha
    ypos 0
    linear 0.2 alpha 0.0 ypos 20



init python:
    button_settings  = 0
    button_load      = 0
    button_new_game  = 0
    button_gallery   = 0
    button_credits   = 0
    buttons_help     = 0
    button_load      = 0
    button_save      = 0
    button_history   = 0
    tmp_button       = 0


    button_menu_now   = None
    button_menu_now_2 = None
    button_menu_now_3 = None

    def set_button_menu_now_2(new):
        global button_menu_now_2, button_menu_now_3
        if button_menu_now_2 is not None:
            button_menu_now_3 = copy.copy(button_menu_now_2)
        button_menu_now_2 = copy.copy(new)




    def set_buttons(i, up = False):
        for x in (    'button_settings',  
    'button_load',      
    'button_new_game',  
    'button_gallery',   
    'button_credits',   
    'buttons_help',
    'button_load',
    'button_save', 
    'button_history'):
            if x != i:
                
                SetVariable(x, 0)()
            else:
                if up:
                    SetVariable(x, 1)()


init 99 python:
    config.intra_transition = Dissolve(.5)
    def my_quit():
        Quit()()
    def my_main_menu():
        global button_menu_now_2
        if button_menu_now_2 == 'Load':
            Hide('load', transition = Dissolve(1))()
        if button_menu_now_2 == 'Settings':
            Hide('preferences', transition = Dissolve(1))()
        if button_menu_now_2 == 'Gallery':
            Hide('gallery', transition = Dissolve(1))()
        if button_menu_now_2 == 'Credits':
            Hide('about', transition = Dissolve(1))()
        
        if button_menu_now_2 == 'Help':
            Hide('help', transition = Dissolve(1))()
        
        button_menu_now_2 = None

style mm_menu:
    size 50
init python:
    mm_button_y = -100
screen navigation(main_mm=False):
   
    vbox:
        style_prefix "mm_menu"

        xalign .4
        ypos 500

        spacing gui.navigation_spacing

        if main_menu:
            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'start')
                    unhovered SetVariable('mm_button_y', -100)
                    action Start()
                text _("New game"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'start':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        else:
            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'history')
                    unhovered SetVariable('mm_button_y', -100)
                    action ShowMenu("history")
                text _("History"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'history':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'
            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'save')
                    unhovered SetVariable('mm_button_y', -100)
                    action ShowMenu("save")
                text _("Save"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'save':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        viewport:
            xmaximum 435
            ymaximum 52
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'main_menu_button'
                hovered SetVariable('mm_button_y', 'settings')
                unhovered SetVariable('mm_button_y', -100)
                action ShowMenu("preferences")
            text _("Settings"):
                xalign .5 yalign .5
                size 42 font 'fonts/h_font.ttf'
                if mm_button_y == 'settings':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'
        viewport:
            xmaximum 435
            ymaximum 52
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'main_menu_button'
                hovered SetVariable('mm_button_y', 'load')
                unhovered SetVariable('mm_button_y', -100)
                action ShowMenu("load")
            text _("Load"):
                xalign .5 yalign .5
                size 42 font 'fonts/h_font.ttf'
                if mm_button_y == 'load':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'


        if not main_menu:
            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'mmenu')
                    unhovered SetVariable('mm_button_y', -100)
                    action MainMenu()
                text _("Main Menu"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'mmenu':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        viewport:
            xmaximum 435
            ymaximum 52
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'main_menu_button'
                hovered SetVariable('mm_button_y', 'about')
                unhovered SetVariable('mm_button_y', -100)
                action ShowMenu("about")
            text _("Credits"):
                xalign .5 yalign .5
                size 42 font 'fonts/h_font.ttf'
                if mm_button_y == 'about':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'


        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'help')
                    unhovered SetVariable('mm_button_y', -100)
                    action ShowMenu("help")
                text _("Help"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'help':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'



        if renpy.variant("pc"):



            viewport:
                xmaximum 435
                ymaximum 52
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'main_menu_button'
                    hovered SetVariable('mm_button_y', 'quit')
                    unhovered SetVariable('mm_button_y', -100)
                    action Quit(confirm=not main_menu)
                text _("Quit"):
                    xalign .5 yalign .5
                    size 42 font 'fonts/h_font.ttf'
                    if mm_button_y == 'quit':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'
    hbox:
        yalign .98
        xalign .47
        spacing 8
        imagebutton:
            idle 'main_menu/patreon_button.png'
            hover im.MatrixColor('main_menu/patreon_button.png', im.matrix.brightness(.3))
            action OpenURL('https://www.patreon.com/bearinthenight')
        imagebutton:
            idle 'discord_button'
            hover im.MatrixColor('main_menu/discord_button.png', im.matrix.brightness(.3))
            action OpenURL('https://discord.gg/FgFp9NeKsz')

#    on "show" action Show("discord_patron_screen")


style navigation_button is gui_button
style navigation_button_text is gui_button_text
screen discord_patron_screen:
    hbox yalign .95 xalign 0.01:
        spacing 10
        imagebutton:
            idle 'discord_idle'
            hover 'discord_hover'
            action OpenURL('https://discord.gg/FgFp9NeKsz')
        imagebutton:
            idle 'patreon_idle'
            hover 'patreon_hover'
            action OpenURL('https://www.patreon.com/bearinthenight')
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")







image main_menu_bg_webm = Movie(play='images/main_menu/main_menu_bg.webm', loop = True)
# label patch_notes_label:
#     $ nv = renpy.call_screen('confirm', 
#         '{size=17}On Sunday evening, all students return to Cordale. {/size}\n{size=17}So you did.', 
#         Return('Ok'), None, yes_text = _('Ok'), no_text = _('Ok'),)

# screen patch_notes_screen:


screen main_menu():
    tag menu
    if not persistent.patch_notes:
        timer 0.1 action  Show('confirm', 
        message= "ver[config.version]\n\n{size=17}Hi there!{/size}\n{size=17} You've  downloaded the latest version of Lust Academy! {/size}\n{size=17}If you want to find out what has changed,{/size}\n{size=17}click on the 'Details' button below.{/size}\n{size=15}You can always access patch notes later in the 'Credits' menu.{/size}\n", 
        yes_action = [SetField(persistent, 'patch_notes', True), Hide('confirm'), Show('about_2')], no_action = [SetField(persistent, 'patch_notes', True), Hide('confirm')], yes_text = _('Details'), no_text = _('Not now'),)

    add 'main_menu_bg_webm'
    viewport:
        xmaximum 620
        ymaximum 1080
        xpos 60
        add '#0000'
        add 'main_menu_line' xalign .5
        use navigation








style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):





    style_prefix "game_menu"

    add 'd_menu_bg'
    add 'game_menu_down' yalign 1.0
    text str(title).upper() size 36 color '#FFEEDE' xalign .5 yalign .1 font 'fonts/h_font.ttf'




    hbox:
        style_prefix "mm_menu"

        xalign .5
        yalign .98

        spacing -30

        if main_menu:
            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'
                    action SetVariable('mm_button_y', 'start'), Start()
                text _("New game"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'start':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        else:
            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'
                    action SetVariable('mm_button_y', 'history'), ShowMenu("history")
                text _("History"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'history':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'
            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'
                    action SetVariable('mm_button_y', 'save'), ShowMenu("save")
                text _("Save"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'save':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        viewport:
            xmaximum 230
            ymaximum 50
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'd_menu_button'
                action SetVariable('mm_button_y', 'settings'), ShowMenu("preferences")
            text _("Settings"):
                xalign .5 yalign .5
                size 24 font 'fonts/h_font.ttf'
                if mm_button_y == 'settings':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'
        viewport:
            xmaximum 230
            ymaximum 50
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'd_menu_button'
                action SetVariable('mm_button_y', 'load'), ShowMenu("load")
            text _("Load"):
                xalign .5 yalign .5
                size 24 font 'fonts/h_font.ttf'
                if mm_button_y == 'load':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'


        if not main_menu:
            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'

                    action SetVariable('mm_button_y', 'mmenu'), MainMenu()
                text _("Main Menu"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'mmenu':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'

        viewport:
            xmaximum 230
            ymaximum 50
            imagebutton:
                idle '#0000'
                focus_mask None
                hover 'd_menu_button'
                if renpy.get_screen('about_2'):
                    action SetVariable('mm_button_y', 'about'), Hide('about_2'), ShowMenu("about")
                else:
                    action SetVariable('mm_button_y', 'about'), ShowMenu("about")
            text _("Credits"):
                xalign .5 yalign .5
                size 24 font 'fonts/h_font.ttf'
                if mm_button_y == 'about':
                    color '#FFEEDE'
                else:
                    color '#C0B9DB'


        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'
                    action SetVariable('mm_button_y', 'help'), ShowMenu("help")
                text _("Help"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'help':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'



        if renpy.variant("pc"):



            viewport:
                xmaximum 230
                ymaximum 50
                imagebutton:
                    idle '#0000'
                    focus_mask None
                    hover 'd_menu_button'
                    action SetVariable('mm_button_y', 'quit'), Quit(confirm=not main_menu)
                text _("Quit"):
                    xalign .5 yalign .5
                    size 24 font 'fonts/h_font.ttf'
                    if mm_button_y == 'quit':
                        color '#FFEEDE'
                    else:
                        color '#C0B9DB'
    hbox:
        yalign .98
        spacing 8
        imagebutton:
            idle 'main_menu/patreon_button.png'
            hover im.MatrixColor('main_menu/patreon_button.png', im.matrix.brightness(.3))
            action OpenURL('https://www.patreon.com/bearinthenight')
        imagebutton:
            idle 'discord_button'
            hover im.MatrixColor('main_menu/discord_button.png', im.matrix.brightness(.3))
            action OpenURL('https://discord.gg/FgFp9NeKsz')








    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


    #else:
    imagebutton: 
        idle   Transform('menu_return_button.png', alpha = .69)
        hover 'menu_return_button.png'
        if main_menu:
            action ShowMenu("main_menu")
        else:
            action Return()
        xalign .99
        yalign .99




























style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 145
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45








define -1 gui.about = '''
Sam Torres             - CEO
Jose Cuervo            - Game Designer
Gordon "Mr. G" Goodman - 3D design
Vonner Rom             - Programmer
Maria Triangle         - 2D design
Lilu Dallas            - 2D design
Pablo Alexander        - Plot
'''


transform about_2_transform:
    on show:
        xalign .5 ypos 0
        linear 1 ypos -1080 xalign .5

    on hide:
        ypos -1080 xalign .5
        linear 1 ypos 0 xalign .5



transform about_2_transform_2:
    on show:
        xalign .5 ypos 1080
        linear 1 ypos 0 xalign .5

    on hide:
        ypos 0 xalign .5
        linear 1 ypos 1080 xalign .5


screen about():
    tag menu





    use game_menu(_("Credits"), scroll="viewport")

    add 'credits_0' xalign .5 yalign .5
    add 'credits' xalign .5 yalign .5

    textbutton "Details" xpos 520 ypos 487 action Hide('about'), Show("about_2")



screen about_2():
    #tag menu



    use game_menu(_("Credits"), scroll="viewport")
    
    add 'credits_0' xalign .5 yalign .5
    viewport:
        at about_2_transform
    
        xmaximum 1920
        ymaximum 1080
        image '#0000'
        add 'credits'   xalign .5 yalign .5
    viewport:
        at about_2_transform_2
    
        xmaximum 1920
        ymaximum 1080
        image '#0000'
        viewport:
            xalign .5 yalign .5
            xmaximum 1500
            ymaximum 700
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            image '#0000'
            vbox:
                xalign .5
                for i in [
                'v0.2.2',
                'Fourth release! Time to get to know the world better!',
                'Introduced weekend activities in {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Dale{/color}{/font}. Win a weekly house competition to get there!',
                'Over {font=fonts/roboto_medium.ttf}{color=#ffe2b6}1000{/color}{/font} renders',
                'More than {font=fonts/roboto_medium.ttf}{color=#ffe2b6}55{/color}{/font} animations in 60fps',
                'New in-game locations: {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Dale main street, Shop, Spa, Hotel, Night club.{/color}{/font}',
                '{font=fonts/roboto_medium.ttf}{color=#ffe2b6}12{/color}{/font} new characters.',
                'Improved {font=fonts/roboto_medium.ttf}{color=#ffe2b6}UI\\UX.{/color}{/font}',
                'Improved {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Navigation{/color}{/font} and {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Quest Log.{/color}{/font}',
                'Improved {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Lustagram.{/color}{/font} Sometimes people will answer your comments now.',
                'Reworked all mini-games.',
                'Added {font=fonts/roboto_medium.ttf}{color=#ffe2b6}1{/color}{/font} new mini-game.', 
                'v0.2.1f',
                'Minor patch  with a bunch of fixes and improvements to the game.',
                'Fixed bugs in Lily’s route.',
                'Fixed bugs in Naomi’s route.',
                'Fixed bug with quest log,',
                'Fixed some problems with duels.',
                'Fixed other small errors and bugs',
                'v0.2.1g',
                'Minor update with a bunch of fixes and improvements to the game.',
                'Added Android version.',
                'Fixed prologue mini game crashes.',
                "Fixed problem with Samantha's room in the prologue.",
                'Fixed "Memory run" problem.',
                'Fixed some typos and logic problems.',
                'Fixed other small errors and bugs.',
                'v0.2.1',
                'Third release! Welcome to the Academy. Yay!',
                'This release features the beginning of the main game. ',
                'Introduced open world (sandox mechanics.)',
                'Over {font=fonts/roboto_medium.ttf}{color=#ffe2b6}800{/color}{/font} renders',
                'More than {font=fonts/roboto_medium.ttf}{color=#ffe2b6}30{/color}{/font} animations in 60fps',
                '{font=fonts/roboto_medium.ttf}{color=#ffe2b6}5{/color}{/font} new characters.',
                'Sandbox mechanic.',
                'Added Interface with Quest log and Fast-travel system',
                'Added Sound design for 0.2.1 + some minor fixes for 0.1.2',
                'Added 4 new mini-games',
                'New in-game locations: {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Library, Victoria’s class, Sabrina’s class, Cafe.{/color}{/font}',
                'v0.1.2 Hot-fix',
                'Minor update with a bunch of fixes and improvements to the game.',
                'Added {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Gallery{/color}{/font} (now you can replay all erotic scenes.)',
                'Added a few renders and text, to make some scenes more logical',
                'Fixed some bugs with sounds',
                'Fixed bugs with minigame crashes',
                'Fixed grammar errors',
                'Fixed bug with "Return" button in the main menu',
                "Fixed android version text space. Now it's smaller",
                'v0.1.2E',
                'Minor patch needed to fix one critical bug that caused game crashes.',
                'Fixed a critical bug in a mini-game.',
                'v0.1.2d',
                'Minor patch  with a bunch of fixes and improvements to the game.',
                'Fixed critical bug that caused game crashes.',
                'Fixed small bugs and typos.',
                'Fixed menu glitch.',
                'Retouched additional renders.',
                'v0.1.2',
                'Second Release. The prologue is complete! Yay!',
                'This release includes the second half of the prologue and features:',
                'Over {font=fonts/roboto_medium.ttf}{color=#ffe2b6}200{/color}{/font} renders',
                'More than {font=fonts/roboto_medium.ttf}{color=#ffe2b6}25{/color}{/font} 60 fps animations',
                '{font=fonts/roboto_medium.ttf}{color=#ffe2b6}6{/color}{/font} new characters: {font=fonts/roboto_medium.ttf}{color=#ffe2b6}3{/color}{/font} New girls + {font=fonts/roboto_medium.ttf}{color=#ffe2b6}3{/color}{/font} side characters',
                '{font=fonts/roboto_medium.ttf}{color=#ffe2b6}Updated interface{/color}{/font}',
                'New {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Sound-Design{/color}{/font} for {font=fonts/roboto_medium.ttf}{color=#ffe2b6}v0.1.1{/color}{/font} and {font=fonts/roboto_medium.ttf}{color=#ffe2b6}0.1.2{/color}{/font}',
                
                'New in-game locations: {font=fonts/roboto_medium.ttf}{color=#ffe2b6}Main Hall, Entrance Hall, Inner Garden, Campus, Mystic Forest{/color}{/font}',
                
                'v0.1.1f ',

                'Minor update with a bunch of fixes and improvements to the game.',
                'Fixed bugs and typos.',
                'Added the “Skip” option to the game.',
                'Added emojis and expanded photos to Instagram.',
                'Added default name for MC.',
                'v0.1.1',
                'First Release. Our history starts here! Yay! ',
                'This release included the first half of the prologue and features:',
                'Over {font=fonts/roboto_medium.ttf}{color=#ffe2b6}140{/color}{/font} renders.',
                '{font=fonts/roboto_medium.ttf}{color=#ffe2b6}10{/color}{/font} 60 fps animations.',
                '7 characters.'
                ]:  

                    if 'v0.' in i:
                        text i size 24 font 'fonts/h_font_2.ttf' xalign .5

                    else: 
                        text i size 20 font 'fonts/roboto_regular.ttf' color '#C19273' xalign 0

        








































style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu
    timer 0.1 action SetVariable('button_menu_now_2', 'Save')
    if persistent.from_gallery:
        timer 0.1 action Jump('end_gallery')

    use file_slots(_("Save"))

screen end_gallery():
    tag menu
    timer 0.1 action Jump('end_gallery')





screen load():
    tag menu



    use file_slots(_("Load"))



screen gallery():
    tag menu



    use file_slots(_("Gallery"))

init -100 python:
    gallery_picks = [
    'images/ero/1.png',
    
    'images/ero/2.png',
    
    'images/ero/3.png',
    
    'images/ero/4.png',
    
    'images/ero/Leona.png',
    
    'images/ero/Lily.png',
    
    'images/ero/NV_Haley.png',
    
    'images/ero/NV_Audrey.png',
    
    'images/ero/NV_Samantha.png',
    
    'images/ero/NV_Lily.png',
    
    
    
    
    


    ]


    gallery_names = {
    'images/ero/1.png'           : 'Ashley',
    'images/ero/2.png'           : 'Olivia & Don',
    'images/ero/3.png'           : 'Haley',
    'images/ero/4.png'           : 'Leona & Katrina',
    'images/ero/Leona.png'       : 'Leona',
    'images/ero/Lily.png'        : 'Lily', 
    'images/ero/NV_Haley.png'    : 'Haley',
    'images/ero/NV_Audrey.png'   : 'Audrey',
    'images/ero/NV_Samantha.png' : 'Samantha',
    'images/ero/NV_Lily.png'     : 'Lily',


    }




screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title)
    add 'file_slots_bg' xalign .5 yalign .5
    

    fixed:



        order_reverse True



        button:
            style "page_label"

            key_events True
            xalign 0.5
            yalign .24
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                color '#FFEEDE'
                size 30
                font 'fonts/h_font.ttf'
                value page_name_value













        grid 5 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing 15

            for i in range(5 * 3):

                $ slot = i + 1
                $ ttt  = FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot"))
                viewport:
                    xmaximum 225
                    ymaximum 146
                    imagebutton:
                        idle 'main_menu/slot_idle_background.png'
                        hover im.MatrixColor('main_menu/slot_idle_background.png', im.matrix.brightness(.3))
                        action FileAction(slot)
                    viewport:
                        add Frame(FileScreenshot(slot))
                        ymaximum 124
                    if ttt != "empty slot":
                        add 'load_save_icon' yalign 1.0
                        add Text(ttt, color = '#160F32', size = 10, font = 'fonts/h_font.ttf') alpha .7 xalign .5 yalign .97
















        hbox:
            style_prefix "page"

            xalign 0.5
            yalign .76

            spacing gui.page_spacing


            imagebutton:
                idle Transform('main_menu/arrow_left_right.png')
                hover Transform(im.MatrixColor('main_menu/arrow_left_right.png', im.matrix.brightness(.3)))
                action FilePagePrevious()
                ypos 15
            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto") text_idle_color '#D6B49D' text_hover_color '#FFEEDE' text_selected_color '#FFEEDE' ypos 12

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick") text_idle_color '#D6B49D' text_hover_color '#FFEEDE' text_selected_color '#FFEEDE' ypos 12


            for page in range(1, 10):
                textbutton "[page]" action FilePage(page) text_idle_color '#D6B49D' text_hover_color '#FFEEDE' text_selected_color '#FFEEDE' ypos 12

            imagebutton:
                idle Transform('main_menu/arrow_left_right.png', xzoom = -1)
                hover Transform(im.MatrixColor('main_menu/arrow_left_right.png', im.matrix.brightness(.3)), xzoom = -1)
                action FilePageNext()
                ypos 15






style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")








init python:
    if persistent.dialogue_color is None: 
        persistent.dialogue_color = '#FFF'


    class ColorButton():
        def __init__(self):
            self.color_1   = '#FFC42C'
            self.color_2   = '#ffdf8c'
            self.color_now = self.color_1
        def change_color(self):
            if self.color_now == self.color_1:
                self.color_now = self.color_2
            else:
                self.color_now = self.color_1


init 499 image main_menu_idle_hover_button:
    on idle:
        'images/main_menu/buttons/idle.png' with Dissolve(.2)
    on hover:
        'images/main_menu/buttons/hover.png' with Dissolve(.2)
    on selected_idle:
        'images/main_menu/buttons/hover.png'
    on selected_hover:
        'images/main_menu/buttons/hover.png'

init python:
    if persistent.window is None:
        persistent.window = True
    if persistent.rollback is None:
        persistent.rollback = 'left'

    if persistent.skip is None:
        persistent.skip = []
    if persistent.text_color is None:
        persistent.text_color = '#FFF'

screen preferences():
    tag menu

    use game_menu(_("Settings"), scroll="viewport")
    viewport:
        xmaximum 1360
        ymaximum 613
        add 'settings_blocks' xalign .5 yalign .5
        xalign .5 yalign .5
        viewport:
            xmaximum 668
            ymaximum 613
            add '#0000'
            vbox:
                xpos 42
                ypos 15
                spacing 40
                vbox:
                    text ' DISPLAY' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    spacing 10
                    hbox:
                        spacing 8
                        viewport:
                            xmaximum 290
                            ymaximum 55
                            imagebutton:
                                idle 'settings_button_long_0'
                                hover 'settings_button_long_1'


                                action SetField(persistent, 'fullscreen', True), SetField(persistent, 'window', False), Preference("display", "fullscreen")
                            add Text('FULLSCREEN', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if not persistent.fullscreen:
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 290
                            ymaximum 55
                            imagebutton:
                                idle 'settings_button_long_0'
                                hover 'settings_button_long_1'
                                action SetField(persistent, 'fullscreen', False), SetField(persistent, 'window', True), Preference("display", "window")
                            add Text('WINDOWED', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if not persistent.window:
                                    alpha .3
                                xalign .5 yalign .5
                vbox:
                    text ' ROLLBACK SLIDE' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    spacing 10
                    hbox:
                        spacing 8
                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'rollback', 'left'), Preference("rollback side", "left")
                            add Text('LEFT', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.rollback != 'left':
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'rollback', 'disable'), Preference("rollback side", "disable")
                            add Text('DISABLE', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.rollback != 'disable':
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'rollback', 'right'), Preference("rollback side", "right")
                            add Text('RIGHT', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.rollback != 'right':
                                    alpha .3
                                xalign .5 yalign .5


                vbox:
                    text ' SKIP' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    spacing 10
                    hbox:
                        spacing 8
                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                if 'skip' in persistent.skip:
                                    action Preference("skip", "toggle"), Function(persistent.skip.remove, 'skip')
                                else:
                                    action Preference("skip", "toggle"), Function(persistent.skip.append, 'skip')
                            add Text('UNSEEN TEXT', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if "skip" not in persistent.skip:
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                if "after choices" in persistent.skip:
                                    action Preference("after choices", "toggle"), Function(persistent.skip.remove, "after choices")
                                else:
                                    action Preference("after choices", "toggle"), Function(persistent.skip.append, "after choices")

                            add Text('AFTER CHOICES', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if "after choices" not in persistent.skip:
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                if "transitions" in persistent.skip:
                                    action InvertSelected(Preference("transitions", "toggle")), Function(persistent.skip.remove, "transitions")
                                else:
                                    action InvertSelected(Preference("transitions", "toggle")), Function(persistent.skip.append, "transitions")

                            add Text('TRANSITIONS', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if "transitions" not in persistent.skip:
                                    alpha .3
                                xalign .5 yalign .5



                vbox:
                    text ' TEXT COLOR' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    spacing 10
                    hbox:
                        spacing 8
                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'dialogue_color', '#FFF')
                                
                            add Text('WHITE', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.dialogue_color != '#FFF':
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'dialogue_color', '#3877cf')
                                 
                            add Text('BLUE', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.dialogue_color != '#3877cf':
                                    alpha .3
                                xalign .5 yalign .5

                        viewport:
                            xmaximum 195
                            ymaximum 52
                            imagebutton:
                                idle 'main_menu/settings_button_short_0.png'
                                hover 'main_menu/settings_button_short_1.png'
                                action SetField(persistent, 'dialogue_color', '#FFCA42')
                            add Text('GOLD', size = 16, color = '#FFEEDE', font = 'fonts/h_font.ttf' ):
                                if persistent.dialogue_color != '#FFCA42':
                                    alpha .3
                                xalign .5 yalign .5
                text 'Random text for color test' size 27 color persistent.dialogue_color font 'fonts/h_font.ttf' outlines [(3, '#000', 0, 0)]
        viewport:
            xmaximum 670
            ymaximum 253
            xpos 688
            add '#0000'
            vbox:
                spacing 35
                ypos 25
                xpos 42
                vbox:
                    spacing 10
                    text ' AUTO-FORWARD TIME' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    bar value Preference("auto-forward time"): 
                        left_bar  'main_menu/left_bar.png'
                        right_bar 'main_menu/right_bar.png'
                        xmaximum 595 yminimum 35
                vbox:
                    spacing 10
                    text ' TEXT SPEED' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    bar value Preference("text speed"): 
                        left_bar  'main_menu/left_bar.png'
                        right_bar 'main_menu/right_bar.png'
                        xmaximum 595 yminimum 35

        viewport:
            xpos 690
            ypos 270
            ymaximum 340
            xmaximum 670
            add '#0000'
            vbox:
                spacing 35
                ypos 25
                xpos 42
                vbox:
                    spacing 10
                    text ' MUSIC VOLUME' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    bar value Preference("music volume"): 
                        left_bar  'main_menu/left_bar.png'
                        right_bar 'main_menu/right_bar.png'
                        xmaximum 595 yminimum 35
                

                vbox:
                    spacing 10
                    text ' SOUND VOLUME' color '#FFEEDE' size 20 font 'fonts/h_font.ttf'
                    bar value Preference("sound volume"): 
                        left_bar  'main_menu/left_bar.png'
                        right_bar 'main_menu/right_bar.png'
                        xmaximum 595 yminimum 35
                
                
                hbox:
                    xpos -27
                    textbutton _("MUTE ALL"):
                        ypos 3
                        if persistent.mute:

                            text_idle_color '#69626c'
                            text_hover_color '#FFEEDE'
                        else:
                            text_idle_color '#FFEEDE'
                            text_hover_color '#FFEEDE'
                        text_font 'fonts/h_font.ttf'
                        text_size 20

                        action SetField(persistent, 'mute', not persistent.mute), Preference("all mute", "toggle")
                        style "mute_all_button"

                    imagebutton:
                        if persistent.mute:
                            idle  'mute_icon'
                            hover 'mute_icon'
                        
                        else:
                            idle  'mute_icon_0'
                            hover 'mute_icon_0'
                        
                        focus_mask None
                        action SetField(persistent, 'mute', not persistent.mute), Preference("all mute", "toggle")














style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"


style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():
    tag menu






    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0)#:

        # style_prefix "history"
    image 'help_bg'
    viewport:
        xmaximum 1200
        ymaximum 800
        xalign .8
        yalign .7
        
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            for h in _history_list:

                viewport:


                    ymaximum 80
                    has fixed:
                        yfit True
                    hbox:
                        spacing 5
                        if h.who:

                            label h.who:
                                #style "history_name"
                                substitute False



                                if hasattr(store, 'gg'):
                                    if h.who != str(gg) and colors_names.get(h.who):
                                        text_color colors_names[h.who]

                                    else:
                                        text_color '#8b00ff'
                                text_outlines [(1, "#000", 0, 0)]
                                text_font 'fonts/h_font.ttf'


                                text_bold True
                                text_size 18




                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False

                            color '#fff'
                            font 'fonts/h_font.ttf'
                            outlines [(1, "#000", 0, 0)]
                            size 18

            if not _history_list:
                label _("The dialogue history is empty.") text_font 'fonts/Bodoni.ttf' text_color '#fff' text_outlines [(1, "#000", 0, 0)] text_size 30




define -1 gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"
    $ btns = 'images/main_menu/buttons/'

    use game_menu(_("Help"), scroll="viewport")#:
    image 'help_bg' xalign .5 yalign .5# alpha .95

    hbox xpos 220 ypos 190:
        spacing 20

        vbox:
            spacing 10
            for i in (("left", "Enter", "Advances dialogue and activates the interface."), ("middle", "H", "Hides the user interface."), ("right", "Escape", "Accesses the game menu.")):
                hbox:
                    viewport:
                        xmaximum 140
                        ymaximum 40
                        ypos 30
                        image 'really_short_button_help'
                        text  i[1] size 20 color '#FFEEDE' xalign .5 yalign .48 font 'fonts/h_font.ttf'
                    text "or" size 24 color '#EFC8AD' font 'fonts/h_font.ttf' ypos 30
                    viewport:
                        xmaximum 60
                        ymaximum 80
                        image '#0000'
                        image 'help_'+i[0]+'_mouse' xalign .5 yalign 1.0
                    text i[2] size 24 color '#EFC8AD' font 'fonts/h_font.ttf' ypos 30
                    spacing 15

            for i in (
                
                ("Page Down",  _("Rolls forward to later dialogue.")),

                ("I",          _("Opens the inventory menu.")),

                ("P",          _("Opens the phone menu.")),

                ("Q",          _("Opens the list of available routes.")),



                ):
                hbox:
                    viewport:
                        xmaximum 140
                        ymaximum 40
                        image 'really_short_button_help'
                        text  i[0] size 20 color '#FFEEDE' xalign .5 yalign .48 font 'fonts/h_font.ttf'

                    text i[1] size 24 color '#EFC8AD' font 'fonts/h_font.ttf' ypos 5
                    spacing 15
        vbox:
            ypos 30
            spacing 10
            for i in (
                ("S",          _("Takes a screenshot.")),
#                ( "V" , _("Enables a self-voicing mode.")),
                ("M",          _("Opens the map.")),

                ("Space", _("Advances dialogue without selecting choices.")),
                
                ("Ctrl",       _("Skips dialogue while held down.")),

                ("Tab",        _("Toggles dialogue skipping.")),

                ("Page Up",    _("Rolls back to earlier dialogue.")),

                ("L",          _("Highlights all active objects.")),

                ("F",          _("Enables fullscreen mode.")),
                
                ("Arrow Keys", _("Navigate the interface.")),

                ):
                hbox:
                    viewport:
                        xmaximum 140
                        ymaximum 40
                        image 'really_short_button_help'
                        text  i[0] size 20 color '#FFEEDE' xalign .5 yalign .48 font 'fonts/h_font.ttf'

                    text i[1] size 24 color '#EFC8AD' font 'fonts/h_font.ttf' ypos 5
                    spacing 15

    #     style_prefix "help"

    #     vbox:
    #         spacing 23

    #         hbox xpos 100:
    #             spacing 25
    #             for i in [(_("KEYBOARD"), SetScreenVariable("device", "keyboard"), ColorButton()), (_("MOUSE"), SetScreenVariable("device", "mouse"), ColorButton())]:

    #                 viewport:
    #                     xmaximum 261
    #                     ymaximum 40

    #                     imagebutton:
    #                         idle btns+'idle.png' hover btns+'hover.png'
    #                         selected_idle btns+'hover.png'
    #                         action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), i[1]
    #                     text Text(i[0], color = '#000', size = 18, font = 'fonts/Bodoni.ttf') xpos 42 yalign .56















    #         if device == "keyboard":
    #             use keyboard_help
    #         elif device == "mouse":
    #             use mouse_help
    #         elif device == "gamepad":
    #             use gamepad_help








screen keyboard_help():









    hbox xpos 200 ypos 100:
        label _("Enter") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Advances dialogue and activates the interface.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Space") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Advances dialogue without selecting choices.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Arrow Keys") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Navigate the interface.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Escape") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Accesses the game menu.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Ctrl") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Skips dialogue while held down.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Tab") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Toggles dialogue skipping.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Page Up") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Rolls back to earlier dialogue.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos 200 ypos 100:
        label _("Page Down") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Rolls forward to later dialogue.") color "#808080" bold True outlines [(1, "#000", 0, 0)]


    hbox xpos -300 ypos -277:
        label _("I") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Opens the inventory menu.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("P") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Opens the phone menu.") color "#808080" bold True outlines [(1, "#000", 0, 0)]

    hbox xpos -300 ypos -277:
        label _("Q") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Opens the list of available routes.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("M") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Opens the map.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("L") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Highlights all active objects.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("F") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Enables fullscreen mode.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("H") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Hides the user interface.") color "#808080" bold True outlines [(1, "#000", 0, 0)]
    hbox xpos -300 ypos -277:
        label _("S") text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
        text _("Takes a screenshot.") color "#808080" bold True outlines [(1, "#000", 0, 0)]



screen mouse_help():

    for i in [("Left Click", "Advances dialogue and activates the interface."), ("Middle Click", "Hides the user interface."), ("Right Click", "Accesses the game menu.")]:

        hbox xpos -100 ypos 100:
            label i[0] text_size 18 text_outlines [(1, "#000", 0, 0)] text_color '#fff'
            text i[1] color "#808080" bold True outlines [(1, "#000", 0, 0)]























screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button") text_font 'fonts/Tahoma.ttf' text_size 24
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0














screen confirm(message, yes_action, no_action, yes_text = _("Yes"), no_text = _("No"), dont_ask_again = None):
    key "rollback" action NullAction()

    zorder 1000

    style_prefix "confirm"


    imagebutton: 
        idle  '#0003'
        hover '#0003'
        action NullAction()
    add 'check' yzoom 1.5 xalign .5 yalign .5
    viewport:
        xmaximum 540
        ymaximum 310
        add '#0000'
        xalign .5 yalign .5
        if '\n' in message:
            $ message = message.split('\n')
            vbox:
                xalign .5
                yalign .3
                for i in message:

                    text _(i):
                        size 24 font 'fonts/h_font.ttf'
                        color '#292C4B'
                        xalign .5
                    
        else:
            text _(message):
                size 24 font 'fonts/h_font.ttf'
                color '#292C4B'
                xalign .5
                yalign .3

        hbox:
            xalign 0.5
            yalign .85
            spacing 50
            if no_action is not None:
                viewport:
                    xmaximum 130
                    ymaximum 45
                    imagebutton:
                        idle 'button_0'
                        hover 'button_1'
                        if dont_ask_again is not None:
                            action dont_ask_again[1], no_action
                        else:
                            action no_action
                    text no_text xalign .5  yalign .48 font 'fonts/h_font.ttf'   size 24 color '#FFEEDE'
            viewport:
                xmaximum 130
                ymaximum 45
                imagebutton:
                    idle 'button_0'
                    hover 'button_1'
                    action yes_action
                text yes_text xalign .5 yalign .48 font 'fonts/h_font.ttf'   size 24 color '#FFEEDE'


        if dont_ask_again is not None:
            hbox:
                spacing 5
                if dont_ask_again[2]:
                    imagebutton: 
                        idle  'gui/checkbox_1.png' 
                        hover 'gui/checkbox_1.png'
                        action dont_ask_again[1]
                        ypos 3
                else:
                    imagebutton: 
                        idle  'gui/checkbox_0.png' 
                        hover 'gui/checkbox_0.png'
                        action dont_ask_again[0]
                        ypos 3
                
                image Text("Please don't ask me again.", size = 15, font = 'fonts/h_font.ttf', color = "#292C4B") alpha .7 
                xalign .5 yalign 1.0














    if dont_ask_again is not None:
        key "game_menu" action dont_ask_again[1], no_action

    else:
        key "game_menu" action no_action



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
