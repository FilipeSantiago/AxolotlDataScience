import pandas


class DataManipulation:

    def __init__(self, data_frame):
        self.df = data_frame

    def drop_columns(self, column_names):

        for column_name in column_names:
            self.df = self.df.drop(column_name, 1)

        return self

    def discretize_column(self, column_name, interval):

        number_of_categories = len(interval)
        categories = list(range(0, (number_of_categories-1)))

        self.df[column_name] = pandas.cut(self.df[column_name], interval, labels=categories, right=False)

        return self

    def set_categorical_columns(self, column_names):

        for column_name in column_names:
            self.df[column_name] = self.df[column_name].astype('category')

        cat_columns = self.df.select_dtypes(['category']).columns
        self.df[cat_columns] = self.df[cat_columns].apply(lambda x: x.cat.codes)

        return self

    def get_data_frame(self):
        return self.df
