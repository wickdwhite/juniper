image jblink:
    "trans.png"
    choice:
        4.5
    choice:
        4.1
    choice:
        2.1
    choice:
        6.2
    choice:
        0.2
    "images/blink.png"
    .1
    "trans.png"
    .1
    repeat


layeredimage juniper neutral:
    always "juniper neutral.png"
    group eyes:
        attribute o default "jblink"

layeredimage juniper smile1:
    always "juniper smile1.png"
    group eyes:
        attribute o default "jblink"

layeredimage juniper smile2:
    always "juniper smile2.png"
    group eyes:
        attribute o default "jblink"

layeredimage juniper smile3:
    always "juniper smile3.png"
    group eyes:
        attribute o default "jblink"

layeredimage juniper peeved:
    always "juniper peeved.png"
    group eyes:
        attribute o default "jblink"

layeredimage juniper distracted:
    always "juniper distracted.png"
    group eyes:
        attribute o default "jblink"

