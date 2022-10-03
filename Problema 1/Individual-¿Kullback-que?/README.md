# ¿Kullback que?

Tags: Individual, Problema

Cuando trabajamos con modelos que representan una distribución de probabilidad nuestro objetivo es hacer que la distribución de los datos se acerque lo más posible a las probabilidades que nos da el modelo sobre esos datos. Existen muchas maneras de calcular esa diferencia, una común es usar funciones de divergencia, entre ellas la divergencia de Kullback-Leibler es la más usada. Dadas dos distribuciones de probabilidad 𝑃 y 𝑄 se define asumiendo que sean distribuciones discretas como:

$$
KL(P|Q)=\sum_{i=1}^{N}P(i)\cdot \log(\frac{P(i)}{Q(i)}) 
$$

![Untitled](images/Untitled.png)

![Untitled](images/Untitled%201.png)

En el caso de distribuciones continuas, simplemente substituimos el sumatorio por una integral.

> Siendo *𝑋* una muestra de datos $x_1, ..., x_n$ **de valores discretos, donde podemos estimar su distribución $P$ a partir de su frecuencia y $Q$ **es una distribución de probabilidad sobre el mismo rango de valores discretos. Demuestra que optimizar $KL(P|Q)$ es equivalente a optimizar la log verosimilitud negativa de $Q$ **sobre los datos.
> 

<aside>
💡 Existe una relación entre $P(i)$, la frequencia, y $Q(i)$, la distribucion de probabilidad. 
$\forall i \; : \; i \in P \rightarrow (i \in Q \; \wedge \; Q(i)=\frac{P(i)}{N})$

</aside>

Empezaremos optimizando la $\texttt{Log Verosimilitud Negativa de Q}.$

$$
\begin{matrix*}[l]
L(\theta)&=&-\log(\prod_{i=1}^{N}Q(i)) \\ 
&=&-\log(\prod_{i=1}^{N}\frac{P(i)}{N}) \\ 
&=& -\sum_{i=1}^{N}\log(\frac{P(i)}{N}) \\
&=& -\sum_{i=1}^{N}(\log(P(i))-\log(N)) \\
&=& -\sum_{i=1}^{N}(\log(P(i))) - \sum_{i=1}^{N}(\log(N)) \\
&=& -\sum_{i=1}^{N}(\log(P(i))) - (N \cdot\log(N)) \\
&=& \sum_{i=1}^{N}(-\log(P(i))) - (N \cdot\log(N)) \\
&=& \sum_{i=1}^{N}(\log(\frac{1}{P(i)})) - (N \cdot\log(N)) \\ \\ \\

\frac{\partial }{\partial P}&=&\sum_{i=1}^{N}(\log(\frac{1}{\frac{1}{P(i)}})) \\
&=&\sum_{i=1}^{N}(P(i))
\\ \\
\frac{\partial }{\partial P}&=&0 \\ 
0&=&\sum_{i=1}^{N}(P(i))

\end{matrix*}

$$

Ahora, seguiremos optimizando la función $KL(P|Q)$

$$
\begin{matrix*}[l]
KL(P|Q)&=&\sum_{i=1}^{N}(P(i)\cdot\log(\frac{P(i)}{Q(i)})) \\
&=&\sum_{i=1}^{N}(P(i)\cdot(\log(P(i))-\log(Q(i)))) \\
&=&\sum_{i=1}^{N}(P(i)\cdot(\log(P(i))-\log(\frac{P(i)}{N}))) \\
&=&\sum_{i=1}^{N}(P(i)\cdot(\log(P(i))-(\log(P(i))-\log(N))))) \\
&=&\sum_{i=1}^{N}(P(i)\cdot(\log(P(i))-\log(P(i))+\log(N)))) \\
&=&\sum_{i=1}^{N}(P(i)\cdot(1+log(N))) \\
&=&N\cdot(1+log(N))\cdot\sum_{i=1}^{N}P(i) \\
&=&(N+N\cdot \log(N)) \cdot\sum_{i=1}^{N}P(i) \\

\\

\frac{\partial }{\partial P}&=&(N+N\cdot \log(N)) \cdot\sum_{i=1}^{N}P(i) \\ \\

\frac{\partial }{\partial P}&=&0 \\
0&=&(N+N\cdot \log(N)) \cdot\sum_{i=1}^{N}P(i)

\end{matrix*}
$$

Se puede ver como en ambas optimizaciones encontramos un mismo punto de inflexion, en ambos casos es $\sum_{i=1}^{N}P(i)$

---

> Todo modelo de clasificación es una distribución de probabilidad sobre un conjunto de valores
discretos, por lo que podemos ajustar un modelo probabilístico para clasificación haciendo que
las probabilidades que obtenga para una muestra se ajusten a las de los datos. Usa la función make_classification de scikit-learn para crear un conjunto de datos de clasificación de dos dimensiones y 100 ejemplos. Tendrás dar un valor 0 al parámetro n_redundant y un valor 1 al parámetro n_clusters_per_class. Da un valor también al parámetro random_state para que los experimentos sean reproducibles. El problema que generará será de clasificación binaria.
>
