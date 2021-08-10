import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pdfkit
from dataProcessing.cleanData import Clean_Data
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from handlers.templateGenerator import template_str

class Get_Stats () :
    def __init__ (self) :
        pass

    def __verify_most_relevant_columns (self, dataset) :
        correlations = dataset.corr()
        correlations.sort_values(["price"], ascending = False, inplace = True)
        correlations = dict(correlations["price"])
        del correlations["price"]
        most_correlated = {key: correlations[key] for key in correlations.keys() if correlations[key] >= 0.6}

        return most_correlated
        
        # 

    def __date_price_relation (self, dataset) :
        graph_col = dataset[["date", "price", "yr_built", "yr_renovated", "zipcode", "id"]]

        # preco por mes
        date_price_df = graph_col.groupby(graph_col["date"].dt.strftime("%m"))["price"].mean()
        date_price_df = date_price_df.to_frame()
        date_price_df.reset_index(level = 0, inplace = True)

        # preco por ano da construcao
        yr_built_price_df = graph_col.groupby(
            pd.cut(
                graph_col["yr_built"], 
                [val for val in range(graph_col["yr_built"].min(), graph_col["yr_built"].max() + 1, 5)]
                )
            )["price"].mean()
        yr_built_price_df = yr_built_price_df.to_frame()
        yr_built_price_df.reset_index(level = 0, inplace = True)
        yr_built_price_df["yr_built"] = [val.left for val in yr_built_price_df["yr_built"]]


        # quantidade de vendas por mês
        qtd_date = graph_col.loc[(graph_col["date"] >= "2014-05-01") & (graph_col["date"] < "2015-05-01")]["date"].dt.strftime("%m").sort_values()

        # criando gráfico
        sns.set(font_scale = 5)
        fig, axes = plt.subplots(2, 2, figsize=(60, 30))
        fig.suptitle("Gráficos")

        sns.lineplot(ax = axes[0, 0], data = date_price_df, x = "date", y = "price")
        axes[0, 0].set_title("Data da venda x preço")
        axes[0, 0].set_xlabel("Mês")
        axes[0, 0].set_ylabel("Média")

        sns.lineplot(ax = axes[0, 1], data = yr_built_price_df, x = "yr_built", y = "price")
        axes[0, 1].set_title("Ano da construção x preço")
        axes[0, 1].set_xlabel("Ano")
        axes[0, 1].set_ylabel("Média")

        sns.histplot(ax = axes[1, 0], data = qtd_date, kde = True)
        axes[0, 1].set_title("Quantidade de casas vendidas por mês")
        axes[0, 1].set_xlabel("Mês")
        axes[0, 1].set_ylabel("Quantidade")
        
        if os.path.exists("./graphs.png"):
            os.remove("./graphs.png")
        fig.savefig("./graphs.png")

    def __create_pdf (self) :
        if os.path.exists("./pdf_test.pdf"):
            os.remove("./pdf_test.pdf")
        config = pdfkit.configuration(wkhtmltopdf = "./wkhtmltopdf.exe")
        wkhtmltopdf_options = {
           'enable-local-file-access': None
        }
        # pdfkit.from_file("./template.html", "pdf_test.pdf", configuration = config, options = wkhtmltopdf_options)
        pdfkit.from_string(template_str, "./pdf_test.pdf", configuration = config, options = wkhtmltopdf_options)

    def get_stats (self) :
        clean_data = Clean_Data()

        dataset = clean_data.main()
        self.__verify_most_relevant_columns(dataset)
        self.__date_price_relation(dataset)
        self.__create_pdf()



get_stats = Get_Stats()

get_stats.get_stats()