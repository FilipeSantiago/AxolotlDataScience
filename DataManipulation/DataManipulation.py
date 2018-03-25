import pandas
from DataManipulation.Enuns import NormalizeRules
import numpy as np

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

    def normalize_columns(self, columns_names, normalize_rule=None):
        normalize_rules = NormalizeRules.NormalizeRules

        for column_name in columns_names:
            if normalize_rule == normalize_rules.Max:
                normal_factor = self.df[column_name].max()
            else:  # normalize_rules.Mean is default
                normal_factor = self.df[column_name].mean()

            self.df[column_name] = self.df[column_name].div(normal_factor)

        return self

    def divide_by_column(self, numerator_columns, denominator_column, drop_numerator_columns=True):

        relative_columns = [column + '_by_' + denominator_column for column in numerator_columns]
        self.df[relative_columns] = self.df[numerator_columns].div(self.df[denominator_column], axis=0)

        if drop_numerator_columns:
            self.drop_columns(numerator_columns)

        return self

    def get_discretization_intervals_based_on_number_of_groups(self, column, number_of_groups):

        min_value = self.df[column].min()
        max_value = self.df[column].max()

        common_difference = (max_value - min_value)/number_of_groups

        discretization_list = np.arange(min_value, max_value+common_difference, common_difference)

        discretization_list[0] = -np.inf
        discretization_list[number_of_groups] = np.inf

        return discretization_list

    def get_data_frame(self):
        return self.df
