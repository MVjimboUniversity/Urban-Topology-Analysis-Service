# Сервис по анализу городской топологии

## Предварительные действия

- Поместить PBF файлы исследуемых городов в директорию `/api/cities_osm/`. 
- Название файлов должны иметь вид: `{Название города с большой буквы}.pbf`. Пример: `Москва.pbf`.
- Для скачивания готовых фалов можно воспользоваться https://extract.bbbike.org/.

## Запуск
 
Для запуска серверной части приложения необходимо выполнить из основной директории проекта команду:

    docker compose up --build
    
## Примечания
 
После выполнения команды, по окончании сборки контейнера, доступ к сайту и серверу базы данных можно получить по следующим ссылкам:
- Сайт: http://localhost:4200/
- Сервер базы данных: http://localhost:8002/docs/

## Выключение сервера

Для того, чтобы корректно завершить работу сервера в консоле выполните команду:
    
     docker compose down

# Анализ графов

В каталоге `/analytics` лежат ноутбуки, которые используются для поиска степнного закона (degrees.ipynb), для вычисления мер центральности (centrality.ipynb) и betweenness'а. 

Для работы с данными ноутбуками требуется библиотека *grpah-tool*. На момент написания README самый удобный способ ее использования - контейнеры. В каталоге также лежит Dockerfile для того, чтобы данный контейнер можно было поднять.
  
На вход ноутбуки принимают JSON-файл, которые возвращают в качестве ответа методы `/api/city/graph/region/` и `/api/city/graph/bbox/`.
