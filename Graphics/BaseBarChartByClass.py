import numpy as np
import copy
import math
from abc import ABC, abstractmethod
import collections

class BaseBarChartByClass(ABC):

    def __init__(self, plt, data_frame=None, rows=1, columns=1, x_size=20, y_size=5):
        self.plt = plt
        self.rows = rows
        self.columns = columns
        self.df = data_frame
        self.attribute_values = None
        self.class_values = None
        self.fig, self.ax = self.plt.subplots(rows, columns, figsize=(x_size, y_size))

    def plot_chart(self, title, row_idx, col_idx, attribute_labels=None, bar_width=0.3, avg_values=None, column=None):

        unique_attributes = sorted(['missing' if x is np.nan else x for x in list(set(self.attribute_values))])
        unique_classes = sorted(list(set(self.class_values)))

        if avg_values is not None:
            avg_values = list(collections.OrderedDict(sorted(avg_values.items())).values())

        number_of_groups = len(unique_attributes)
        ind = np.arange(number_of_groups)
        width = bar_width
        rects = []
        graph_data = self.handle_data_to_plot_chart(unique_attributes, unique_classes, column)

        width_spacement = 0
        for class_value in graph_data.keys():
            rect = self.get_ax(row_idx, col_idx).bar(ind + width_spacement, list(graph_data[class_value].values()), width)
            rects.append(rect)
            width_spacement += width
            self.autolabel(rect, row_idx, col_idx, avg_values)

        self.get_ax(row_idx, col_idx).set_title(title)
        self.get_ax(row_idx, col_idx).legend(rects, graph_data.keys())
        self.get_ax(row_idx, col_idx).set_xticks(ind + width / 2)

        if attribute_labels is not None:
            self.get_ax(row_idx, col_idx).set_xticklabels(attribute_labels)
        else:
            self.get_ax(row_idx, col_idx).set_xticklabels(unique_attributes)

    def autolabel(self, rects, row_idx, col_idx, avg_values=None, class_avg=None):

        for rect_idx in range(len(rects)):
            rect = rects[rect_idx]
            height = rect.get_height()
            self.get_ax(row_idx, col_idx).text(rect.get_x() + rect.get_width() / 2., 1. * height,
                    self.avg_label(rects, rect_idx, height, avg_values), ha='center', va='bottom')

    def avg_label(self, rects, rect_idx, height, avg_values):
        if (avg_values is None) or (len(rects) != len(avg_values)):
            return '%d' % height
        else:
            difference = 100 * ((height - avg_values[rect_idx]) / avg_values[rect_idx])

            if difference >= 0:
                return '+%d%%' % difference
            return '%d%%' % difference

    def set_attribute_values(self, attribute_values):
        self.attribute_values = attribute_values
        return self

    def set_class_values(self, class_values):
        self.class_values = class_values
        return self

    def get_ax(self, row_idx, col_idx):

        if self.rows > 1 and self.columns > 1:
            return self.ax[row_idx][col_idx]
        elif self.rows == 1 and self.columns > 1:
            return self.ax[col_idx]
        else:
            return self.ax

    def handle_nan(self, input):

        if self.is_number(input) and math.isnan(input):
            return 'missing'
        return input

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @abstractmethod
    def handle_data_to_plot_chart(self, unique_attributes, all_classes, column=None):
        raise NotImplementedError()
