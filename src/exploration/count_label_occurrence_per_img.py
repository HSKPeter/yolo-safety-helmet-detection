import os
import matplotlib.pyplot as plt

def explore_ds3():
    # Define the path to the labels folder
    folder_of_this_file = os.path.dirname(__file__)
    labels_folder_path = os.path.join(folder_of_this_file, os.pardir, 'assets', 'labels', 'ds3', 'train')

    # Read all filenames in the labels folder
    filenames = os.listdir(labels_folder_path)

    # Filter txt files
    filenames = [x for x in filenames if x.endswith('.txt')]

    label_occurrences_per_img = {}


    def get_lines_from_file(filepath):
        f = open(filepath, 'r')
        content = f.read()
        lines = content.splitlines()
        f.close()
        return lines


    def get_labels_occurrence_from_lines(lines):
        labels = {}
        for line in lines:
            try:
                line_split = line.split(' ')
                label = line_split[0]
                if label in labels:
                    labels[label] += 1
                else:
                    labels[label] = 1
            except:
                pass
        return len(labels.keys())


    for filename in filenames:
        filepath = os.path.join(labels_folder_path, filename)
        lines = get_lines_from_file(filepath)
        labels_occurrences = get_labels_occurrence_from_lines(lines)

        if labels_occurrences in label_occurrences_per_img:
            label_occurrences_per_img[labels_occurrences] += 1
        else:
            label_occurrences_per_img[labels_occurrences] = 1

    labels_to_plot = []
    sizes = []
    for occurrences_count in label_occurrences_per_img:
        labels_to_plot.append(occurrences_count)
        sizes.append(label_occurrences_per_img[occurrences_count])

    plt.bar(labels_to_plot, sizes, align='center')
    plt.xlabel('Number of labels per image')
    plt.xticks(labels_to_plot)
    plt.title('Number of labels per image in dataset 3')

    for i in range(len(labels_to_plot)):
        plt.text(labels_to_plot[i], sizes[i] + 0.5, str(sizes[i]), ha='center', va='bottom')

    plt.show()


if __name__ == '__main__':
    explore_ds3()   