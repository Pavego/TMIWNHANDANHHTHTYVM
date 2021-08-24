


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


label ending(ending_id=0):
    scene bg black
    stop music
    hide natsuki
    window hide
    python:

    image exception_bg = "#dadada"
    image fake_exception = Text("An ending has occurred.", size=40, style="_default")
    $ ending_text="Ending {}.".format(ending_id)
    image fake_exception2 = Text(, size=20, style="_default")
    image fake_exception2 = Text("File \"game/script.rpy\", line 35\nSee traceback.txt for details.", size=20, style="_default")
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("ScriptError: could not find label 'p2_start'.", False)
        except: pass
    $ pause(1)


label endgame(pause_length=4.0):
    "If you are reading this, it means that an ending is missing."
    "Please report this bug as instructed in the README file."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
