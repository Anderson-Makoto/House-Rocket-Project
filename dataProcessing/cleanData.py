import pandas as pd

class Clean_Data () :
    
    def __init__ (self) :
        pass

    def main (self) :
        dataset = self.__open_dataset()
        dataset = self.__tranform_categorical_to_numerical(dataset)
        dataset = self.__remove_null_entries_if_higher_than_70_percent(dataset)

        return dataset

    def __open_dataset (self) :
        dataset = pd.read_csv("./dataProcessing/kc_house_data.csv")
        return dataset

    def __tranform_categorical_to_numerical (self, dataset) :
        # neste dataset, somente a tabela date estava como object
        dataset["date"] = pd.to_datetime(dataset["date"])

        return dataset
    
    def __remove_null_entries_if_higher_than_70_percent (self, dataset) :
        null_col = [col for col in dataset.columns 
            if (dataset[col].isnull().sum(axis = 0) / dataset.shape[0]) >= .7
        ]
        dataset = dataset.drop(null_col, axis = 1)

        return dataset
