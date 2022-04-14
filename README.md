# kemsu.backend

## 1. Установить докер и ab бенчмарк утилиту
sudo apt-get install docker
sudo apt-get install apache2-utils 

## 2. Собрать образ
docker build -t kemsu_flask:latest .

## 3. Запустить докер контейнер
sudo docker run --name kemsu_flask -d -p 8000:8000 --rm kemsu_flask:latest

## 4. Проверить логи Flask и отсутствие ошибок
sudo docker logs kemsu_flask

## 5. Провести нагрузочное тестирование и упреждение HTTP-DDOS атак
ab -n 1500 http://localhost:8000/

## 6. Открыть в браузере и убедиться в бизнес-функциональности
http://localhost:8000/
