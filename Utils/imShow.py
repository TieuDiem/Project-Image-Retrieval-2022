import matplotlib.pyplot as plt
import numpy as np
__all__=[
    
    "plot_results"
]
__doc__ =="""

* Suported showing the result (querry image and result after querring)

"""

def plot_results(query, ls_path_score):
    columns = 3 ;rows =3
    plt.imshow(query/255.0)
    fig = plt.figure(figsize=(15, 15)) 

    for i, path in enumerate(sorted(ls_path_score, key=lambda x : x[1],reverse=True)[:9], 1):
        img = np.random.randint(10, size=(10,10))
        fig.add_subplot(rows, columns, i)
        plt.imshow(plt.imread(path[0]))
        score = path[1]
        plt.title(f'score: {score}')
        plt.axis("off")
    plt.show()
    
    
    
