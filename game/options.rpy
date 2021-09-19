









# init 999 python:
#     config.developer = True
#     config.console   = True
#     optimiz          = False
#     debug_now        = True

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc




define config.name = _("LustAcademy")





define gui.show_name = True


define web_version    = False

init python:
    'End at Audrey'


define web_version_load_list = []

define config.version = '0.2.2b'


init -100 python:
    config.developer = False
    config.console   = False
define test = True


init python:
    mp = MultiPersistent("LustAcademy")
    if not mp.gallery:
        mp.gallery = []
        mp.save()

    def unlock_gallery(img):
        if img in gallery_picks and img not in mp.gallery:
            mp.gallery.append(img)
            mp.save()

init -100 python:
    good_saves = ['0.2.1c', '0.2.1f', '0.2.1g', '0.2.1_webp_test', '0.2.2a', '0.2.2b', '0.2.1_new_renpy']


define config.autosave_slots  = 15
define config.quicksave_slots = 15

init 1000 python:
    list_files = renpy.list_files()
    config.image_cache_size   = 3000
    config.predict_statements = 3000
    config.image_cache_size_mb = 3000



define config.main_menu_music = "audio/menu.mp3"
define gui.about = _p("""
""")






define build.name = "Lust-Academy"






define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "LustAcademy-43413566"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/**.xlsx', None)
    build.classify('game/**.py', None)

    build.classify('game/**.rpy', None)
    build.classify("game/**.psd", None)

    build.classify("game/**.mov", None)


    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webp', 'images')



    build.classify('game/**.webm', 'videos')



    build.classify('game/**.rpyc', 'scripts')

    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.ttf', 'archive')

    build.classify('game/**.ogg', 'audios')
    build.classify('game/**.ogg', 'audios')


    build.classify('game/**.mp3', 'audios')
    build.classify('game/**.mp3', 'audios')



    build.archive("scripts", "all")

    build.archive("images", "all")

    build.archive("videos", "all")
    build.archive("audios", "all")









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
