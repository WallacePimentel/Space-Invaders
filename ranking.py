from PPlay.sprite import *

def rank (janela,click,bot):
    bot.set_position(janela.width/2 - bot.width/2,janela.height / 2 + 50)
    if click.is_over_object(bot):
        bot = Sprite("z_ranking_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 + 50)
        bot.draw()
    else:
        bot.draw()
