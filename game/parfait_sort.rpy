init python:
    import random


    class MangaTitle:
        def __init__(self, series, number):
            self.series=series
            self.number=number
            self.word=series+" #"+str(number)
    
    def check_sortedness(full,sfull):
        X=[full[i]==sfull[i] for i in range(len(sfull))]
        return sum(X)
    


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



label mangasort(transition=True):
            
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
    if persistent.playthrough == 0:
        python:
            ste="It's time to sort the manga!\nTo replace two pieces of manga, select them one after another!"
            ste+="\n\nSort the manga by title first and number second.\n\nThe first item of second column goes after the last item of first column."
        call screen dialog(ste, ok_action=Return())
    python:
        poemgame_glitch = False
        progress = 0
        columnsize = 8

        natsukiTime = renpy.random.random() * 4 + 4
        natsukiPos = renpy.random.randint(-1,1)
        natsukiOffset = 0
        natsukiZoom = 1
        totalcount=columnsize*2
        mangalist = []
        with renpy.file('manganames.txt') as wordfile:
            for line in wordfile:
                
                line = line.strip()
                
                if line == '' or line[0] == '#': continue
                
                
                X = line.split(',')
                used=set()
                for i in range(int(X[3])):
                    a=-1
                    while True:
                        a=random.randint(int(X[1]),int(X[2]))
                        if a not in used:
                            used.add(a)
                            break
                    mangalist.append(MangaTitle(X[0],a))
            sorted_mangalist=sorted(mangalist, key=lambda x:(x.series,x.number))
            sequence=[i for i in range(totalcount)]
            random.shuffle(sequence)
            for i in range(totalcount):
                mangalist[sequence[i]]=sorted_mangalist[i]
            used=set()
            difficulty=totalcount
            for i in range(totalcount):
                if i in used:
                    continue
                cur=i
                while cur not in used:
                    used.add(cur)
                    cur=sequence[cur]
                difficulty-=1




        current=-1
        while True:
            ystart = 152
            cstring = "None" if current==-1 else mangalist[current].word
            ui.text("Move: "+str(progress+1), style="poemgame_text", xpos=810, ypos=50, color='#000')
            ui.text("Current: "+cstring, style="poemgame_text", xpos=810, ypos=80, color='#000')
            columnsize=8
            for j in range(0,columnsize*2,columnsize):
                if j == 0: x = 100
                else: x = 800
                ui.vbox()
                for i in range(columnsize):
                    word = mangalist[i+j]
                    if current==i+j:
                        ui.textbutton("(Empty)", clicked=ui.returns(i+j), text_style="poemgame_text", xpos=x, ypos=i * 24 + ystart)
                        continue
                    ui.textbutton(word.word, clicked=ui.returns(i+j), text_style="poemgame_text", xpos=x, ypos=i * 24 + ystart)
                ui.close()
            
            t = ui.interact()
            renpy.play(gui.activate_sound)
            if current==-1:
                current=t
            else:
                if t!=current:
                    if (t>current)==(mangalist[t].word>mangalist[current].word):
                        renpy.show("n_sticker hop")
                    temp=mangalist[current]
                    mangalist[current]=mangalist[t]
                    mangalist[t]=temp
                current=-1
            progress += 1
            ee=""
            if check_sortedness(mangalist,sorted_mangalist)==columnsize*2:
                break

        
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
