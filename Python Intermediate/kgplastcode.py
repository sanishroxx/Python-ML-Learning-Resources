import pandas as pd

ec = pd.read_csv('Ecommerce Customers.csv')

ec.info()

# after executing get the output

ec.isnull()






#next

import pandas as pd
import seaborn as sns

ec = pd.read_csv('Ecommerce Customers.csv')


sns.heatmap(ec.isnull(),camp='virids',
            yticklabels=False)

ec.columns

