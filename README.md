# Курсовая 8. Docker

## Критерии приемки курсовой работы

* Для разных сервисов создали отдельные контейнеры (django, postgresql, redis, celery, при необходимости список можно самостоятельно расширять).
* Всё оформили в файле docker-compose, при необходимости создали вспомогательные Dockerfiles.
* Проект готов быть размещенным на удаленном сервере:
  * его можно запустить по инструкции, приложенной в Readme-файл;
  * для запуска не требуется дополнительных настроек.
* Решение выложили на GitHub.

## Инструкция для запуска проекта

1. Клонируйте данный репозиторий к себе на локальную машину:

```bash
    git clone https://github.com/ssher250110/course_work_docker.git
```

2. В файле .env_example подставьте свои переменные окружения и переименуйте файл в .env
3. Запустите Docker
4. Введите команду в терминале(выполнение команды осуществляется из папки проекта):

```bash
docker-compose up -d --build 
```