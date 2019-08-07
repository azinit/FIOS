"""
.com (commercial) — для коммерческих организаций.
.net (networks) — для сетевых структур.
.org (organizations) — некоммерческие организации.
.biz (business organizations) — только коммерческие организации.
.info (information) — домен открытый для всех.
.name (personal) — для персональных сайтов.
.pro (professionals) — для специалистов определённых профессий.

Не так часто встречаются, но все-таки существуют такие доменные зоны как:
.asia — домен для резидентов азиатско-тихоокеанского региона.
.aero — организации и физические лица, так или иначе связанные с аэроиндустрией.
.cat — предназначен для представителей каталонского лингвистического и культурного сообщества.
.coop — для кооперативных организаций.
.eco — для интернет-ресурсов, связанных с экологией.
.jobs — домен для веб-сайтов с информацией о востребованных профессиях и вакансиях.
.mobi — для сайтов и сервисов, ориентированных на работу с мобильными телефонами и беспроводными устройствами.
.museum — для музеев.
.post — для почтовых организаций.
.tel — для хранения и управления персональными и корпоративными контактами.
.travel — для туристической индустрии.
.xxx — сайты для взрослых.

Доменные зоны .ru .by .kz и т.д. являются национальными и показывают (по задумке) на аудиторию какой страны направлен ресурс. Так:
.ru — Россия.
.by — Беларусь.
"""

# __domain_zones = {
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "net": {"name": ".net", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "org": {"name": ".org", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "biz": {"name": ".biz", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "info": {"name": ".info", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "name": {"name": ".name", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "pro": {"name": ".pro", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "asia": {"name": ".asia", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "aero": {"name": ".aero", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "cat": {"name": ".cat", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "coop": {"name": ".coop", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "eco": {"name": ".eco", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "jobs": {"name": ".jobs", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "mobi": {"name": ".mobi", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "museum": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "post": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "tel": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "travel": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "xxx": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "ru": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "by": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
#     "com": {"name": ".com", "full_name": "commercial", "description": "для коммерческих организаций"},
# }


def get_domain_zones():
    return [".com", ".net", ".org", ".io", ".ru", ".eu", ".net"]
