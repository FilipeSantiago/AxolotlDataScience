import copy
from Graphics import BaseBarChartByClass
import collections
import math

class MultipleColumnsBarChartByClass(BaseBarChartByClass.BaseBarChartByClass):

    def handle_data_to_plot_chart(self, unique_attributes, all_classes, column):

        unique_attributes = list(sorted(unique_attributes))
        attribute_values = list(self.attribute_values)
        class_dicts = {}

        attribute_dict = dict.fromkeys(unique_attributes, 0)

        for unique_class in all_classes:
            class_dicts[unique_class] = copy.deepcopy(attribute_dict)

        for class_idx in range(len(all_classes)):
            data_frame = self.df[self.df[column] == all_classes[class_idx]]
            for col_idx in range(len(attribute_values)):
                attribute = attribute_values[col_idx]
                mean = data_frame[attribute].mean()
                class_dicts[all_classes[class_idx]][self.handle_nan(attribute_values[col_idx])] += mean

        for class_value in class_dicts:
            class_dicts[class_value] = collections.OrderedDict(sorted(class_dicts[class_value].items()))

        class_dicts = collections.OrderedDict(sorted(class_dicts.items()))
        return class_dicts

    def avg_label(self, rects, rect_idx, height, avg_values=None, class_value=None):
        if (avg_values is None) or (len(rects) != len(avg_values)):
            return '%d' % height
        else:
            if math.isnan(height):
                height = 0

            difference = 100 * ((height - avg_values[rect_idx]) / avg_values[rect_idx])

            if difference >= 0:
                return '%d \n (+%d%%)' % (height, difference)
            return '%d \n (%d%%)' % (height, difference)
