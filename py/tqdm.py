import tqdm
a=[i for i in range(1000000)]
for i in tqdm.tqdm(a):
    pass

from tqdm import tqdm,trange

for i in tqdm(a):
    pass
for i in trange(1000000000):
    pass
