from random import uniform


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def minimum(self):
        return self.left.minimum() if self.left else self.data

    def maximum(self):
        return self.right.maximum() if self.right else self.data

    def __str__(self, indent=''):
        temp = indent + str(self.data)
        temp_indent = ' ' * len(temp) + '-' * (indent.count('-') + 1)
        if self.left and self.right:
            temp += '' + self.left.__str__(temp_indent.strip())
            temp += '\n' + self.right.__str__(temp_indent)
        elif self.left:
            temp += '' + self.left.__str__(temp_indent.strip())
        elif self.right:
            temp += '' + self.right.__str__(temp_indent.strip())
        return temp


def minimum(y, list_of_trees):
    return list_of_trees[int(y)].minimum()


def create_data(n=10):
    data = [round(uniform(0, 3), 2) for _ in range(n)]
    return data


def create_dict_roots(list_of_data):
    tab_keys = []
    dict_roots = {}
    for elem in list_of_data:
        if (int(elem) + 0.5) not in tab_keys:
            tab_keys.append(int(elem) + 0.5)
    tab_keys.sort()
    for key in tab_keys:
        dict_roots[key] = []
    for elem in list_of_data:
        dict_roots[int(elem) + 0.5].append(elem)
    return dict_roots


if __name__ == '__main__':
    values = create_data(10)
    roots = create_dict_roots(values)
    print(roots)
    print(values)
    trees = []
    for i in roots:
        root = Node(i)
        for each in roots[i]:
            root.insert(each)
        print(root)
        print('??????')
        trees.append(root)
        print('??????')
        print(root.maximum())
        print('??????')
    print(trees[0])
    print('jjj')
    print(minimum(2.5, trees))
