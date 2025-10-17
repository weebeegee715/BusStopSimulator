# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pusheen", color="#ebbce3")
define m= Character("Man", color="#1a969d")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky at center

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pusheen typing at left
    with moveinleft

    # These display lines of dialogue.

    p "Im really trying to make a game..."

    p "isnt that cool?"

    p "It's good to always try new things!"

    show pusheen dance

    # pusheen got up

    p "I think I'm making good progress!"

    p "At this rate, i'll be done in no time."

    p "Isnt it weird that we're floating??"

    scene bg flower

    show pusheen flower
    with dissolve

    p "This is much better, right?"

    show man at left
    with moveinleft

    m "Hello pusheen I am the IRS"

    p "You're the entire IRS??"

    m "Don't question me."

    p "I am NOT paying my taxes LOL!!!"

    m "Nahh ur going to jail..."
    # This ends the game.

    return
