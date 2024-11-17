# Guía Completa de Ejemplos de Notaciones y Símbolos TeX en Markdown

## 1. Letras Griegas

### Minúsculas:

$\alpha$, $\beta$, $\gamma$, $\delta$, $\epsilon$, $\zeta$, $\eta$, $\theta$, $\iota$, $\kappa$, $\lambda$, $\mu$, $\nu$, $\xi$, $\omicron$, $\pi$, $\rho$, $\sigma$, $\tau$, $\upsilon$, $\phi$, $\chi$, $\psi$, $\omega$.

### Mayúsculas:

$\Alpha$, $\Beta$, $\Gamma$, $\Delta$, $\Epsilon$, $\Zeta$, $\Eta$, $\Theta$, $\Iota$, $\Kappa$, $\Lambda$, $\Mu$, $\Nu$, $\Xi$, $\Omicron$, $\Pi$, $\Rho$, $\Sigma$, $\Tau$, $\Upsilon$, $\Phi$, $\Chi$, $\Psi$, $\Omega$.

## 2. Operadores Matemáticos
### Suma: $a + b$
### Resta: $a - b$
### Multiplicación: $a \cdot b$, $ab$
### División: $a \div b$, $\frac{a}{b}$
### Igualdad: $a = b$
### Desigualdad: $a \neq b$
### Menor que: $a < b$
### Mayor que: $a > b$
### Menor o igual: $a \leq b$
### Mayor o igual: $a \geq b$

## 3. Funciones Matemáticas

### Seno: $\sin(x)$
### Coseno: $\cos(x)$
### Tangente: $\tan(x)$
### Logaritmo natural: $\ln(x)$
### Logaritmo en base $b$: $\log_b(x)$
### Exponencial: $\exp(x)$

## 4. Ecuaciones

### Ecuación cuadrática:
  $$
  ax^2 + bx + c = 0
  $$

### Solución:
  $$
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
  $$

### Teorema de Pitágoras:
  $$
  a^2 + b^2 = c^2
  $$

## 5. Fracciones y Raíces

### Fracción: $\frac{1}{2}$
### Raíz cuadrada: $\sqrt{4} = 2$
### Raíz de orden $n$: $\sqrt[n]{x}$

## 6. Sumas, Productos e Integrales

### Sumatoria:
  $$
  \sum_{i=1}^{n} i = \frac{n(n+1)}{2}
  $$
  
### Producto:
  $$
  \prod_{i=1}^{n} i
  $$

### Integral:
  $$
  \int_{a}^{b} f(x) \, dx
  $$

## 7. Límites y Derivadas

### Límite:
  $$
  \lim_{x \to a} f(x)
  $$

### Derivada: 
  $$
  \frac{dy}{dx}
  $$

## 8. Matrices y Vectores

### Matriz:
  $$
  \begin{bmatrix}
  a_{11} & a_{12} \\
  a_{21} & a_{22}
  \end{bmatrix}
  $$

### Vector: 
  $$
  \vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}
  $$

## 9. Conjuntos y Operaciones

### Números naturales: $\mathbb{N}$
### Números enteros: $\mathbb{Z}$
### Números racionales: $\mathbb{Q}$
### Números reales: $\mathbb{R}$
### Números complejos: $\mathbb{C}$
### Unión: $A \cup B$
### Intersección: $A \cap B$
### Diferencia: $A \setminus B$

## 10. Notaciones Especiales

### Teorema de Pitágoras: $a^2 + b^2 = c^2$
### Notación de cardinalidad: $|A|$ denota el número de elementos en el conjunto $A$.

## 11. Símbolos Especiales

### Infinito: $\infty$
### Aproximadamente: $\approx$
### Porcentaje: $\%$
### Para todo: $\forall$
### Existe: $\exists$
### No existe: $\nexists$

## 12. Ejemplos Completos en Bloque

### Ecuación en bloque:
$$
E = mc^2
$$

### Derivadas en bloque:
$$
\frac{d}{dx}\left(e^x\right) = e^x
$$

### Integral definida:
$$
\int_{0}^{1} x^2 \, dx = \frac{1}{3}
$$

## 13. Notación de Series y Sucesiones

### Serie geométrica:
  $$
  S = a + ar + ar^2 + ar^3 + \ldots + ar^{n-1} = \frac{a(1 - r^n)}{1 - r} \quad (r \neq 1)
  $$

