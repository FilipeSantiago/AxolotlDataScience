import numpy as np
import copy
import matplotlib.pyplot as plt


class BarChart:

    def plot_chart(self, attribute_values, class_values, attribute_labels=None):

        unique_attributes = list(set(attribute_values))
        number_of_groups = len(unique_attributes)
        ind = np.arange(number_of_groups)
        width = 0.15
        print(number_of_groups)

        fig, ax = plt.subplots()
        rects = []

        graph_data = self.handle_data_to_plot_chart(attribute_values, class_values)

        width_spacement = 0
        for class_value in graph_data.keys():
            print(list(graph_data[class_value].values()))
            rects.append(ax.bar(ind + width_spacement, list(graph_data[class_value].values()), width))
            width_spacement += width

        ax.set_xticks(ind + width / 2)

        if attribute_labels is not None:
            ax.set_xticklabels(attribute_labels)

        plt.show()

    def handle_data_to_plot_chart(self, attribute_values, class_values):

        all_classes = list(set(class_values))
        class_dicts = {}

        unique_attributes = list(set(attribute_values))
        attribute_dict = dict.fromkeys(unique_attributes, 0)

        for unique_class in all_classes:
            class_dicts[unique_class] = copy.deepcopy(attribute_dict)

        for idx in range(len(attribute_values)):
            class_dicts[class_values[idx]][attribute_values[idx]] += 1

        return class_dicts
