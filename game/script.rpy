#test
define my_dissolve = { "master" : Dissolve(.3) }

define my_long_dissolve = { "master" : Dissolve(4) }
screen splashscreen:
    vbox xalign .5 yalign .5:
        text 'All characters are 18 age or older even if specified otherwise.' xalign .5
        text 'This game contains violence, obscene scenes (naked girls and sex scenes), ' xalign .5
        text 'rude humor, scenes that depict smoking or infrequent use of profanity.' xalign .5
image splashscreen_im = Movie(play='main_interface/splashscreen.webm')





'''Here you can keep track of all the routes, activities, etc. that are available to you. and quickly navigate to the desired one, without wasting time walking around the locations and searching. Next to the avatars of the characters are icons, the decoding of which is next.'''




label splashscreen:
    $ quick_menu = False
    if not persistent.set_volume:
        $ persistent.set_volume = True

        $ _preferences.set_volume('music', .5)
        $ _preferences.set_volume('sound', .5)



    scene splashscreen_im with Dissolve(.5)
    $ renpy.pause(4.5)



    scene expression '#000'
    show screen splashscreen 
    with Dissolve(.5)
    $ renpy.pause(999999999)
    hide screen splashscreen 
    with Dissolve(.5)
    $ renpy.pause(.5)
    return


init python:
    renpy.music.register_channel("movie", mixer="movie_sfx", loop=False, stop_on_mute=False, tight=True, buffer_queue=False, movie=True)

    renpy.music.register_channel('music_2', mixer = 'music') 

    renpy.music.register_channel('music_3', mixer = 'music') 

    renpy.music.register_channel('music_fire', mixer = 'sound') 

    renpy.music.register_channel('movie_images/video/ep2/1.webm_None', mixer = 'music') 

    renpy.music.register_channel('sound_2', mixer='music', loop=False, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True)

    renpy.music.register_channel('sound', mixer='sound', loop=False, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True)

    renpy.music.register_channel('sound_message', mixer='sound', loop=False, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True)

    if persistent.set_music_volume is None:
        renpy.music.set_volume(.5, 'music_1')
        renpy.music.set_volume(.5, 'music_3')
        renpy.music.set_volume(.5, 'music_2')
        persistent.set_music_volume = True


label main_menu:
    if persistent.from_gallery:
        $ ret_men = True
        $ Show('gallery', transition = Dissolve(.5))()
        $ button_menu_now_2 = 'Gallery'
        $ persistent.from_gallery = False
        call screen empty_screen

    jump main_menu_screen


label hide_gallery_label:
    $ Hide('gallery', transition = Dissolve(1))()
    if hasattr(store, 'ret_men'):
        $ del ret_men
    $ button_menu_now_2 = None
    jump main_menu_screen





screen disclaimer_screen:
    add '#000'
    vbox xalign .5 yalign .5:

        text 'Warning!' xalign .5
        text 'In order to maximize the enjoyment of the game we have added music and ambient sounds, including those of an erotic nature.'
        text 'You can adjust the volume and turn off the music in the settings.' xalign .5
        text 'We hope this did not cause you any trouble.' xalign .5
        text 'Enjoy the game!' xalign .5
screen disclaimer_screen_LGBTQ:

    add '#000'
    vbox xalign .5 yalign .5:



        text "Note that our game features different fetishes. If you're not interested in stuff like that at all, you can turn this option off right now." xalign .5
        text "(You can always turn it on later, in the settings.)" xalign .5
        text "Leave this option enabled if you're only interested in some fetishes." xalign .5
        text "Don't worry! We'll ask you beforehand each time there's a chance to encounter such interactions." xalign .5
        text " " xalign .5
        text "Do you want to enable LGBTQ+ and hardcore fetishes?" xalign .5
screen disclaimer_screen_LGBTQ_buttons:


    style_prefix "choice"

    vbox yalign .8:
        textbutton 'Enable' action Return(1) text_color '#fff' text_size 24 text_yalign .5
        textbutton 'Disable' action Return(0) text_color '#fff' text_size 24 text_yalign .5



