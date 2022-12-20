### Тема: Прогнозирование конечных свойств новых материалов (композиционных материалов). 
Выпускная квалификационная работа по курсу "Data Science".
в образовательном центре МГТУ им. Н.Э.Баумана по теме:
"Прогнозирование конечных свойств новых материалов (композиционных материалов)"
В рамкам выпускной квалификационной работы:
1) Изучены теоретические основы и методы решения поставленной задачи.
2)	Проведен разведочный анализ предложенных данных. Нарисовать гистограммы распределения каждой из переменной, диаграммы ящика с усами, попарные графики рассеяния точек. Для каждой колонки получены среднее, медианное значение, проведён анализ и исключение выбросов, проверено наличие пропусков.
3)	Проведёна предобработка данных.
4)	Обучены ряд моделей для прогноза модуля упругости при растяжении и прочности при растяжении:
  •	Линейная регрессия;
  •	Метод случайного леса;
  •	Метод опорных векторов;
  •	Метод k-ближайших соседей;
  •	Градиентный бустинг (библиотека sklearn);
  •	Градиентный бустинг (библиотека xgboost);
  •	Autogluon
7)	Написана нейронная сеть, которая рекомендует соотношение матрица-наполнитель. 
8)	Разработано приложение с графическим интерфейсом или интерфейсом командной строки, которое будет выдавать прогноз нейронной сети.
9)	Оценена точность модели на тренировочном и тестовом датасете. 
10)	Создан репозиторий в GitHub / GitLab и размещён код исследования. Оформлен файл README.

Инструкция использования приложения:
Приложение позволяет решать задачу прогнозирования "Соотношение матрица наполнитель". Для получения прогноза необходимо

1) Установить python 10 и следующие версии библиотек
   • tensorflow 2.9.0
   • numpy 1.22.2
2) Закинуть в папку с приложением папку saved_model и файл scaler
3) запустить application.py
4) В новом открывшемся окне ввести 12 входных параметров и нажать "Спрогнозировать".
