import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dataProcessing.getStats import Get_Stats

def start (update, context) :
    context.bot.send_message(
        chat_id = update.effective_chat.id, text = r"Olá, eu fui desenvolvido pelo Anderson Makoto Shinoda. O meu principal objetivo é facilitar a compra e venda de imóveis. Para ver os comandos digite '/help'"
    )

def help (update, context) :
    context.bot.send_message(
        chat_id = update.effective_chat.id, text = default_string
    )

def about (update, context) :
    context.bot.send_message(
        chat_id = update.effective_chat.id, text = about_str
    )

def rel (update, context) :
    get_stats = Get_Stats()
    get_stats.get_stats()
    context.bot.send_document(
        chat_id = update.effective_chat.id, document = open("./pdf_test.pdf", 'rb')
    )

def echo (update, context) :
    context.bot.send_message(
        chat_id = update.effective_chat.id, text = not_found
    )

def unknown (update, context) :
    context.bot.send_message(
        chat_id = update.effective_chat.id, text = not_found
    )

not_found = "Não entendi, por favor, digite '/help' para ver os comandos."

about_str = """
PROJETO HOUSE ROCKET\n\n
Fonte da ideia do projeto: https://medium.com/@meigarom/os-5-projetos-de-data-science-que-far%C3%A1-o-recrutador-olhar-para-voc%C3%AA-c32c67c17cc9\n
Fonte dos dados: https://www.kaggle.com/harlfoxem/housesalesprediction\n
Link do projeto no github: https://github.com/Anderson-Makoto/House-Rocket-Project\n\n
Descrição do projeto:\n
A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia.\n
Você é um Data Scientist contrato pela empresa para ajudar a encontrar as melhores oportunidades de negócio no mercado de imóveis. O CEO da House Rocket gostaria de maximizar a receita da empresa encontrando boas oportunidades de negócio.\n
Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.\n
Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços.\n
Portanto, seu trabalho como Data Scientist é responder as seguinte perguntas:\n\n
1 - Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?\n
2 - Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?\n
3 - A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?
"""

default_string = """
Lista de comandos:\n
/rel - retorna um pdf com relatório completo sobre os preços dos imóveis.\n
/about - Informações sobre este projeto.\n
/pred - realizar predições sobre quais casas comprar no próximo mês e quando revender.
"""