label change_main_loc:
    show expression '#000a'
    hide screen main_interface
    with Dissolve(.5)
    menu:
        "Academy" if True:
            if locations_now[0] != locations_academy[0]:
                $ locations_now = copy.copy(locations_academy)
                $ location_now  = 'cord_entrance'
        "Campus" if True:

            if locations_now[0] != locations_campus[0]:

                $ location_now  = 'leon_living'
                $ locations_now = copy.copy(locations_campus)
    hide expression '#000a'

    jump main_interface_label


label escape_from_dale:
    show image '#000a' 
    hide screen main_interface
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    show screen black_tmp_screen_menu
    with Dissolve(.5)
    $ nv = renpy.call_screen('confirm', 
        '{size=20}On Sunday evening, all students{/size}\n{size=20} return to Cordale. So you did.', 
        Return('Ok'), None, yes_text = _('Ok'), no_text = _('Ok'),)
    $ day_now -= 1
    $ dow      = 'SUN'
    $ change_location_2('leon_living', 4)
    jump main_interface_label


init python:
    def check_space_name(name):
        for i in name:
            if i != ' ':
                return None
        return True
label start:
    $ wins_house            = 'None'
    $ new_cnq_2             = None
    $ new_cnq               = None
    $ potions               = {

    'Lesser Heal'      : 0,

    'Stoneskin'        : 0,

    'Inspiration'      : 0,

    'Magic Reflection' : 0,


    }


    $ Q_Victoria = 0
    $ Q_Elijah   = 0
    $ Q_Leona    = 0
    $ Q_Lily     = 0
    $ Q_Haley    = 0
    $ Q_Amelie   = 0
    $ Q_Samantha = 0
    $ Q_Jacob    = 0
    $ Q_Molly    = 0
    $ Q_Naomi    = 0
    $ Q_Sabrina  = 0
    $ Q_Audrey   = 0


    $ Q_Victoria_old = 0
    $ Q_Elijah_old   = 0
    $ Q_Leona_old    = 0
    $ Q_Lily_old     = 0
    $ Q_Haley_old    = 0
    $ Q_Amelie_old   = 0
    $ Q_Samantha_old = 0
    $ Q_Jacob_old    = 0
    $ Q_Molly_old    = 0
    $ Q_Naomi_old    = 0
    $ Q_Sabrina_old  = 0
    $ Q_Audrey_old   = 0


    $ audrey_events   = True
    $ audrey_events_3 = True
    $ victoria_events = True
    $ elijah_events   = True
    $ victoria_events = True
    $ leona_events    = True
    $ haley_events    = True
    $ haley_events_2  = True
    $ haley_events_3  = True
    $ elijah_events_2 = True
    $ amelie_events   = True
    $ samantha_events = True
    $ samantha_events_3 = True
    $ jacob_events     = True
    $ molly_events     = True
    $ naomi_events     = True
    $ naomi_event_2    = True
    $ naomi_events_2   = True
    $ naomi_events_3   = True
    $ sabrina_events   = True


    $ lily_events      = True
    $ lily_events_2    = True
    $ lily_events_3    = True
    $ lily_events_4    = True
    $ lily_events_5    = True


    $ audrey_events_set       = []
    $ lily_events_set         = []
    $ lily_events_set_2       = []
    $ lily_events_set_3       = []
    $ lily_events_set_4       = []
    $ lily_events_set_5       = []

    $ audrey_events_set_3     = []
    $ victoria_events_set     = []
    $ elijah_events_set       = []
    $ victoria_events_set     = []
    $ leona_events_set        = []
    $ haley_events_set        = []
    $ haley_events_set_2      = []
    $ haley_events_set_3      = []
    $ elijah_events_set_2     = []
    $ amelie_events_set       = []
    $ samantha_events_set     = []
    $ samantha_events_set_3   = []
    $ jacob_events_set        = []
    $ molly_events_set        = []
    $ naomi_events_set        = []
    $ naomi_events_set_2      = []
    $ naomi_events_set_3      = []
    $ sabrina_events_set      = []


    $ wakeup_sets             = []
    $ lily_view     = True
    $ lily_view_2   = True
    $ lily_view_3   = True
    $ lily_view_4   = None
    $ lily_view_5   = True
    $ audrey_view   = True
    $ audrey_view_3 = True
    $ victoria_view = True
    $ elijah_view   = True
    $ victoria_view = True
    $ leona_view    = True
    $ haley_view_2  = True
    $ haley_view_3  = None
    $ elijah_view_3 = True
    $ amelie_view   = True
    $ samantha_view = True
    $ jacob_view    = True
    $ molly_view    = True
    $ naomi_view    = True
    $ naomi_view_2  = True
    $ sabrina_view  = True
    $ log_message   = {}



    $ books_now             = {}
    $ books_gg              = 0
    $ books_send            = 0
    $ generate_books()

    $ pos_track_now         = 0
    $ persistent.first_game = True
    $ button_menu_now       = None
    $ button_menu_now_2     = None

    $ homes = {

    'Leonheart' :{'now':0, 'new':0, 'add':0},
    'Adderin'   :{'now':0, 'new':0, 'add':0},
    'Crowhive'  :{'now':0, 'new':0, 'add':0},
    'Martenden' :{'now':0, 'new':0, 'add':0},

    }
    $ quick_menu = False
    scene expression '#000' with Dissolve(.5)
    $ events       = {}

    $ locations_now = copy.copy(locations_academy)
    $ time_now     = 1
    $ day_now      = 1
    $ dow          = 'MON'
    $ location_now = 'leon_room_mc'
    $ old_location = None

    $ renpy.pause(.5, hard = True)

    show screen disclaimer_screen 
    with Dissolve(.5)


    $ renpy.pause(99999)

    hide screen disclaimer_screen 
    show screen disclaimer_screen_LGBTQ
    with Dissolve(.5)
    $ LGBTQ =renpy.call_screen('disclaimer_screen_LGBTQ_buttons')
    hide screen disclaimer_screen_LGBTQ
    with Dissolve(.5)









    $ renpy.pause(.5)










    play music 'audio/new/ambience/ambience_street_day2.mp3' fadein .5
    call set_variables_at_start from _call_set_variables_at_start

    $ location_now = 'gg_room'


    $ notes = "{b}Olivia{/b} said I have to talk to Don about this rent thing. \nHe should be in the living room."


    $ old_location = None
    $ renpy.pause(.1, hard = True)
    $ renpy.choice_for_skipping()

    call change_location_optimisation_books_label_2 from _call_change_location_optimisation_books_label_2


    $ quick_menu = True
    scene sc i_1_001 with Dissolve(.5)


    "Hi! My name is..."

