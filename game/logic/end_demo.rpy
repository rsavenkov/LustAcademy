label end_demo:
    scene expression '#000'
    show expression Text(_('To Be Continued')):
        xalign .5 yalign .5
    with Dissolve(1)
    $ renpy.pause(99999)
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
