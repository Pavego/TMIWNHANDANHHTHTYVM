


label start:
    $ moddev = "MousePotatoDoesStuff"
    $ config.developer=True
    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer

    $ chores=[False,False,False]
    $ chore_names=["go to the bathroom","change clothes", "sort manga"]

    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ n_outfit_mode = 0
    $ n_outfits = ['b','b','']
    $ n_outfit = 'b'
    if persistent.playthrough == 0:
        call nat_welcome
    elif persistent.playthrough == 1:
        call nat_intro
    call p1_start
    call p2_start



label endgame(pause_length=4.0):
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
