import numpy as np
import copy
import math
from Graphics import BaseBarChartByClass


class SingleColumnBarChartByClass(BaseBarChartByClass.BaseBarChartByClass):

    def handle_data_to_plot_chart(self, unique_attributes, all_classes, column=None):

        attribute_values = list(self.attribute_values)
        class_values = list(self.class_values)

        class_dicts = {}

        attribute_dict = dict.fromkeys(unique_attributes, 0)

        for unique_class in all_classes:
            class_dicts[unique_class] = copy.deepcopy(attribute_dict)

        for col_idx in range(len(attribute_values)):
            class_dicts[class_values[col_idx]][self.handle_nan(attribute_values[col_idx])] += 1

        return class_dicts
