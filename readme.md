# Git: Практика 1

1. [Скачайте](https://git-scm.com/downloads) и установите Git. При установке на
   вопросе "Choose the default editor used by Git" выберите предпочитаемый вами
   текстовый редактор (в крайнем случае — Notepad). Остальные параметры следует
   оставить без изменений.

   Если Git уже установлен, то этот шаг можно пропустить.

2. Запустите командную строку Windows (либо терминал Windows) и сконфигурируйте
   Git. Параметры нужно указать в двойных кавычках без угловых скобок. Значения
   этих параметров нужны для того, чтобы ваши коллеги понимали кто сделал
   коммиты и как с ним связаться.

   ```
   git config --global user.name "<ваше имя>"
   git config --global user.email "<ваш email>"
   ```

   Для проверки текущих настроек можно использовать команду:

   ```
   git config --global --list
   ```

3. Перейдите в каталог для размещения проекта (например **Документы** или
   **Documents**) и склонируйте репозиторий (чтобы увидеть URL репозитория в
   интерфейсе GitHub нажмите кнопку **Code**.):

   ```
   cd <путь к каталогу>
   git clone <URL репозитория>
   ```

   Просмотрите перечень файлов с помощью команды `dir` и перейдите в каталог
   репозитория (обычно называется так же как ваш репозиторий).

   ```
   cd <каталог репозитория>
   ```

4. Проверьте работу программы:

   Просмотрите перечень файлов с помощью команды `dir`, затем запустите скрипт
   `main.py`:

   ```
   py main.py
   ```

5. Внесите изменения в файл `main.py`:

   * Надпись "Example" замените на "Учебный пример"
   * Надпись "Hello, world!" замените на "Привет!"
   * Надпись "Press me" замените на "Нажми меня"

6. Проверьте состояние файлов в проекте:

   ```
   git status
   ```

7. Добавьте измененные файлы к планируемому коммиту:

   ```
   git add <имя изменнённого файла>
   ```

8. Проверьте состояние файлов в проекте:

   ```
   git status
   ```

9. Зафиксируйте изменения (выполните коммит):

   ```
   git commit -m "<Сообщение>"
   ```

10. Отправьте коммиты (зафиксированные изменения) из локального репозитория в
    центральный:

    ```
    git push
    ```

11. Обновите страницу репозитория в GitHub и проверьте что ваши изменения видны.
