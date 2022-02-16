# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Nyx", image="nyx")
define c = Character("Crow", image="crow")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg abysssky1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nyx happy 

    # These display lines of dialogue.

    e "Meow, what's up?"
   
    scene bg abysssky1
    show nyx happy
    e "Nice to meet you"
    
    hide bg abysssky1
    
    scene bg abysssky2
    show crow seriousmouthclose
    
    scene bg abysssky2
    show crow seriousmouthopen
    c "We are gonna go somewhere today"
    
    scene bg abysssky2
    show crow seriousmouthclose
    c "Understood?"

    # This ends the game.

    return
