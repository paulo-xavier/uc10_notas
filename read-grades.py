


import pandas as pd

df = pd.read_excel("base.xlsx") 

df['Average'] = df[['Grade1', 'Grade2', 'Grade3']].mean(axis=1)

df.to_excel('grade_student.xlsx', index=False)