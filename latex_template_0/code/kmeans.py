from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
with open("./geo_diff.csv") as f:
    data = f.readlines()
data = data[2:]
trainMat = []
for line in data:
    trainMat.append([float(item.strip("\n")) for item in line.split(",")])
estimator = KMeans(n_clusters=4)
estimator.fit(trainMat)
centroids = estimator.cluster_centers_
plt.plot([item[0] for item in trainMat], \
    [item[1] for item in trainMat], 'o', label='user')
plt.plot([item[0] for item in centroids], \
    [item[1] for item in centroids], 'o', label='centroids')
plt.legend(loc=2)
plt.show()
