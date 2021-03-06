image bg = "#82B5E8"

label bird_eye_intro:
    "This is the start of the bird eye section."
    show bg
    with dissolve

    # show bird:
    #     anchor (1.0, 0.5)
    #     xpos 0.0
    # pause 0.25
    # show bird:
    #     align (0.5, 0.5)
    # with move
    # "Show this bird!"
    # show layered_bird
    # "This is the bird with an eye."
    # show layered_bird look_right
    # "Bird looking right."

    # show layered_bird look_down_right
    # "Bird looking."

    # show layered_bird look_up_left
    # "Bird looking."

    # show layered_bird look_up bottom_closed
    # "Bird looking."

    # show layered_bird open
    # "Bird looking."

    # show layered_bird open look_straight

    # hide layered_bird
    # "Bird looking."

    show layered_bird
    "Bird looking."

    show layered_bird:
        easein_elastic 0.25 yoffset -50
        pause 0.15
        linear 0.5 yoffset 0
        repeat
    "Bird hopping excitement."

    #call screen bird_eye_follow
    return

layeredimage layered_bird:
    always "bird"

    group pupil:
        anchor (0.5, 0.5)
        pos (755, 180)

        attribute look_straight default:
            "pupil"
            offset (0, 0)

        attribute look_right:
            "pupil"
            offset (15, 0)

        attribute look_left:
            "pupil"
            offset (-15, 0)

        attribute look_up:
            "pupil"
            offset (0, -15)

        attribute look_down:
            "pupil"
            offset (0, 15)

        attribute look_down_right:
            "pupil"
            offset (12, 12)

        attribute look_down_left:
            "pupil"
            offset (-12, 12)

        attribute look_up_right:
            "pupil"
            offset (12, -12)

        attribute look_up_left:
            "pupil"
            offset (-12, -12)

    group lid:
        pos (755, 180)
        anchor (0.5, 0.5)
        attribute open default:
            Null()
        attribute top_closed:
            "top_lid"
        attribute bottom_closed:
            "bottom_lid"
        attribute squint:
            "squint"

    attribute exclamation:
        pos (550, 25)
        "exclamation"

screen bird_eye_follow:
    add "bird"