### Sucesión de Fibonacci:
  $$
  F_n = F_{n-1} + F_{n-2} \quad \text{con } F_0 = 0, F_1 = 1
  $$

## 14. Notación de Combinatoria

### Combinaciones:
  $$
  \binom{n}{r} = \frac{n!}{r!(n - r)!}
  $$

### Permutaciones:
  $$
  P(n, r) = \frac{n!}{(n - r)!}
  $$

## 15. Notación de Teoría de Números

### División entera:
  $$
  a = bq + r \quad (0 \leq r < b)
  $$

### Módulo:
  $$
  a \equiv b \ (\text{mod} \ m)
  $$


## 16. Notación de Álgebra Lineal

### Norma de un vector:
  $$
  \| \vec{v} \| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
  $$

### Producto punto:
  $$
  \vec{u} \cdot \vec{v} = \sum_{i=1}^{n} u_i v_i
  $$

### Determinante:
  $$
  \text{det}(A) = \begin{vmatrix}
  a_{11} & a_{12} \\
  a_{21} & a_{22}
  \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}
  $$

## 17. Notación de Cálculo Diferencial e Integral

### Teorema Fundamental del Cálculo:
  $$
  \int_{a}^{b} f(x) \, dx = F(b) - F(a) \quad \text{donde } F'(x) = f(x)
  $$

### Regla de la cadena:
  $$
  \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
  $$

## 18. Notación de Análisis Complejo

### Número complejo:
  $$
  z = a + bi \quad (a, b \in \mathbb{R})
  $$

### Módulo de un número complejo:
  $$
  |z| = \sqrt{a^2 + b^2}
  $$

## 19. Símbolos de Lógica Matemática

### Y lógico: $ p \land q $
### O lógico: $ p \lor q $
### Negación: $ \neg p $
### Implicación: $ p \implies q $
### Doble implicación: $ p \iff q $

## 20. Símbolos de Probabilidad y Estadística

### Esperanza matemática:
  $$
  E[X] = \sum_{i=1}^{n} x_i P(x_i)
  $$

### Varianza:
  $$
  Var(X) = E[X^2] - (E[X])^2
  $$

### Distribución normal:
  $$
  X \sim N(\mu, \sigma^2)
  $$

## 21. Notaciones Avanzadas

### Operador de Laplace:
  $$
  \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) \, dt
  $$

### Transformada de Fourier:
  $$
  F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \, dt
  $$

## 22. Notaciones Gráficas

### Curvas paramétricas:
  $$
  x = f(t), \quad y = g(t)
  $$
  
### Ecuaciones polares:
  $$
  r = f(\theta)
  $$

## 23. Notación de Funciones Especiales

### Función Gamma:
$$
\Gamma(n) = \int_{0}^{\infty} t^{n-1} e^{-t} \, dt
$$

### Función Beta:
$$
B(x, y) = \int_{0}^{1} t^{x-1} (1-t)^{y-1} \, dt
$$

### Funciones hiperbólicas:
  $$
  \sinh(x) = \frac{e^x - e^{-x}}{2}
  $$
  
  $$
  \cosh(x) = \frac{e^x + e^{-x}}{2}
  $$

## 24. Notación de Teoría de Grafos

### Gráfico: $ G = (V, E) $
### Grado de un vértice: $\deg(v)$
### Caminos y ciclos:
Camino: $v_1, v_2, \ldots, v_n$
Ciclo: $v_1 \rightarrow v_2 \rightarrow \ldots \rightarrow v_1$

## 25. Notación de Sistemas de Ecuaciones

### Sistema de ecuaciones lineales:
$$
\begin{align*}
a_1x + b_1y &= c_1 \\
a_2x + b_2y &= c_2
\end{align*}
$$

### Matriz aumentada:
$$
\left[\begin{array}{cc|c}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2
\end{array}\right]
$$

## 26. Notación de Transformaciones y Mapas

### Transformación lineal:
$$
T(\vec{x}) = A\vec{x}
$$

### Función inyectiva:
$$
f: A \rightarrow B \quad \text{es inyectiva si } f(a_1) = f(a_2) \implies a_1 = a_2
$$

### Función sobreyectiva:
$$
f: A \rightarrow B \quad \text{es sobreyectiva si } \forall b \in B, \exists a \in A: f(a) = b
$$

