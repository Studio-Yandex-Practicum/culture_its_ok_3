WELCOME_MESSAGE = '''
Добрый день! Вас приветствует
официальный бот арт-медиатор проекта
"Ничего страшного"
'''

START_MESSAGE = '''
Перед Вами карта фестиваля. Фестиваль

в этом году объединяет 100 работ. Мы разработали
3 маршрута для арт-медитации. Выберите маршрут.

Описание маршрутов можно найти в bio к боту.
'''

START_WAY_TEXT = '''
Во время нашего маршрута мы не только
посмотрим более 12 работ, выполненных
художниками из разных городов России за время
фестиваля «Ничего страшного» в 2022, но и
будем фиксировать ощущения от облика города,
замечать особенности, рассуждать о
руинизированных пространствах и городе, как
живой, постоянно меняющейся системе.
Вот схема нашего маршрута!
'''

START_WAY_QUESTION = '''
Вы стоите в месте начала маршрута?
'''

START_MEDITATION = '''
Отлично, тогда начнём нашу медиацию!
'''
NAME_OF_PLACE = {
    1: (
        'Название работы: без названия, автор: Алексей Кассета',
        'Название работы: «Эпоха разоренной красоты», автор: Иван Симонов',
        'Название работы: «Спутник», автор: Иван Симонов',
        'Название работы: «Подорожник», автор: Couple of creators',
        'Название работы: «Тигр», автор: Антон Сакво ',
        'Название работы: «Хоровод», автор: ХочуБытьСоковым',
        'Название работы: без названия, автор: без автора',
        'Название работы: без названия, автор: Тэг команды AC',
    ),
    2: (
        'Название работы: без названия, автор: без автора',
        'Название работы: без названия, автор: без автора',
        'Название работы: без названия, автор: без автора',
    ),
    3: (
        'Название работы: без названия, автор: без автора',
        'Название работы: без названия, автор: без автора',
        'Название работы: без названия, автор: без автора',
    ),
}

ADDRESSES = {
    1: (
        'Адрес: Художественная галерея «Ростов», пер. Соборный, 22',
        'Адрес: ул. Социалистическая, 99',
        'Адрес: ул. Социалистическая, 100',
        'Адрес: ул. Социалистическая, 100',
        'Адрес: ул. Шаумяна, 108',
        'Адрес: ул. Шаумяна, 108',
        'Адрес: ул. Шаумяна, 108',
        'Адрес: ул. Шаумяна, 108',
    ),
    2: (
        'Адрес: ...',
        'Адрес: ...',
        'Адрес: ...',
    ),
    3: (
        'Адрес: ...',
        'Адрес: ...',
        'Адрес: ...',
    ),
}

HOW_TO_PASS = {
    1: ('''
        Как пройти:
        Войти в бизнес-центр «Соборный 22»,
        подняться на второй этаж. Код для входа: 1357#
        ''',
        '''
        Как пройти:
        Остановитесь рядом с домом номер 86 на ул. Социалистической,
        посмотрите на небольшой дом напротив. Найдите белеющих «холст»
        с работой в виде ворот в правой части здания. Можете перейти
        дорогу и приглядеться к надписи над трафаретными воротами,
        созданной художником.
        ''',
        '''
        Как пройти:
        Дойти до парковки между домами 100 и 102 на ул. Социалистическая.
        Зайти внутрь парковки и обратить внимание на черно-белую фотографию
        на стене, она расположена на высоте 4-5 метров!
        ''',
        '''
        Как пройти:
        На этой же парковке, предлагаем обратить внимание на правую стену
        с пёстрыми цветами и надписью «жизнь всегда происходит сейчас»!
        ''',
        '''
        Как пройти:
        От парковки предлагаем пройти сквозь руины в сторону улицы Шаумяна.
        Обратите внимание на правую стену,
        на которой в том числе разлёгся огромный тигр!
        ''',
        '''
        Как пройти:
        На этой же стене осталось множество элементов-осколоков здания,
        некогда находившегося здесь. Найдите кафель с розовыми фигурами!
        ''',
        '''
        Как пройти:
        Руинизированная площадь активно обрастает тэгами и кусками
        вне деятельности фестиваля. Посмотрите на левую стену
        с россыпью работ от уличных художников.
        ''',
        '''
        Как пройти:
        Вновь посмотрите на правую сторону площадки,
        особенно на две крупных, словно стекающих сиренево-розовые буквы AC.
        ''',
        ),
    2: ('''
        Как пройти: ...
        ''',
        '''
        Как пройти: ...
        ''',
        '''
        Как пройти: ...
        ''',
        ),
    3: ('''
        Как пройти: ...
        ''',
        '''
        Как пройти: ...
        ''',
        '''
        Как пройти: ...
        ''',
        ),
}

