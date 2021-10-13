BOT_TOKEN: str = "ODQ4ODI4NDc1OTA1NDA5MDQ0.YLSTHw.3gnHtLB-B1GLN6QVZV8Hv7dv35I"
SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""

BOT_PREFIX = "*"

EMBED_COLOR = 0x4dd4d0  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  #maximum of 25

COOKIE_PATH = "/config/cookies/cookies.txt"

STARTUP_MESSAGE = "Запускаем бота..."
STARTUP_COMPLETE_MESSAGE = "Запуск завершён"

NO_GUILD_MESSAGE = 'Ошибка: Пожалуйста, присоединитесь к голосовому каналу или введите команду в чате сервера'
USER_NOT_IN_VC_MESSAGE = "Ошибка: Пожалуйста, присоединяйтесь к активному голосовому каналу, чтобы использовать команды"
WRONG_CHANNEL_MESSAGE = "Ошибка: Пожалуйста, используйте настроенный для команд канал"
NOT_CONNECTED_MESSAGE = "Ошибка: Бот не подключен ни к одному голосовому каналу"
ALREADY_CONNECTED_MESSAGE = "Ошибка: Уже подключен к голосовому каналу"
CHANNEL_NOT_FOUND_MESSAGE = "Ошибка: Не удалось найти канал "
DEFAULT_CHANNEL_JOIN_FAILED = "Ошибка: Не удалось подключиться к голосовому каналу по умолчанию"
INVALID_INVITE_MESSAGE = "Ошибка: Неверная ссылка на приглашение"

ADD_MESSAGE_1 = """```To add this bot to your own Server, click the following link:
                ```\n<https://discordapp.com/oauth2/authorize?client_id="""
ADD_MESSAGE_2 = "&scope=bot>"

INFO_HISTORY_TITLE = "Songs Played:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Uploader: "
SONGINFO_DURATION = "Duration: "
SONGINFO_SECONDS = "с"
SONGINFO_LIKES = "Понравилось: "
SONGINFO_DISLIKES = "Не понравилось: "
SONGINFO_NOW_PLAYING = "Сейчас играет"
SONGINFO_QUEUE_ADDED = "Добавлено в плейлист"
SONGINFO_SONGINFO = "Информация о песне"
SONGINFO_UNKNOWN_SITE = "Неизвестный сайт :question:"
SONGINFO_PLAYLIST_QUEUED = "Список воспроизведения в очереди :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Неизвестно"

HELP_ADDBOT_SHORT = "Добавить бота на другой сервер"
HELP_ADDBOT_LONG = "Дает вам ссылку для добавления этого бота на другой ваш сервер/Gives you the link for adding this bot to another server of yours."
HELP_CONNECT_SHORT = "Подключите бота к голосовому каналу"
HELP_CONNECT_LONG = "Подключает бота к голосовому каналу, на котором вы в данный момент находитесь"
HELP_DISCONNECT_SHORT = "Отключите бота от голосового канала"
HELP_DISCONNECT_LONG = "Отключите бота от голосового канала и остановите звук."

HELP_SETTINGS_SHORT = "Просмотр и изменение настроек бота"
HELP_SETTINGS_LONG = "Просмотр и настройка параметров бота на сервере. Использование: {}settings setting_name value".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Показать историю воспроизведения"
HELP_HISTORY_LONG = "Показывет " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " последних воспрозведееных трека."
HELP_PAUSE_SHORT = "Пауза, приостановить музыку"
HELP_PAUSE_LONG = "Приостанавливает работу аудиоплеера. Воспроизведение можно продолжить с помощью команды resume."
HELP_VOL_SHORT = "Выбрать громкость %"
HELP_VOL_LONG = "Изменяет громкость аудиоплеера. Аргумент указывает %, на которое должен быть установленj pyfxtybt."
HELP_PREV_SHORT = "Вернитесь на одну песню назад"
HELP_PREV_LONG = "Снова воспроизводит предыдущую песню."
HELP_RESUME_SHORT = "Возобновить воспроизведение"
HELP_RESUME_LONG = "Возобновляет работу аудиоплеера"
HELP_SKIP_SHORT = "Пропустить трек"
HELP_SKIP_LONG = "Пропускает воспроизводимую в данный момент песню и переходит к следующему элементу в очереди."
HELP_SONGINFO_SHORT = "Информация о текущей песне"
HELP_SONGINFO_LONG = "Показывает подробную информацию о воспроизводимой в данный момент песне и публикует ссылку на песню."
HELP_STOP_SHORT = "Остановить воспроизведение"
HELP_STOP_LONG = "Останавливает аудиоплеер и очищает очередь песен"
HELP_YT_SHORT = "Воспроизведение поддерживаемой ссылки или поиск на youtube"
HELP_YT_LONG = ("$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]")
HELP_PING_SHORT = "Pong"
HELP_PING_LONG = "Тест бота на статус ответа"
HELP_CLEAR_SHORT = "Очистить плейлист."
HELP_CLEAR_LONG = "Очищает очередь и пропускает текущую песню."
HELP_LOOP_SHORT = "Зацикливает воспроизводимую в данный момент песню, включить/ выключить."
HELP_LOOP_LONG = "Зацикливает воспроизводимую в данный момент песню и блокирует очередь. Используйте команду еще раз, чтобы отключить цикл."
HELP_QUEUE_SHORT = "Показывает песни в очереди."
HELP_QUEUE_LONG = "Показывает количество песен в очереди, до 10."
HELP_SHUFFLE_SHORT = "Перетасуйте очередь"
HELP_SHUFFLE_LONG = "Произвольная сортировка песен в текущей очереди"
HELP_CHANGECHANNEL_SHORT = "Измените канал бота"
HELP_CHANGECHANNEL_LONG = "Измените канал бота на тот, в котором вы находитесь"

ABSOLUTE_PATH = '' #do not modify