label start_input:
    $ Name = renpy.call_screen("input", prompt = "Enter your name", someText='James')
    $ gg   = Name
    if not len(gg) or check_space_name(gg):
        jump start_input



label start_input_2:

    $ Surname = renpy.call_screen("input", prompt = "Enter your surname", someText='Pogger')


    if not len(Surname) or check_space_name(Surname):
        jump start_input_2



    show sc i_1_001 with my_dissolve
    "[Name]" "My name is [Name] [Surname] and I am 18 years old."


    stop music fadeout 1.0
    play music_2 'audio/new/gameplay/keyboard_mous.mp3' fadein 1.0


    show sc i_1_002 with my_dissolve
    "[Name]" "I could have been with my club at the training camp preparing for the soccer season right now."
    show sc i_1_002 with my_dissolve
    "[Name]" "But fate had something else prepared for me."

    show sc i_1_002_2 with my_dissolve

    "[Name]" "Double open fracture..."
    "[Name]" "It's a miracle I'm not crippled."
    "[Name]" "Still, I had to say goodbye to my sports career..."
    "[Name]" "And to the sports scholarship I needed for college."

    stop music_2 fadeout 1.0
    play music 'audio/new/ambience/ambience_street_night.mp3' fadein 1.0

    show sc i_1_003 with my_dissolve
    "[Name]" "So I had to find another way to get an education."
    show sc i_1_003 with my_dissolve
    "[Name]" "Samantha suggested I try photography."
    show sc i_1_003 with my_dissolve
    "[Name]" "As it turned out I am natural at this!"
    show sc i_1_003 with my_dissolve
    "[Name]" "Now I work part-time as a photographer to save money for college."


    stop music fadeout 1.0
    play music_2 'audio/new/Music/background_music1.mp3' fadein 1.0

    show sc i_1_004 with my_dissolve
    "[Name]" "I've been applying filters on photos all day..."
    show sc i_1_004 with my_dissolve
    "[Name]" "I hope the client will be happy."
    show sc i_1_004 with my_dissolve
    "[Name]" "A few more shoots and I'll have enough for a down payment."
    show sc i_1_004 with my_dissolve
    "[Name]" "And I still have time to get out of this shit-hole this semester."

    menu:
        "Continue" if True:

            $ pass
        "Skip prologue" if True:
            jump arthur_label


    play sound 'audio/Door_Knock.mp3'
    show sc i_1_006 with my_dissolve

    "Knock-Knock" ""




    play sound ["<silence .5>", 'audio/new/gameplay/Door_open1.mp3' ]
    scene sc i_1_007 with Dissolve(1)
    $ renpy.pause(9999)






    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music_2')) - 2
        except:
            pos_track_now = 0

    stop music_2 fadeout 1.0
    play music 'audio/new/Music/background_music1.mp3' fadein 10.0
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0





    scene sc i_1_008 with Dissolve(.5)


    $ renpy.pause(9, hard = True)

    $ renpy.pause(9999)

    scene sc i_1_009 with Dissolve(.5)








    "Olivia" "[Name] [Surname]! You've been slacking again?"
    show sc i_1_009 with my_dissolve
    "Olivia" "Well, as it is expected of you!"
    show sc i_1_010 with my_dissolve
    "[Name]" "Please don't start that, Olivia, I've been working all day."
    show sc i_1_009 with my_dissolve
    "Olivia" "Start what?!"
    show sc i_1_009 with my_dissolve
    "Olivia" "What kind of tone is that?"
    show sc i_1_009 with my_dissolve
    "Olivia" "You've been in your room all day!"
    show sc i_1_009 with my_dissolve
    "Olivia" "Or do you think I'm blind?!"
    show sc i_1_010 with my_dissolve
    "[Name]" "But..."
    show sc i_1_009 with my_dissolve
    "Olivia" "No buts!"
    show sc i_1_009 with my_dissolve
    "Olivia" "That's what Don was talking about. You're out of control!"
    show sc i_1_009 with my_dissolve
    "Olivia" "Your ingratitude leaves us no choice."
    show sc i_1_009 with my_dissolve
    "Olivia" "If your mother heard that at 18 years old..."
    show sc i_1_009 with my_dissolve
    "Olivia" "...her son would neither study nor work!"
    show sc i_1_009 with my_dissolve
    "Olivia" "She'd be spinning in her grave!"
    show sc i_1_010 with my_dissolve
    "[Name]" "Olivia..."
    show sc i_1_010 with my_dissolve
    "[Name]" "Leave my mother alone!"
    show sc i_1_011 with my_dissolve
    "Olivia" "Don't you raise your voice at me in my house!"
    show sc i_1_011 with my_dissolve
    "Olivia" "Truth hurts, doesn't it?"
    show sc i_1_010 with my_dissolve
    "[Name]" "You know why this is the way it is!"
    show sc i_1_010 with my_dissolve
    "[Name]" "I'd be at university right now if it wasn't for my leg..."
    show sc i_1_009 with my_dissolve
    "Olivia" "You should have thought of that before!"
    show sc i_1_009 with my_dissolve
    "Olivia" "Sport is always a risk."
    show sc i_1_009 with my_dissolve
    "Olivia" "You should've done less loafing and studied more. Like Ashley!"
    show sc i_1_009 with my_dissolve
    "Olivia" "And now what?"
    show sc i_1_009 with my_dissolve
    "Olivia" "How do you plan to get an education?"
    show sc i_1_010 with my_dissolve
    "[Name]" "I'm working on it."
    show sc i_1_009 with my_dissolve
    "Olivia" "He's working..."
    show sc i_1_009 with my_dissolve
    "Olivia" "I see how hard you’re \"working\"!"
    show sc i_1_009 with my_dissolve
    "Olivia" "[Name], our hospitality is not unlimited."
    show sc i_1_010 with my_dissolve
    "[Name]" "{i}(That's for sure...){/i}"
    show sc i_1_009 with my_dissolve
    "Olivia" "We didn't want this, but you leave us no choice."
    show sc i_1_009 with my_dissolve
    "Olivia" "If you want to throw your life away..."
    show sc i_1_009 with my_dissolve
    "Olivia" "We won't let you do it with your feet dangling off Don's neck!"
    show sc i_1_009 with my_dissolve
    "Olivia" "You're a grown man."
    show sc i_1_009 with my_dissolve
    "Olivia" "You can take care of yourself."
    show sc i_1_010 with my_dissolve
    "[Name]" "What do you mean? Are you kicking me out?"
    show sc i_1_010 with my_dissolve
    "[Name]" "But, Olivia, come on... Where am I supposed to go?"
    show sc i_1_009 with my_dissolve
    "Olivia" "What do you take us for? Savages?"
    show sc i_1_009 with my_dissolve
    "Olivia" "You're my best friend's son, God rest her soul."
    show sc i_1_009 with my_dissolve
    "Olivia" "And I talked Don out of kicking you out."
    show sc i_1_010 with my_dissolve
    "[Name]" "Thank you, I knew..."
    show sc i_1_009 with my_dissolve
    "Olivia" "But!"
    show sc i_1_010 with my_dissolve
    "[Name]" "{i}(Of course there’s a \"but\"!){/i}"
    show sc i_1_009 with my_dissolve
    "Olivia" "We're done supporting you."
    show sc i_1_010 with my_dissolve
    "[Name]" "What?!"
    show sc i_1_009 with my_dissolve
    "Olivia" "From now on, if you want to live here..."
    show sc i_1_009 with my_dissolve
    "Olivia" "Pay your rent as a lodger."
    show sc i_1_010 with my_dissolve
    "[Name]" "What?! What?!"
    show sc i_1_009 with my_dissolve
    "Olivia" "I expect payment by the fifth of every month."
    show sc i_1_010 with my_dissolve
    "[Name]" "You're kidding, right?"
    show sc i_1_009 with my_dissolve
    "Olivia" "You don't have to pay for August, but..."
    show sc i_1_010 with my_dissolve
    "[Name]" "Olivia, hey. Tell me you're kidding..."
    show sc i_1_009 with my_dissolve
    "Olivia" "I need your first and last month's payment in September."
    show sc i_1_009 with my_dissolve
    "Olivia" "Plus a security deposit in case of property damage."
    show sc i_1_010 with my_dissolve
    "[Name]" "What... what kind of nonsense is that?!"
    show sc i_1_010 with my_dissolve
    "[Name]" "How am I supposed to save for school while paying rent? It's a vicious circle!"
    show sc i_1_011 with my_dissolve
    "Olivia" "Young man!"
    show sc i_1_011 with my_dissolve
    "Olivia" "You're under my roof."
    show sc i_1_011 with my_dissolve
    "Olivia" "You follow my rules."
    show sc i_1_011 with my_dissolve
    "Olivia" "You don't like our offer?"
    show sc i_1_011 with my_dissolve
    "Olivia" "Go into the living room and say it to Don's face."
    show sc i_1_011 with my_dissolve
    "Olivia" "Or do you only have the courage to bicker with me?"
    show sc i_1_010 with my_dissolve
    "[Name]" "{i}(Damn it, I knew I shouldn't have fallen for her provocations...){/i}"
    show sc i_1_010 with my_dissolve
    "[Name]" "All right. I'll talk to Don."
    show sc i_1_010 with my_dissolve
    "[Name]" "Maybe he won't be so deaf to reason."
    show sc i_1_009 with my_dissolve
    "Olivia" "Good luck with that."
    show sc i_1_009 with my_dissolve
    "Olivia" "After all, it was his idea."
    show sc i_1_012 with my_dissolve
    $ renpy.pause(99999999)
    show sc i_1_013 with my_dissolve
    $ renpy.pause(99999999)
    play sound 'audio/new/gameplay/Door_close1.mp3'
    show sc i_1_006 with my_dissolve
    $ renpy.pause(99999999)
    scene expression '#000' with Dissolve(1)
    $ config.mouse = None
    $ location_now = 'gg_room'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
