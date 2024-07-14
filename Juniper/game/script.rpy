# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("???")
define m = Character("Me")
define n = nvl_narrator
# define elle = False
#define config.gl2 = True

image bg room= Movie(play="images/bgroom.ogv")

label start:
    $ quick_menu = False
    with introtrans
    n "The same inky, cloying ache has gripped you again today"
    n "It’s worse than usual, you think"
    n "..."
    n "..."
    n "{sc=3}{i}{color=#bdb999}Have you noticed the world burning around us lately?{/sc}"
    nvl clear
    n "You feel the helplessness take hold of you"
    n "You can’t bear to face it today"
    nvl clear
    n "{fi=[0]-[1]-[7]}{i}{color=#99ffd1}“While the world is full of troubles\nAnd anxious in its sleep.\nCome away, O human child!”{/fi}"
    nvl clear
    n "The words narrowly emerge in your thoughts, remnant of an Irish poetry anthology you used to frequent"
    nvl clear
    n "You hadn’t thought about it in a while"
    n "You hadn’t thought about books in a while"
    n "There was too much magic in their pages—you’d yearned to be so consumed in it your surroundings fell away for good"
    nvl clear
    n "It’s childish…"
    n "But… it would soothe your ache"
    n "So you think back to the stories and let yourself fantasize for a moment"
    nvl clear
    n "{fi=[0]-[1]-[5]}{i}{color=#99ffd1}\n\n“To the waters and the wild…”"
    nvl clear
    n "\n\nYou drift off before long..."
    nvl clear

    pause 1.0
    $ quick_menu = True
    scene bg room
    with introtrans
    pause 0.9
    play music "audio/bgm.mp3" fadein 0.3

    "You haven’t dreamt in a while… it’s a welcome change."
    "You spot wisteria, just barely visible."
    "You admire their grace."
    "So awed, you nearly forget their nature."
    "How the wisteria {i}climb{/i} and {i}twist{/i} and {i}cling{/i} along branches so tightly... {b}they strangle the tree to its death.{/b}"
    "..."
    "Your gaze eventually travels downward and you spot a figure you’d somehow managed to miss before."

    show juniper distracted
    with dissolve
    "..."

    show juniper shock
    "Your presence startles her for a moment, but she quickly recovers."
    show juniper smile3
    j "And who are you?"
    $ m = renpy.input("Enter your name:", length=12).strip()
    $ renpy.say(j, " "+str(m)+"...")
    j "I hope that's not your true name."
    j "Names hold power, you know?"
    j "..."
    $ j = "Juniper"
    j "You can call me... Juniper."
    "{i}It's a fitting name, you think. Like the Juniper Hairstreak..."

    define why=True
    define who=True
    menu ask:
        "Why are we here?" if why == True:
            $ why = False
            show juniper smile2
            j "Gorgeous mood lighting, hospitable rocks, what's not to like? You could say... I'm attached to this place. I feel a {i}connection."
            j "..."
            show juniper reminisce
            j "I found it as a little rascal, long ago. I'd sneak out here to meet someone, and we'd just talk under the moonlight until the world forgot about us."
            show juniper smile2
            j "I used to really love this place... and now... I'm..."
            "{i}Used to?"
            show juniper smile3
            j "Anyway, as for you... I've a feeling you already know why you're standing before me."
        "Tell me about yourself" if who == True:
            $ who = False
            j "About me?"
            j "What, are we making small talk here? I've already given you my name."
            j "..."
            show juniper distracted
            j "Fine."
            show juniper smile2
            j "I..."
            j "Really like birds."
            j "They're restless spirits, averse to remaining in one spot for long. Unfettered and boundless."
            j "I feel a kinship with them, you could say."
            show juniper neutral
            j "There, that's all you're going to get."
    
    if why == True or who == True:
        jump ask

    show juniper smile3
    j "Why don't you ask me what you really want to know?"
    menu:
        "{sc=1}{b}{i}{color=#bdb999}Are you real? Are you here... for me?":
            pass
    j "Am I?"
    show juniper form at AnimatedAberate with starTrans
    show juniper form at Reset
    $ renpy.pause(0.1, hard=True)
    show juniper smile3 with starTrans


    "It was just a momentary flicker, but you {i}saw{/i} it. The inhuman luminescence beneath her skin, her eyes. Were those gossamer wings?"
    "The incredible lucidity of what {i}has{/i} to be a dream."
    "A {i}sidhe{/i} of some sort, surely! Known to appear only in response to strong intent."
    "{i}The helplessness loosens its hold."
    "It's all {i}real{/i}."

    j "You've suffered enough, [m]. Let's leave."
    j "All you need to do..."
    j "...is take my hand."

    menu:
        "{sc=2}{b}{color=#bdb999}Accept{/sc}":
            jump accept
        "{sc=2}{b}{color=#bdb999}Refuse{/sc}":
            jump refuse

