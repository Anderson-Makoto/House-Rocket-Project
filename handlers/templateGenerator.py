import os

abs_path = os.path.abspath(".")

# import base64

# def get_image_file_as_base64_data():
#     with open("./graphs.png", 'rb') as image_file:
#         return base64.b64encode(image_file.read())

template_str = f"""
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<div id="header" style="width=100%; border-bottom:solid 10px">

    <h1 style="text-align:center">RELATÓRIO IMOBILIÁRIO</h1>

</div>
<div id="content" style="background-color: yellow">

    <h2>Conteúdo do relatório alterado</h2>
    <img src="{abs_path}\graphs.png" alt="My test image" style="width: 100%">

</div>
"""