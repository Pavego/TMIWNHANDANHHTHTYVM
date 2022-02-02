init python:
    import random


    class CupcakeWord:
        def __init__(self, word, sPoint, mPoint, mcPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.mPoint = mPoint
            self.mcPoint = mcPoint
            self.glitch = glitch

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    mcTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    monikaPos = 0
    mcPos = 0
    sayoriOffset = 0
    monikaOffset = 0
    mcOffset=0
    sayoriZoom = 1
    monikaZoom = 1
    mcZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMC(trans, st, at):
        if st > mcTime:
            global mcTime
            mcTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0

    def randomMoveMC(trans, st, at):
        global mcPos
        global mcOffset
        global mcZoom
        if st > .16:
            if mcPos > 0:
                mcPos = renpy.random.randint(-1,0)
            elif mcPos < 0:
                mcPos = renpy.random.randint(0,1)
            else:
                mcPos = renpy.random.randint(-1,1)
            if trans.xoffset * mcPos > 5: mcPos *= -1
            return None
        if mcPos > 0:
            trans.xzoom = -1
        elif mcPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * mcPos
        mcOffset = trans.xoffset
        mcZoom = trans.xzoom
        return 0



label cupcake_defense(transition=True, cd_file='cupcakewords.txt'):
    stop music fadeout 2.0
    scene bg notebook
    show screen quick_menu
    show s_sticker at sticker_left
    show mc_sticker at sticker_mid
    show m_sticker at sticker_right
    if transition:
        with dissolve_scene_full
    play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0:
        call screen dialog("It's time to write some words on cupcakes!\n\nClub members may be tempted if there are enough of their favourite on it...", ok_action=Return())
    python:
        WIN_CONDITION = 45
        numWords=10

        full_cupcakelist = []
        with renpy.file(cd_file) as wordfile:
            for line in wordfile:
                
                line = line.strip()
                
                if line == '' or line[0] == '#': continue
                
                
                x = line.split(' ')
                if len(x)==2:
                    WIN_CONDITION=int(x[0])
                    numWords=int(x[1])
                else:
                    full_cupcakelist.append(CupcakeWord(x[3], int(x[0]), int(x[1]), int(x[2])))
        a,b,c=0,0,0
        for t in full_cupcakelist:
            a+=t.sPoint
            b+=t.mPoint
            c+=t.mcPoint
    # call screen dialog("{} {} {}".format(a,b,c), ok_action=Return())
    python:
        outcome=-1
        sPointTotal = 0
        mPointTotal = 0
        mcPointTotal = 0
        wordlist = list(full_cupcakelist)

        sayoriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        mcTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        monikaPos = renpy.random.randint(-1,1)
        mcPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        monikaOffset = 0
        mcOffset = 0
        sayoriZoom = 1
        monikaZoom = 1
        mcZoom = 1





        for progress in range(1,numWords+1):
            ystart = 160
            ui.text(str(progress) + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            ui.text("Sayori: "+str(sPointTotal), style="poemgame_text", xpos=80, ypos=200, color='#000')
            ui.text("Monika: "+str(mPointTotal), style="poemgame_text", xpos=80, ypos=280, color='#000')
            ui.text(protag_name+": "+str(mcPointTotal), style="poemgame_text", xpos=80, ypos=360, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()
            t = ui.interact()
            if t.sPoint!=0:
                renpy.show("s_sticker hop")
            if t.mcPoint!=0:
                renpy.show("mc_sticker hop")
            if t.mPoint!=0:
                renpy.show("m_sticker hop")
            sPointTotal += t.sPoint
            mPointTotal += t.mPoint
            mcPointTotal += t.mcPoint
            if max(sPointTotal,mPointTotal,mcPointTotal)>=WIN_CONDITION:
                break
        
        if mPointTotal >= WIN_CONDITION:
            outcome=2
        if mcPointTotal >= WIN_CONDITION:
            WIN_CONDITION=mcPointTotal
            outcome=1
        if sPointTotal >= WIN_CONDITION:
            WIN_CONDITION=sPointTotal
            outcome=0
    call screen dialog("Sayori:{}\n{}:{}\nMonika:{}".format(sPointTotal,protag_name,mcPointTotal,mPointTotal), ok_action=Return())
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    $ pause(1.0)
    return

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image mc_sticker:
    "images/chibi_protag/chibi_hover.png"
    xoffset mcOffset xzoom mcZoom
    block:
        function randomPauseMC
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMC
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image mc_sticker hop:
    "images/chibi_protag/mcchibijump.png"
    xoffset mcOffset xzoom mcZoom
    sticker_jump
    xoffset 0 xzoom 1
    "mc_sticker"

image s_sticker jumps:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_jump
    xoffset 0 xzoom 1
    "s_sticker"

image mc_sticker jumps:
    "images/chibi_protag/mcchibijump.png"
    xoffset mcOffset xzoom mcZoom
    sticker_jump
    xoffset 0 xzoom 1
    "mc_sticker"

image m_sticker jumps:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_jump
    xoffset 0 xzoom 1
    "m_sticker"

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_jump:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset -40
    easein_quad .18 yoffset -120
    easeout_quad .18 yoffset -80
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