#     $ renpy.notify("This is a notification")

label refuse:
    stop music
    show juniper peeved
    j "I was trying so hard to avoid doing this…"
    show juniper peeved2
    j "You're making me break a promise, {glitch=78.94}{color=#bdb999}[m]{/color}{/glitch}..."
    "Your thoughts haze the slightest bit and you feel your body involuntarily starts forward."
    "Your hand clasps in hers and a wave of dizziness hits you."
    window hide 
    show chains with introtrans
    window show
    "Her jewelry was… actual chains? What is–?"
    show juniper peeved
    j "Ugh, it always feels so ugly every time I do that."
    show juniper smile2
    j "{sc=2}{i}{size=-9}{color=#bdb999}I promise it’s the last time, Elle.{/size}"
    "The words were so soft, you almost didn’t catch them. They weren’t meant for you."
    hide chains with hpunch
    show juniper smile1
    "You’re too stunned to move—or maybe you {i}can’t{/i} move—as you watch the chains drop on the ground."
    j "Aine above, that feels {i}so good!"
    show juniper neutral
    "She stretches and closes the distance between you two."
    "The shackles that once bound her shoot towards your limbs and clasp shut." with hpunch
    "You finally regain the feeling in your limbs, but it’s too late. You can’t do much other than stare blankly."
    "Your mind is too foggy to even form coherent thoughts…"
    "But… you’re still able to ascertain that something’s missing from you."
    "{i}Stolen{i} from you."
    "As she makes to leave, Juniper meets your gaze one last time and reads the thought you didn’t voice."
    show juniper smile1
    j "Like I told you, sweetheart."
    j "Names hold power."
    hide juniper smile1 with dissolve
    "As the statement registers within your hampered mind, she disappears from view and you’re left accompanied only by the hollow in your identity."
    "This is how it was always going to be."
    "You should’ve known that."
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    "And so the helplessness took hold of you for good."
    window hide
    jump splashscreen_hollowed

label accept:
    "{i}This is it..."
    stop music
    show juniper smile3
    "As your hand meets hers, you’re hit with an abrupt dizzy spell and you see something you couldn’t before."
    window hide 
    show chains with introtrans
    $ renpy.pause(1.0, hard=True)
    window show
    "Chains? Her chain jewelry was..."
    "{i}No... {b}something's wrong."
    "You immediately start to back away."
    j "Agh, finally!"
    hide chains with hpunch
    "The chains drop and she reaches for you immediately." 
    j "Shhh, don't panic, [m]. I know, it’s okay. I see you too."
    j "You, who always read those books and wanted to be them. Not in their place, but {i}them{/i}, because it wouldn't be the same anymore if it was you——you'd ruin it."
    j "Wanting to feel everything but hating what you feel."
    j "Each day, your skin is sordid and your bones are lead. Anchors."
    j "..."
    j "You already live a sedentary life, don’t you?"
    j "This won’t be much different, except… now it finally means something!"
    show juniper peeved
    j "Ugh, no, that’s not–"
    show juniper smile3
    j "What I mean is…"
    j "When you gave me your hand, you gave me a… a gift! One that I’ll make better use of!"
    j "I’m not a villain, [m]… I just wanted to go home!"
    j "And you were so {i}desperate{/i} to escape."
    j "So I… I took my chance. I became what you needed me to be."
    j "..."
    j "{sc=1}{size=+2}{color=#bdb999}Just because your fantasies turned out to be real… doesn't\nmean you're the lead."
    "With that, the chains that once bound her shoot towards your limbs and clasp shut." with hpunch
    hide juniper smile1 with dissolve
    "She glances back one last time and seems almost… apologetic. And then she’s gone."
    "Alone and chained, you release the sobs you’d been holding in for weeks."
    "You recall how that poem ended:"
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    "{fi=[0]-[1]-[7]}{i}{color=#99ffd1}“For the world's more full of weeping than he can understand.”"
    window hide
    jump splashscreen_delusional


label splashscreen_delusional:
    $ quick_menu = False
    scene black with introtrans
    $ renpy.pause(1.0, hard=True)
    show text "Ending: delusional" with dissolve
    $ renpy.pause(5.0, hard=True)
    return

label splashscreen_hollowed:
    $ quick_menu = False
    scene black
    $ renpy.pause(1.0, hard=True)
    show text "Ending: hollowed" with dissolve
    $ renpy.pause(5.0, hard=True)
    return
