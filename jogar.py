from PPlay.sprite import *

def jogar(janela,tecla,click,bot):
    bot.set_position(janela.width/2 - bot.width/2,janela.height/ 2 - 230)

    if click.is_over_object(bot):
        bot = Sprite("z_jogar_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 - 230)
        bot.draw()
        if click.is_button_pressed(1):
            while True:
                janela.set_background_color([0,0,0])
                if tecla.key_pressed("esc"):
                    break
            
                janela.update()
    else:
        bot.draw()