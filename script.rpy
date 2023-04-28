# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Natally")
define b = Character("Luke")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene escola

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show natally

    # These display lines of dialogue.



    e "Olá "

    e "Menino venha aqui, qual seu nome?"

    hide natally

    show lukke

    b "Eu sou o Luke"

    hide lukke

    show natally

    e "Já vi você pela escola"

    e "Você me conhece?"

    hide natally

    show lukke

    b "Não, sou novo aqui nessa escola"

    hide lukke

    show natally

    e "Ah sim, se quiser podemos ser amigos"

    hide natally

    show lukke

    b "Claro, mas agora vamos para a sala, pois a aula ja vai começar"

    hide lukke

    show natally


    e "Você não quer matar aula?"

    hide natally

    show lukke
menu:

    "Não vou matar aula.":
        jump aula1

    "Sim,vamos vai ser legal.":
        jump aula2

   
label aula1:

    b "Eu não faço essse tipo de coisa."

    jump marry

label aula2:

    b "Para onde iremos ir? O que vamos fazer?."

    jump marryi

label marry:

    b "De qualquer modo é melhor ir para a aula"

    jump marry1

label marryi:

    b "Estou ansioso para o nosso dia"

label marry1:
    scene sala

    hide lukke

    show natally

    e "Você tinha razão foi bem melhor vim para a aula, não sabia que hoje teria prova"

    hide natally

    show lukke

    b "Sim, ainda bem que viemos, mas se você  quiser depois daqui podemos sair e ir a algum lugar, o que acha?"

    hide lukke

    show natally 

    e "Claro eu adoraria, vai ser legal!"

    e "Para onde iremos?"

    hide natally

    show lukke

    b "Você prefere ir ao cinema ou a sorveteria?"

    hide luke

    show natally

menu:
    "Cinema":
        jump cineminha

    "Sorveteria":
        jump sorveteria

label cineminha:
    e "Qual filme iremos assistir?"

    hide natally

    show lukke

    b "o que acha de panico 5?"

    hide lukke

    show natally

    e "Ah, pode ser"

    jump cinemmaa

label sorveteria:
    e "Qual sorvete iremos tomar?"

    hide natally

    show lukke

    b "O que acha de açai?"

    hide luke

    show natally

    e "Pode ser, eu amo açai"

    jump açai




    # This ends the game.

    return