TEXT_PLACE_1 = {
    1: ('''
        Алексей Кассета совмещает несколько визуальных эстетик,
        оформив вход в галерею «Ростов».
        С одной стороны, Вы видите обилие ярких геометрических элементов.
        С другой, узнаются вполне реалистичные объекты,
        выполненные в черно-белой гамме: хуторской домик,
        цветок в горшке, автомобиль.
        Слева внизу Вы можете обнаружить тэг Алексея Кассеты — BASF
        и год создания работы 22.
        ''',
        '''
        Перед Вами работа Ивана Симонова "Эпоха разорённой красоты",
        символически расположившаяся на фасаде одноэтажного ветхого
        здания летом 2022 во время фестиваля "Ничего страшного".
        Возможно, именно на этом месте могли бы быть настоящие кованные ворота.
        Иван Симонов так прокомментировал процесс создания работы:
        "Ростов-на-Дону известен своими домами в стиле модерн. Решётки,
        барельефы, печи погибают без реставрации в пожарах или
        в результате "ошибки экскаваторщика".
        За время своего пребывания в Ростове я лично стал свидетелемметаморфоз.
        Лёгкость и скорость, с которой эти дома уничтожаются,
        произвела на меня глубокое впечатление.
        Меньше чем за сутки ковш экскаватора разрушил здание.
        Пыль и обломки - вот всё, что от него осталось.
        Этот дом уже никто не увидит из вновь приехавших туристов.
        Город теряет свой исконный облик, индивидуальность и
        историческую привлекательность. Им на смену приходят
        безликие многоэтажные однотипные дома из стекла и бетона
        или пустыри для парковки».
        ''',
        '''
        Предлагаем ознакомиться Вам с историей создания работы «Спутник»,
        рассказанной самим художником, Иваном Симоновым: "Эти герои появились
        у меня в 2017 году, когда я посетил Зеленоградск.
        Был невероятной силы шторм, меня сносило ветром, а человек вдоль
        моря выгуливал собаку. Они были спокойны, как будто шторм и ураганный
        ветер это обыденность. Меня сильно заинтересовал этот образ,
        он отлично иллюстрирует взаимоотношения человека и животного,
        их привязанность и преданность друг другу. Они идут вместе не
        смотря ни на что. В работе сохранена игра масштабов и является
        продолжением серии #маленькиелюди. За счёт огромного размера стены
        персонажи теряются на фоне здания, несмотря на то, что выполнены в
        размере реального человеческого роста".
        ''',
        '''
        Художники Couple of creators намеренно создают яркие работы
        с четко читаемым текстом. Это немного иное направление в отличие
        от искривлённых тэгов, которые мы находили на улицах ранее.
        Работа с написанием букв получает название райтинг в уличной среде.
        Ваня Make, один из художников тандема Couple of creators, занимается
        придумыванием способов написания букв, то есть леттерингом. Юлия JK,
        вторая половна тандема - отвечает за яркость и объёмность цветов.
        Художники выбрали именно такую формулировку, чтобы привлечь внимание
        прохожих к сиюминутности жизни и важности каждого прожитого момента.
        ''',
        '''
        Этого милого тигра сделал московский художник Антон Сакво.
        В работах Антона часто присутствует ирония. Что может быть ироничнее
        тигра, развалившегося вдоль обрушившегося фасада?
        ''',
        '''
        Эти абстракции на кафеле сделал анонимный творческий коллектив
        из Челябинска – ХочуБытьСоковым. Работа получила название "Хоровод".
        Сложно придумать что-то более непоколебимое,
        чем железные спортивные снаряды с советских детских площадок.
        Они пережили взросление каждого ребенка и страны в целом,
        сохраняя память дворового уюта до сих пор. Исходной точкой для
        работы "Хоровод" стал один из таких снарядов, найденный во дворах
        Ростова-на-Дону. Приумноженный, он превратился в орнамент-оберег,
        перенося свою неприкосновенность на стенку дома, устоявшего от сноса.
        ''',
        '''
        Это очень частый персонаж, то есть керек (от англ. character),
        авторства ростовского граффитчка. Зовут персонажа Хорошогр и создан он,
        чтобы поднимать настроение всем вокруг, даже своим именем говоря:
        "всё будет хорошогр!"
        ''',
        '''
        AC (Active Crew – их аббревиатуру очень часто можно увидеть в Ростове).
        Команда настолько активна, что невозможно не столкнуться
        с их тэгам на улицах города. Также расшифровать аббревиатуру
        их можно вспомнив одно из сленговых выражений уличной среды
        All City (пер. весь город). То есть граффитчик настолько крут
        и известен своими тэгами именно потому что оставил их буквально
        по всему городу!
        В данном случае команда изобразила свой тэг нарочито огромным,
        а градиентный плавный переход цветов считается отдельным уровнем
        мастерства и носит названия faded.
        ''',
        ),
    2: ('''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        '''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        '''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        ),
    3: ('''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        '''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        '''
        Для начала, предлагаю ознакомиться с проектом,
        создававшимся с 1972 по 1983. Речь идёт об одной
        из визитных карточек Ростова-на-Дону – мозаиках
        в подземных переходах.
        ''',
        ),
}

QUESTION_ABOUT_EXHIBIT = '''
О чем Вы думаете, глядя на эту работу?
'''

STOP_JOURNY = '''
Как жаль, что вы  решили закончить,
надеемся другой маршрут вам понравится больше.
'''

NOT_START_PLACE = '''
Медитация начинается по адресу _адрес_. Чтобы
пройти к началу маршрута, предлагаю
воспользоваться Яндекс.картами .
'''

ABOUT = '''
Описание проекта "Ничего страшного".
'''

WHAT_I_CAN_DO = '''
Описание функций бота.
'''

END_OF_WAY = '''
Поздравляем! Вы завершили маршрут.
'''

END_WAY_MESSAGE = '''
Команда фестиваля «Ничего страшного» будет
рада вашему отклику! Для этого мы прикрепляем
здесь небольшую форму, заполнение которой займёт
не больше минуты:)/
'''
