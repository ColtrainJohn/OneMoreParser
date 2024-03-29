

driverOptions = [
    "--no-sandbox",
    "--headless",
    "--disable-dev-shm-usage",
    "--disable-extensions"
]


def checkOption(option, name):
    if option.text in checkDict[name]:
        return True
    return False


selectorHandlers = {
        "year" : "//div[@id='ext-element-7']",
        "month" : "//div[@id='ext-element-8']",
        "region" : "//div[@id='ext-element-5']",
        "table" : "//div[@id='ext-element-15']",
        "tableIndex" : "//div[@id='ext-element-14']",
        # "columns" : "",
        "declicker" : "//span[@class='x-btn-wrap x-btn-wrap-default-small x-btn-arrow x-btn-arrow-right']",
    }


url = "https://www.iminfin.ru/areas-of-analysis/health/perechen-zabolevanij?territory=45000000"

years = [str(i) for i in list(range(2015, 2023))]

months = ["Декабрь", "Ноябрь", "Октябрь", "Сентябрь", "Август", "Июль", "Июнь", "Май", "Апрель", "Март", "Февраль", "Январь"]

monthToDigit = {
    "Декабрь" : "12",
    "Ноябрь" : '11', 
    "Октябрь" : '10', 
    "Сентябрь" : '09', 
    "Август" : '08', 
    "Июль" : '07', 
    "Июнь" : '06', 
    "Май" : '05', 
    "Апрель" : '04', 
    "Март" : '03', 
    "Февраль" : '02', 
    "Январь" : '01',
}

regions = [
    'Российская Федерация', 
    'Центральный федеральный округ', 
    'Белгородская область', 
    'Брянская область', 
    'Владимирская область', 
    'Воронежская область', 
    'г. Москва', 
    'Ивановская область', 
    'Калужская область', 
    'Костромская область', 
    'Курская область', 
    'Липецкая область', 
    'Московская область', 
    'Орловская область', 
    'Рязанская область', 
    'Смоленская область', 
    'Тамбовская область', 
    'Тверская область', 
    'Тульская область', 
    'Ярославская область', 
    'Южный федеральный округ', 
    'Астраханская область', 
    'Волгоградская область', 
    'г. Севастополь', 
    'Краснодарский край', 
    'Республика Адыгея (Адыгея)', 
    'Республика Калмыкия', 
    'Республика Крым', 
    'Ростовская область', 
    'Северо-Западный федеральный округ', 
    'Архангельская область', 
    'Вологодская область', 
    'г. Санкт-Петербург', 
    'Калининградская область', 
    'Ленинградская область', 
    'Мурманская область', 
    'Ненецкий автономный округ', 
    'Новгородская область', 
    'Псковская область', 
    'Республика Карелия', 
    'Республика Коми', 
    'Дальневосточный федеральный округ', 
    'Амурская область', 
    'Еврейская автономная область', 
    'Забайкальский край', 
    'Камчатский край', 
    'Магаданская область', 
    'Приморский край', 
    'Республика Бурятия', 
    'Республика Саха (Якутия)', 
    'Сахалинская область', 
    'Хабаровский край', 
    'Чукотский автономный округ', 
    'Сибирский федеральный округ', 
    'Алтайский край', 
    'Иркутская область', 
    'Кемеровская область - Кузбасс', 
    'Красноярский край', 
    'Новосибирская область', 
    'Омская область', 
    'Республика Алтай', 
    'Республика Тыва', 
    'Республика Хакасия', 
    'Томская область', 
    'Уральский федеральный округ', 
    'Курганская область', 
    'Свердловская область', 
    'Тюменская область', 
    'Ханты-Мансийский автономный округ - Югра', 
    'Челябинская область', 
    'Ямало-Ненецкий автономный округ', 
    'Приволжский федеральный округ', 
    'Кировская область', 
    'Нижегородская область', 
    'Оренбургская область', 
    'Пензенская область', 
    'Пермский край', 
    'Республика Башкортостан', 
    'Республика Марий Эл', 
    'Республика Мордовия', 
    'Республика Татарстан (Татарстан)', 
    'Самарская область', 
    'Саратовская область', 
    'Удмуртская республика', 
    'Ульяновская область', 
    'Чувашская Республика - Чувашия', 
    'Северо-Кавказский федеральный округ', 
    'Кабардино-Балкарская Республика', 
    'Карачаево-Черкесская Республика', 
    'Республика Дагестан', 
    'Республика Ингушетия', 
    'Республика Северная Осетия - Алания', 
    'Ставропольский край', 
    'Чеченская республика', 
    'Крымский федеральный округ', 
    'г. Байконур'
]