## 27. Notaciones en Lógica y Conjuntos

### Conjuntos y sus operaciones:
Unión: $ A \cup B $
Intersección: $ A \cap B $
Diferencia: $ A \setminus B $
Complemento: $ A^c $

### Cuantificadores:
Para todo: $\forall x \in A, P(x)$
Existe: $\exists x \in A, P(x)$

## 28. Notaciones de Análisis Numérico

### Error absoluto:
$$
E_a = |x_{exacto} - x_{aproximado}|
$$

### Error relativo:
$$
E_r = \frac{|x_{exacto} - x_{aproximado}|}{|x_{exacto}|}
$$

## 29. Notaciones de Teoría de Juegos

### Juego normal:
$$
(S_A, S_B, u_A, u_B)
$$

### Equilibrio de Nash:
$$
(s_A^*, s_B^*) \text{ tal que } u_A(s_A^*, s_B) \geq u_A(s_A, s_B) \text{ para todo } s_A \in S_A
$$

## 30. Otros Símbolos Comunes

### Números primos:
$$
p \text{ es primo } \iff p > 1 \text{ y no tiene divisores aparte de } 1 \text{ y } p
$$

### Simbolismo de conjuntos:
$$
A \subseteq B \quad \text{si } A \text{ es un subconjunto de } B
$$

### Producto cartesiano:
$$
A \times B = \{(a, b) | a \in A, b \in B\}
$$

## 31. Notaciones en Álgebra Abstracta

### Grupo:
$(G, \cdot)$ donde $G$ es un conjunto y $\cdot$ es una operación binaria.

### Anillo:
$(R, +, \cdot)$ donde $R$ es un conjunto con operaciones de suma y multiplicación.

## 32. Notaciones de Estadística Inferencial

### Intervalo de confianza:
$$
\hat{p} \pm z_{\frac{\alpha}{2}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

### Prueba de hipótesis:
$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_a: \mu \neq \mu_0
$$

## 33. Notación de Estadística Descriptiva

### Media:
$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

### Mediana:
$$
\text{Mediana} = \begin{cases} 
x_{\frac{n}{2}} & \text{si } n \text{ es par} \\ 
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{si } n \text{ es impar} 
\end{cases}
$$

### Moda:
$$
\text{Moda} = \text{valor más frecuente}
$$

## 34. Notaciones en Topología

### Abierto y cerrado:
Conjunto abierto: $U$ es abierto si para cada $x \in U$, existe un $\epsilon > 0$ tal que $B(x, \epsilon) \subseteq U$.
Conjunto cerrado: $C$ es cerrado si contiene todos sus puntos límite.

### Interior y frontera:
Interior: $\text{int}(A)$
Frontera: $\partial A$

## 35. Notación de Programación y Algoritmos

### Complejidad temporal:
$$
O(n), \Theta(n), \Omega(n)
$$

### Recursión:
$$
T(n) = \begin{cases} 
1 & \text{si } n = 1 \\ 
T(n-1) + O(n) & \text{si } n > 1 
\end{cases}
$$

## 36. Notaciones de Cálculo Tensorial

### Tensor:
$$
T^{\mu\nu} = \frac{\partial^2 L}{\partial (\partial_\mu \phi) \partial (\partial_\nu \phi)}
$$

### Contracción de índices:
$$
T^\mu_\mu = \sum_{\mu=1}^{n} T^\mu_\mu
$$

## 37. Notaciones de Física

### Segunda Ley de Newton:
$$
F = ma
$$

### Ley de la Gravitación Universal:
$$
F = G \frac{m_1 m_2}{r^2}
$$

## 38. Notaciones de Teoría de Conjuntos Avanzada

### Cardinalidad:
$$
|A| \text{ es la cardinalidad del conjunto } A
$$

### Conjuntos infinitos:
$\aleph_0$ (número cardinal de los números naturales)

## 39. Notaciones de Análisis Funcional

### Espacios vectoriales:
$$
V \text{ es un espacio vectorial sobre un campo } K
$$

### Normas y espacios métricos:
$$
\|f\| = \int_{a}^{b} |f(x)| \, dx
$$

## 40. Notaciones en Economía

### Función de utilidad:
$$
U(x, y) = x^\alpha y^\beta
$$

### Elasticidad:
$$
E_d = \frac{\partial Q}{\partial P} \cdot \frac{P}{Q}
$$
