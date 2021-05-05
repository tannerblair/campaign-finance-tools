from collections import Counter

import dataset
from pyvis.network import Network


def get_recipient_contributions(recipient, data):
    return [contribution for contribution in data if contribution['recipient'] == recipient]


def add_shared_recipients(net, recipient, data, count=8):
    net.add_node(recipient)

    subset = get_recipient_contributions(recipient, data)

    donors = [contribution['donor'] for contribution in subset]
    for contribution in data:
        if contribution['donor'] in donors and contribution['recipient'] != recipient:
            subset.append(contribution)

    c = Counter([contribution['recipient'] for contribution in subset if contribution['recipient'] != recipient])
    c = c.most_common(count)
    net.add_nodes([key for key, value in c])
    [net.add_edge(recipient, key, title=value, value=value) for key, value in c if key != recipient]


def main():
    # dataset.refresh()
    data = dataset.load()
    net = Network()
    add_shared_recipients(net, 'Casar, Gregorio E. "Greg"', data)
    net.show("contributions.html")


if __name__ == '__main__':
    main()
