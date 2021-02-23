import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "../dataset/student-mat.csv"

data = pd.read_csv(path, sep="\s*;\s*", header=0, engine='python')
# print(data.head())
# print("Data info")
# print(data.info())
# print(50 * "*")
# print("Statisque descriptive sur age")
# print(data["age"].describe())
# print(50 * "*")
# print("Mediane", data["age"].median())
# print(50 * "*")
# print(data.describe())
# print(50 * "*")
# print(data.median())

"""HISTAGRAM numeric values"""
# liste_mesures = data.select_dtypes(include=["int64"])
# print(liste_mesures)
# liste_mesures.hist()
# plt.savefig("secondhist.png")
# plt.show()


# list_categorie = data.select_dtypes(include=["object"])
# print(list_categorie)
# plt.figure()
# sns.countplot(data=list_categorie, x="ecole")
# plt.show()

# list_categorie = data.select_dtypes(include=["object"])
# plt.figure()
# sns.countplot(data=list_categorie, x="taillefam", hue="sexe")
# plt.show()

# list_categorie = data.select_dtypes(include=["object"])
# sns.countplot(data=list_categorie, x="taillefam", hue="sexe")
# plt.savefig("secondpairplot.png")
# plt.show()

data=data[["sexe", "Perdu", "Medu", "sortie", "Dalc", "Walc", "G1", "G2", "G3", "adbsences"]]
sns.pairplot(data, hue="sexe")
"""HEAT MAP"""
cora = data.corr()
sns.heatmap(cora, annot=True)
plt.savefig("secondheatmap.png")
plt.title("Correlation Students")
plt.show()
