# Сервис по анализу городской топологии

## Предварительные действия

- Поместить PBF файлы исследуемых городов в директорию `/api/cities_osm/`. 
- Название файлов должны иметь вид: `{Название города с большой буквы}.osm.pbf`. Пример: `Москва.osm.pbf`.
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

  
