init python:
    import random


    class Item:
        def __init__(self, question, answers, correctIndex):
            self.question=question
            self.answers=answers
            self.correctIndex=correctIndex
    


    natsukiTime = renpy.random.random() * 4 + 4
    natsukiPos = 0
    natsukiOffset = 0
    natsukiZoom = 1

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0



label recipe_quiz(transition=True):
            
    stop music fadeout 2.0
    scene white
    show screen quick_menu
    show n_sticker at sticker_true_mid
    if transition:
        with dissolve_scene_full
    play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    python:
        questions=[]
        with renpy.file('recipe_quiz.txt') as wordfile:
            L=[]
            M=[L]
            for line in wordfile:
                line = line.strip()
                if line == '' or line[0] == '#':
                    L=[]
                    M.append(L)
                else:
                    L.append(line)
            for L in M:
                if len(L)<3:
                    continue
                Q=Item(L[0],L[2:],int(L[1]))
                if Q.correctIndex>=len(Q.answers):
                    Q.correctIndex=0
                questions.append(Q)

    if persistent.playthrough == 0:
        python:
            ste="You copied the recipe. Now you need to read it!\n\n"
            ste+="I'll ask you a few questions about the ingredients and cooking process."
        call screen dialog(ste, ok_action=Return())
    jump rq_start
label rq_fail:
    python:
        ste="That's not quite right...let's try again!"
    call screen dialog(ste, ok_action=Return())
label rq_start:
    python:
        poemgame_glitch = False

        natsukiTime = renpy.random.random() * 4 + 4
        natsukiPos = renpy.random.randint(-1,1)
        natsukiOffset = 0
        natsukiZoom = 1



        qCount=len(questions)
        current=0
        random.shuffle(questions)
        while current!=qCount:
            ystart = 152
            CQ=questions[current]
            current += 1
            ui.text("Question "+str(current)+" of "+str(qCount), style="poemgame_text", xpos=810, ypos=50, color='#000')
            ui.text("Question "+str(current)+" of "+str(qCount), style="poemgame_text", xpos=100, ypos=100, color='#000')
            columnsize=8
            y_pos=ystart
            i=0
            for e in CQ.answers:
                ui.vbox()
                ui.textbutton(e, clicked=ui.returns(i), text_style="poemgame_text", xpos=100, ypos=y_pos)
                y_pos+=100
                i+=1
                ui.close()
            t = ui.interact()
            renpy.play(gui.activate_sound)
            if t!=CQ.correctIndex:
                current=-1
                break
    if current==-1:
        jump rq_fail
    

        
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    $ pause(1.0)
    return

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat
image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

transform sticker_true_mid:
    xcenter 640 yalign 0.9 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
