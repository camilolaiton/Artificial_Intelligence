
import pandas as pd 	# Libreria usada para procesamiento de data, y para leer los datos
import seaborn as sns 	# Libreria para visualizar los datos
import matplotlib.pyplot as plt 	# Libreria para visualizacion
import numpy as np 	# Libreria usada para algebra lineal
import warnings

from sklearn.model_selection import train_test_split	#Para la data
from sklearn.neural_network import MLPClassifier # Red neuronal 
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error 	#Error
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import GridSearchCV

pishing = pd.read_csv("dataset.csv")
#Informacion de los datos
pishing.info()

ax=plt.subplots(1,1,figsize=(10,8))
sns.countplot('Result',data=pishing)
plt.title("Pishing attributes data")
#plt.show()


pishing.hist(edgecolor='black', linewidth=1.2)
fig=plt.gcf()
#fig.set_size_inches(12,12)
#plt.show()

"""
pishing = pishing.drop('id',axis=1)
box_data = pishing #variable representing the data array
box_target = pishing.Result #variable representing the labels array
sns.boxplot(data = box_data,width=0.5,fliersize=5)
#sns.set(rc={'figure.figsize':(2,15)})
plt.show()
"""

X = pishing.iloc[:, 1:10]
f, ax = plt.subplots(figsize=(10, 8))
corr = X.corr()
print(corr)
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), 
          cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax, linewidths=.5)
#plt.show()

X = pishing.iloc[:, 1:-1].values	# voy desde inicio al final en filas , todos menos el ultimo
y = pishing.iloc[:, 10].values	# Todo, cantidad de caracteristicas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)	#	Consejo machine learning 80% entrenamiento 20% prueba

print(" INICIO \n", X_train, " \n\n ", X_test, " \n\n ", " \n\n ", y_train, " \n\n ", y_test)

warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")

model =  MLPClassifier(activation='relu', alpha=0.01, batch_size='auto',  early_stopping=False,        
						hidden_layer_sizes=(20,10), learning_rate='constant',    
						learning_rate_init=0.01, max_iter=2000, momentum=0.5,       
						shuffle=True, verbose=True) 

model.fit(X_train, y_train) #Training the model

#Test the model
predictions = model.predict(X_test)
print("accuracy_score: ", accuracy_score(y_test, predictions))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, predictions))

pishingclass = pishing['Result']
pishingclass_encoded, pishingclass_categories = pishingclass.factorize()
print("Encoded: ", pishingclass_encoded)
print("Categorias: ", pishingclass_categories[:10])

#X_train_R, X_test_R, y_train_R, y_test_R = train_test_split(X, pishingclass_encoded, test_size=0.20)
#model =  MLPRegressor(hidden_layer_sizes = (2,2), alpha=0.01, max_iter=1000) 
#model.fit(X_train_R, y_train_R) #Training the model

#predictions_R = model.predict(X_test_R)
#print("Error cuadratico medio sobre predicciones: ", mean_squared_error(y_test_R, predictions_R))
v = -np.arange(1, 5)
print("V ", v)
print("alpha: ", (0.01)**v)

param_grid = [
				{	
					'hidden_layer_sizes' : [(15,10), (8,5), (20,10), (5,4), (10, 20)], 
					'max_iter':[100, 500, 1000, 2000],
					'momentum':[0.5, 0.9, 0.4, 0.3],
					'alpha': [0.0001, 0.001, 0.01, 0.1],

				}
              ]

model = MLPClassifier()
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', iid=False)
grid_search.fit(X_train, y_train)

print("Mejores parametros encontrados por GRID: ", grid_search.best_params_)
print("Best: %f using %s" % (grid_search.best_score_, grid_search.best_params_))

"""
model2 = MLPRegressor()
grid_search2 = GridSearchCV(model2, param_grid, cv=5, scoring='neg_mean_squared_error', iid=False)
grid_search2.fit(X_train_R, y_train_R)


print("Mejores parametros REGRESSOR: ", grid_search2.best_params_) #Mejores parámetros encontrados para MLPRegressor
"""

ind = grid_search.best_estimator_  #
new_predictions = ind.predict(X_test) #Utilizamos los parámetros encontrados para volver 
print('accuracy_score obtenido con los parámetros encontrados por GridSearchCV:')
#print(mean_squared_error(y_test_R, new_predictions_R))	Para regresion
print(accuracy_score(y_test, new_predictions))	# Para clasificacion

print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, new_predictions))

X = np.arange(1, len(y_test)+1)
plt.figure()
plt.plot(X, y_test, 'k', label='Datos Originales')
plt.plot(X, predictions, 'r', label='Primera Aproximación')
plt.plot(X, new_predictions, 'g', label='Segunda Aproximación')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Original data Vs Predictions')
plt.legend()
plt.show()