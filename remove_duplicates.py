import codecs
from more_itertools import unique_everseen
import pandas as pd

# Avoid any duplication
# Trim empty rows
def no_duplication():
    try:
        with codecs.open(r"LinkedIn.csv", 'r', encoding='utf-8') as file, open(r"LinkedIn_x.csv", 'w',
                                                                               encoding='utf-8') as _remove:
            _remove.writelines(unique_everseen(file))

        df = pd.read_csv('LinkedIn_x.csv', encoding='utf-8')
        df.to_csv('LinkedIn_xx.csv', index=False, encoding='utf-8')
    except Exception:
        pass
