import torch
import torch.nn as nn

def message_passing(nodes, edges, edges_features, message_fn):
    n_nodes = nodes.shape[0]
    n_edges = edges.shape[0]
    n_embed = nodes.shape[1]

    message_inputs = nodes[edges]
    message_inputs = message_inputs.view(n_edges, 2*n_embed)
    messages = message_fn(message_inputs)

    updates = torch.zeros(n_nodes, n_embed)
    idx_j = edges[:, 1]
    updates = updates.index_add(0, idx_j, messages)
    return updates


if __name__=='__main__':
    nodes = torch.Tensor([[0.12, 0.41, 2.23], [0.11, 0.22, 0.33], [0.12, 0.33, 0.42]])
    edges = torch.Tensor([[0, 1], [1, 0], [2, 1], [1, 2]]).long()
    print(edges.shape)
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.fc1 = nn.Linear(6,3)
        def forward(self, x):
            x = self.fc1(x)
            return x
    message_passing(nodes, edges, None, Net())





