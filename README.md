Практическая работа 1
Цель работы. Работа направлена на прорешивание простых базовых задач с помощью библиотек pygame и numpy.
Только последняя 11-я задача является более объямной и предполагает элементы ООП.

1. Напишите программу, которая позволяет ввести координаты точки и применить к ним матричное преобразование с матрицей:  
```
T =  ⎡ 1  3 ⎤  
     ⎣ 4  1 ⎦  
```
Выведите на экран начальные и полученные координаты. Прорисуйте исходную и новую точки в окне с использованием pygame.  

![image](https://github.com/user-attachments/assets/a8296e5c-5352-45cc-a214-83d7450403cc)  

![image](https://github.com/user-attachments/assets/6d9c58e1-fe14-4b57-886a-2480303ec738)  


2. Нарисуйте графические примитивы (pygame) — окружность, линии, текст — различными цветами в окне программы.

![image](https://github.com/user-attachments/assets/e4a9ee55-0777-42d0-8e2a-a39b68a35780)  

3. Напишите программу, которая преобразует отрезок, заданный двумя точками. Запишите координаты в матрицу
отрезка и примените к ней матричное преобразование:
```
T =  ⎡ 1  3 ⎤  
     ⎣ 4  1 ⎦  
```
Отобразите исходный и преобразованный отрезок разными цветами.  
 
![image](https://github.com/user-attachments/assets/1b58d1ab-d3d2-4528-8fa3-99f13c311325)  
![image](https://github.com/user-attachments/assets/d179e8cf-bfbb-4fd0-a12e-852370fd1874)  



4. Напишите программу для преобразования координат конца отрезка

```
𝐿 =  ⎡  0  100 ⎤  
     ⎣ 200 300 ⎦  
```
по матрице:
```
T =  ⎡ 1  2 ⎤  
     ⎣ 3  1 ⎦  
```

Найдите середину исходного и преобразованного отрезка и визуализируйте оба отрезка с помощью pygame. Обозначьте середины отрезков небольшими кругами и соедините их ещё одним отрезком.

![image](https://github.com/user-attachments/assets/13bacf18-ba50-4140-b21a-01f739451074)  
![image](https://github.com/user-attachments/assets/4908fd52-1042-4733-995e-adcf4efabefe)  


5. Преобразуйте два параллельных отрезка, заданных матрицей
```
𝐿 =  ⎡ 50  100 ⎤
     ⎜250 200 ⎜
     ⎜ 50 200 ⎜
     ⎣ 250 300 ⎦  ,
```
с помощью той же матрицы 𝑇, что и в предыдущей задаче. Рассчитайте и отобразите их начальный и конечный наклоны.

![image](https://github.com/user-attachments/assets/3e505a28-6629-44d4-9c40-689d65756aa2)  
![image](https://github.com/user-attachments/assets/7c768055-857e-41a6-bc02-7220ff7422cf)  


6. Напишите программу для преобразования пересекающихся отрезков
```
𝐿 =  ⎡ −1/2  3/2 ⎤
     ⎜  3   −2  ⎜
     ⎜ −1   −1  ⎜
     ⎣  3   5/3  ⎦
```
по матрице:
```
T =  ⎡ 1  2 ⎤  
     ⎣ 1 -3 ⎦  
```

Искусственно сместите все получившиеся отрезки в видимую область игрового окна для наглядности (сохраняйте оригинальную матрицу координат в изначальной матрице 𝐿 !). Перед преобразованиями умножьте искусственно
матрицу отрезка 𝐿 на 100, чтобы он и его преобразованная версия имели видимую длину в пикселях.

![image](https://github.com/user-attachments/assets/dd9198a5-50db-40f3-b8ac-d96afca38e18)
![image](https://github.com/user-attachments/assets/5b267755-9fc4-4b07-9ef8-78afe3d25809)


7. Вращайте треугольник
```
𝐿 =  ⎡  3   -1 ⎤
     ⎜ 4   1   ⎜
     ⎣  2   1  ⎦
```

на 90 градусов (𝜋/2) против часовой стрелки с помощью матрицы:
```
T =  ⎡  0  1 ⎤  
     ⎣ -1  0 ⎦  
```

Перед преобразованиями умножьте искусственно матрицу отрезка 𝐿 на 100, чтобы он и его преобразованная версия
имели видимую длину в пикселях. Как и в предыдущей задаче, смещайте оригинальный треугольник, чтобы он был
виден на экране (сохраняйте оригинальную матрицу координат в изначальной матрице 𝐿 !), после преобразования
матрицы 𝐿 сместите на такое же количество пикселей в видимую область окна новый треугольник 𝐿.

![image](https://github.com/user-attachments/assets/c94c4e4a-98bc-4751-ac54-08e389b7677e)  


8. Отразите треугольник

```
𝐿 =  ⎡  8   1  ⎤
     ⎜ 7   3  ⎜
     ⎣  6   2  ⎦
```
относительно линии 𝑦 = 𝑥 с помощью матрицы:
```
T =  ⎡  0  1 ⎤  
     ⎣  1  0 ⎦  
```
Также прибегайте к смещениям в пикселях, к умножению на 100 и тому подобным приёмам, как и в предыдущей
задаче, чтобы треугольники были видны.

![image](https://github.com/user-attachments/assets/8c5dafe1-da67-47b1-8b20-0f73115d6b22)  


9. Масштабируйте (с надлежащим изменением координат в пикселях, чтобы всё было видно) треугольник

```
𝐿 =  ⎡  5   1  ⎤
     ⎜ 5   2  ⎜
     ⎣  3   2  ⎦
```
с помощью матрицы:
```
T =  ⎡  2  0 ⎤  
     ⎣  0  2 ⎦  
```

![image](https://github.com/user-attachments/assets/6dc989ab-f89f-4d09-86f6-bbf3c739517c) 


10. Нарисуйте на экране спираль в виде улитки Паскаля, используя полярные координаты:  
𝑟 = 𝑏 + 2 ⋅ 𝑎 ⋅ cos(𝜃)  
𝑥 = 𝑟 ⋅ cos(𝜃), 𝑦 = 𝑟 ⋅ sin(𝜃)

![image](https://github.com/user-attachments/assets/17cd27a9-e10d-4172-8ca7-0ac76375b711)


12. Постройте квадрат, масштабируйте его с коэффициентом 𝑚 = 0.9 и поворачивайте на угол 𝛼 = 𝜋/32. Начальные координаты квадрата:

```
X =  ⎡  2  -2 ⎤
     ⎜ -2 -2  ⎜
     ⎜ -2  2  ⎜   × 100
     ⎣  2   2 ⎦  
```

Используйте комбинированное преобразование и выполните 20 таких операций с отрисовкой в pygame.  

![image](https://github.com/user-attachments/assets/e3d22a71-8774-41a7-95c2-515cb412b8f8)

