


label start:
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
    $ ch_natsuki=dict()
    $ ch_natsuki['call']=n
    $ ch_natsuki['name']='natsuki'
    $ ch_natsuki['pose']='1'
    $ ch_natsuki['outfit']='b'
    $ ch_natsuki['head']='a'
    $ gameBegan=False
    if persistent.playthrough == 0:
        call nat_welcome
    else:
        call nat_intro
    call p1_start
    $ gameBegan=True
    call p2_start
    call p3_start

label ending(ending_name, ending_detailed_name=None):
    $ ending_title=ending_name
    $ ending_title+=(" "+ending_detailed_name) if ending_detailed_name is not None else ""
    scene bg black
    stop music
    hide natsuki
    window hide
    python:
        with renpy.file("endings.txt") as ending_file:
            record=True
            L=[]
            b=False
            for line in ending_file:
                line = line.strip()
                ending_list=line.split(" ")+["",""]
                if ending_list[0]=='<ending>':
                    b=ending_list[1]==ending_name
                    if b:
                        L.append(ending_name+"\n")
                    continue
                if b:
                    L.append(line)
                    if line=="<norecord>":
                        record=False
            if record:
                persistent.endingsAchieved.add(ending_name)
            L.append("\nEndings achieved:")
            for e in persistent.endingsAchieved:
                L.append(e)
            L.append("\n\nNext episode of Parfait Girls: "+str(persistent.next_parfait))
    image fauxception = Text("An ending has occurred.", size=40, style="_default")
    image fauxception2 = Text("See ending.txt for details.", size=20, style="_default")
    show exception_bg zorder 2
    show fauxception zorder 2:
        xpos 0.1 ypos 0.05
    show fauxception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        F=open("ending.txt","w")
        F.write("\n".join(L))
        F.close()
        persistent.endings_test=time.time()
        L.append("<ending>")
        if gameBegan:
            persistent.playthrough+=1
        i=0
label ending_loop:
    python:
        line=L[i]
        i+=1
    if line=="":
        jump ending_loop
    if line=="<ending>":
        $ renpy.quit()
    "[line]"
    jump ending_loop
    


label endgame(pause_length=4.0):
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