allDiseaseIndex = [
    'Сифилис (впервые выявленный) все формы',
     'Другие сальмонеллезные инфекции',
     'Носительство возбудителя COVID-19',
     'Гранулоцитарный анаплазмоз человека',
     'Острый вирусный гепатит Е',
     'Трихинеллез',
     'Корь',
     'Бациллярные формы туберкулеза',
     'Гонококковая инфекция',
     'ОКИ, ПТ установленной этиологии',
     'Энтеровирусные инфекции',
     'Грипп',
     'Болезнь Брилля',
     'Бактериальная дизентерия (шигеллез)',
     'Педикулез',
     'Моноцитарный эрлихиоз человека',
     'Клещевой вирусный энцефалит',
     'Генерализованные формы менингококковой инфекции',
     'Острые вялые параличи',
     'Менингококковая инфекция',
     'Лихорадка Ку',
     'Туберкулез органов дыхания',
     'Краснуха',
     'J10-J11 Грипп',
     'Риккетсиоз, вызываемый Anaplasma phagocytophilum',
     'Туляремия',
     'Лихорадка Денге',
     'Острые инфекции верхних дыхательных путей множественной или неуточненной локализации',
     'Крымская геморрагическая лихорадка (вызванная вирусом Конго)',
     'Паротит эпидемический',
     'Бруцеллез, впервые выявленный',
     'Хронический гепатит В',
     'Геморрагические лихорадки с почечным синдромом',
     'Псевдотуберкулез',
     'Острый паралитический полиомиелит',
     'Острый вирусный гепатит С',
     'Хронический гепатит С',
     'ОКИ, ПТ неустановленной этиологии',
     'Укусы, ослюнения, оцарапывания животными',
     'Острые вирусные гепатиты',
     'Носительство возбудителя вирусного гепатита В',
     'Хронические вирусные гепатиты',
     'Эпидемический сыпной тиф',
     'Пневмонии, вызванные вирусом COVID-19',
     'Поствакцинальные осложнения',
     'Астраханская пятнистая лихорадка',
     'Ветряная оспа',
     'Лептоспироз',
     'Пневмонии, вызванные вирусом COVID-19, вирус идентифицирован',
     'Сибирская язва',
     'Острый вирусный гепатит А',
     'Сибирский клещевой тиф',
     'Вирусные лихорадки, передаваемые членистоногими и вирусные геморрагические лихорадки',
     'Пневмония (внебольничная)',
     'Дифтерия',
     'COVID-19',
     'Риккетсиозы',
     'Укусы, нанесенные собаками',
     'Укусы клещами',
     'Клещевой боррелиоз (болезнь Лайма)',
     'Риккетсиоз, вызываемый Ehrlichia chaffeensis и Ehrlichia muris',
     'Брюшной тиф',
     'Малярия, впервые выявленная',
     'Туберкулез (впервые выявленный) активные формы',
     'Коклюш',
     'Лихорадка Западного Нила',
     'Острый вирусный гепатит В',
     'Болезнь, вызванная вирусом иммунодефицита человека (ВИЧ) и бессимптомный инфекционный статус, вызванный (ВИЧ)',
     'Энтеровирусный менингит',
     'Бешенство'
]

checkDict = {
        'year' : years,
        'month' : months,
        'region' : regions
    }

