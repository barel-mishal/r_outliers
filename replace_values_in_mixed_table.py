import numpy as np
import pandas as pd

def create_table(n_fetuers=10, ids=4, n_reapte_ids=4):
  rows = ids * n_reapte_ids
  ids = np.tile([id_ for id_ in range(1, n_reapte_ids+1)], n_reapte_ids)
  values = np.random.randint(1, 1000, size=(rows, n_fetuers))
  fetuers = [f'feature_{n}' for n in range(n_fetuers)]
  data = pd.DataFrame(values, columns=fetuers)
  ids_series = pd.Series(ids, name="IDs")
  return pd.concat([ids_series, data], axis=1)



print(create_table())


