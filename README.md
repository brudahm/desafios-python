# Desafios em Python
3 desafios desenvolvidos em linguagem Python e seus respectivos testes com framework de testes unitários.

### Sobre

Nesse repositório contém 3 pastas nomeadas Problema 1 (Conversão das horas), Problema 2 (Diferença das diagonais) e Problema 3 (Pares divisíveis). Dentro de cada uma delas contém 2 arquivos sendo 1 deles "nomedoproblema.py" a resolução do respectivo desafio, e o outro arquivo "nomedoproblema_test.py" o seu teste unitário.    
Abaixo estão os enunciados dos desafios.  

### Problema 1

Dado um horário no formato AM/PM, converta-o para o formato 24 horas.  
<b>OBS:</b>  
12:00:00AM em um relógio de 12 horas é 00:00:00    
12:00:00PM em um relógio de 12 horas é 12:00:00    
<b>Descrição:</b>  
Crie uma função para a conversão do tempo. Ela deve retornar uma nova string
representando a hora de entrada no formato de 24 horas.  
<b>Entrada:</b>  
Uma única string que representa uma hora no formato de 12 horas (ou seja:
hh:mm:ssAM ou hh:mm:ssPM).  
<b>Retorno:</b>  
Uma string que representa a hora no formato 24 horas.  

### Problema 2

Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas
diagonais.  
Por exemplo, a matriz quadrada abaixo:  
1 2 3  
4 5 6  
9 8 9  
A diagonal que vem da esquerda para direita = 1 + 5 + 9 = 15. A diagonal que vem
da direita para esquerda = 3 + 5 + 9 = 17. E sua diferença absoluta é |15 - 17| = 2  
<b>Descrição:</b>    
Crie uma função para calcular a diferença absoluta das diagonais.  
<b>Entrada:</b> Uma matriz quadrada de números inteiros.  
<b>Saída:</b> A diferença absoluta entre as somas das duas diagonais da matriz como um
único inteiro.  

### Problema 3

Você recebe uma lista de n inteiros, ar = [ar[0], ar[1], ..., ar[n-1]] ,e um inteiro positivo, k.  
Encontre e imprima o número de pares (i,j) onde i < j e ar[i] + ar[j] é divisível por k.  
Por exemplo, ar=[1, 2, 3, 4, 5, 6] e k=5. Nossos três pares que atendem aos critérios são
[1,4], [2,3] e [4,6].  
<b>Descrição:</b>  
Crie uma função que deve retornar a contagem inteira de pares que atendem aos critérios.
<b>Entrada:</b>  
ar: uma lista de inteiros positivos  
k : o inteiro positivo para dividir a soma do par  
<b>Ex:</b>  
ar = [1, 3 , 2, 6, 1, 2]  
k = 3  
<b>Saída:</b> Imprimir o número de pares (i,j) onde i < j e a[i] + a[j] e é divisível por k.  
Ex: 5  
<b>Exemplo:</b>  
Entradas:  
ar = [1, 3 , 2, 6, 1, 2]  
k = 3  
Saída: 5  
<b>Explicação:</b>  
(0, 2) => ar[0] + ar[2] = 1 + 2 = 3  
(0, 5) => ar [0] + ar [5] = 1 + 2 = 3  
(1, 3) => ar[1] + ar[3] = 3 + 6 = 9  
(2, 4) => ar[2] + ar[4] = 2 + 1 = 3  
(4, 5) => ar[4] + ar[5] = 1 + 2 = 3  

