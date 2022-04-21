# _APIproject - тестовый проект_
____

## _Описание_

API проект с возможностью добавления статей и их последующего комментирования.

## _Инструкция по установке_
1.Склонируйте репозиторий в необходимую Вам директорию:
```
https://github.com/Gorstka/APIproject
```
2.В предустановленном виртуальном окружении в директории проекта /apiproject установите зависимости:
```
pip install -r requirements.txt
```
3.В директории /infra выполните команды для запуска сервера 
```
docker-compose up (построение контейнеров и запуск)
docker-compose exec web python manage.py migrate (выполние миграций)
```
4.При необходимости протестировать проект запросами при помощи Postman либо др. сервисов.

## _Технологии_

- Python
- Django
- Django Rest Framework
- Docker
- PostgreSQL

### _Автор_
Горстка Сергей, github.com/Gorstka, gorstkasergei@gmail.com
