from __future__ import print_function
import torch

x = torch.ones(5, 3, dtype=torch.long)

y = torch.ones(5, 3, dtype=torch.long)

a = torch.LongTensor([i for i in range(0,20)])

print(a)


#result = torch.empty(5,3, dtype=torch.long)

#torch.add(x, y, out=result)
#print(result)

c = a.view(2, 10)

print(c)

c = c.view(-1, 5, 2)

print(c)