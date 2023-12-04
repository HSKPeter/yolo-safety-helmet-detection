import os

# Define the path to the labels folder
folder_of_this_file = os.path.dirname(__file__)
labels_folder_path = os.path.join(folder_of_this_file, 'labels')

# Read all filenames in the labels folder
filenames = os.listdir(labels_folder_path)

# Filter txt files
filenames = [x for x in filenames if x.endswith('.txt')]



def get_lines_from_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    lines = content.splitlines()
    f.close()
    return lines


def get_labels_from_lines(lines):
    labels = []
    for line in lines:
        try:
            line_split = line.split(' ')
            label = line_split[0]
            labels.append(label)
        except:
            pass
    return labels


for filename in filenames:
    filepath = os.path.join(labels_folder_path, filename)
    lines = get_lines_from_file(filepath)
    labels_from_lines = get_labels_from_lines(lines)

    for label in labels_from_lines:
        if label in labels:
            labels[label] += 1
        else:
            labels[label] = 1

# Draw a pie chart with the labels
labels_to_plot = []
sizes = []
for label in labels:
    labels_to_plot.append(label)
    sizes.append(labels[label])

print(labels)

# Show percentages in the pie chart
plt.pie(sizes, labels=labels_to_plot, autopct='%1.1f%%')
plt.axis('equal')
plt.show()