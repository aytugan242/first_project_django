# Работа с проектом и приложением

## Задание

Вам дана заготовка с Django-проектом. В проект уже добавлено одно приложение — `app`.

Вам необходимо реализовать три view-функции и настроить для них правильные урлы.

- `/` — домашняя страница, содержит список доступных страниц;
- `current_time/` — показывает текущее время в любом удобном вам формате;
- `workdir/` — выводит содержимое [рабочей директории](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9_%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3).

В первую очередь обратите внимание на файл [urls.py](./first_project/urls.py). В нём задаются пути ко view-функциям, которые отвечают по соответствующим запросам.

Приложение `app` уже добавлено в проект и включено в `INSTALLED_APPS`. Обязательно убедитесь в этом, проверив файл с настройками.

`home_view` использует шаблон для генерации контента страницы. Шаблоны мы ещё не изучали, это материал дальнейших лекций. Поэтому ориентируйтесь на подсказки, часть кода уже написано, вам нужно вписать недостающее 🙂.

Вам нужно вписать свой код в следующие файлы:

- [urls.py](./first_project/urls.py)
- [views.py](./app/views.py)

В случае возникновения ошибок не забывайте использовать рекомендации по отладке вашего Django-проекта из лекции.