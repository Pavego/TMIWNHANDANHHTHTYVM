label char_s(character,speech=None,pose=None,head=None):
    call char_v(character,speech,None,pose,None,head)
    return

label char_v(character,speech=None,name=None,pose=None,outfit=None,head=None,z_order=3):
    if name!=None:
        $ character['name']=name
    if pose!=None:
        $ character['pose']=pose
    if outfit!=None:
        $ character['outfit']=outfit
    if head!=None:
        $ character['head']=head
    $ command_needed="{} {}{}{}".format(character['name'],character['pose'],character['outfit'],character['head'])
    $ renpy.show(command_needed,zorder=z_order)
    if speech!=None:
        $ character['call'](speech) 
    return