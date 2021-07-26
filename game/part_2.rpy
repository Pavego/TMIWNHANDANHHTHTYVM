label p2_start:
    stop music
    hide natsuki
    window hide
    image exception_bg = "#dadada"
    image fake_exception = Text("An exception has occurred.", size=40, style="_default")
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
    show natsuki 5b zorder 3 at h11
    n "HEY!"
    n "WHERE IS THE REST OF MY MOD?"
    n 5f "{nw}"
    moddev "I'm making it as fast as I can, okay?"
    n 5w "WELL, MAKE IT FASTER!"
    $ pause(2)
    n 5b "AS FOR YOU, [player]..."
    n 1d "I hope you enjoyed this early version of the mod!"
    n 5c "Unfortunately, it's not complete yet..."
    n 1d "But it should give you a rough idea of what the full thing is going to be like!"
    n "I hope to see you in the full mod!"
    n "Goodbye, [player]!"
    menu:
        "Goodbye, Natsuki!":
            $ renpy.quit()