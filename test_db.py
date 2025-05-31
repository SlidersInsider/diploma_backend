# # import pymysql
# #
# # host = "80.87.104.185"
# # user = "test"
# # password = "test"
# # database = "diploma"
# #
# # try:
# #     conn = pymysql.connect(host=host, user=user, password=password, database=database)
# #     print("✅ Подключение успешно!")
# #     conn.close()
# # except Exception as e:
# #     print("❌ Ошибка подключения:", e)
#
#
# from Crypto.PublicKey import RSA
#
# # Генерация ключа (2048 бит — рекомендуется для безопасности)
# key = RSA.generate(2048)
#
# # Приватный ключ
# private_key = key.export_key().decode()  # Экспортируем как строку
#
# # Публичный ключ
# public_key = key.publickey().export_key().decode()  # Экспортируем как строку
#
# print("🔑 Приватный ключ RSA:")
# print(private_key)
#
# print("\n🔓 Публичный ключ RSA:")
# print(public_key)
#
# #
# # 🔑 Приватный ключ RSA:
# # -----BEGIN RSA PRIVATE KEY-----
# # MIIEowIBAAKCAQEAucrIn4fM3ANSMAJUnD64CHCwUFI1nIFE/SshMcU75xniuQQN
# # 9AETz4kUPg4a0AL/i32AWCpJ1/KxsPd3wRPcbs2bDxmbbRC8pgrRzitzZLxGrRtv
# # utl83TJq0Gx/0wxNv9JDPlmkPsqrVX9o6b64L67RqdMCWXHdiEY/aqNK8J9Pcyny
# # 94eaW6pvl7pPz+U3DYuCH9QwwOIsY4EN/Mih6uQXPxCFcWv3XV3MA14YpQb7otwr
# # u3A74RLuMYZYQE56d4FQRPcELxhr32/0Vm/EoNx8AnGe1ZXmsiuswHWK2v8kgeIb
# # 4yyPnwe4qABCyIq5SJXdzhiXIVGOqYYPrHZOywIDAQABAoIBAACzJ2m7kBMfgl11
# # EoEWcj+V4++OFpNSoC/mObCkBGgIJ8lTw7mwtRAcNBK+n22ElV+MkFPEsHA7OcuM
# # R6cyh2IICM18nX3U0k7Nzeo45D+GCFBnwOiOsk5HkA0mpJ3CUq04lGOw4HalOn/8
# # hAQUPPjMb8bhsk5IhBY/UhAd6MXIZHddnLZIhWT/qmGhj1ivoPtxw6U3sEt4Xi8c
# # 37zR9TlC3GK4Cxuls6XX/Tx9Ogb4oBtGyTQyv/jIFJRNQvXyHaM9lWCdOaegk22y
# # e+aSTCIb5rTalWxdjNYNsaZlB4qINlV5K9nymLAFABfr6Fr35J/3trUUtLpBEFeg
# # ZXSNygECgYEAvxNChJKBGoqExD0kQJjmMgC87JXGw4aDXeuxwhgSb1V9Zolaq2R+
# # vu2nP+aDI55qLr/qbKPxCb1rfj/rpRdkCoSg2Ik9sQ17oXn+JrOiYEnCAIKv2UWt
# # VaLL87XFSGhIc/ulttk6XFY7dLpfWa8r0aDG/h6dB02LxK+U9jIj2a0CgYEA+Ov4
# # iStzRyE7pUS4mew0/k6zFWj3Hhmu3mn4yPOLyCJZuSVD9Qm3btVsPfyr5zDmDZSv
# # eHEGuSTI/S1TKxfMpac9dNyUmfNygrSlesN8XWZ5owMo5EgVivPceYrfb/CZWNm2
# # R7r2lCCHaE44U78J/lGH85oqR2yU38dl506pSVcCgYA5d9J2yxV3ZRf/aaBAqXv6
# # qAwqX/XTEt7p3ZyuEs1gnObFcyRJDkWsqQ+3gV4J1Xh8LQ6VtE0nr8fnxdPa6IkX
# # PMKfvc9HNBXuACH3g+mfai+mNagsAe/bJMaQuyfl2i+IarRxpS4PXYQuXGuXLr9Q
# # IjoXbh+udZ1G/8Qes//iVQKBgQDNbrncQv7NmlDGcbPEXJvTsZG8vrcLoXifWGgZ
# # OF6JWkggM/Ak39MCZqMBeXFJySJj3O0AAo/g5sn1oJ19+BNON3rR4mXFtJQx6PKV
# # IZaW4sbKUQZDeHZHCkFQEdubX76/BFaaVmPAFiSKYdu8yfJucE06L2ZrMeKf2Mly
# # H4o42wKBgF8F9uO15vo2CzOhxiSvvdYhsL35nuPy3QziY98x/6SdP6MVIKN0hy6l
# # cOPQtzRq2QEfPmhQb2S72zTxxm5PNl14JqPUonks/h/QaQq4SoaDlBd7iXsecrO2
# # Jzcmu8/jItePdmt1TvTehvZ2dT2T2MAz9wx3Aa+nZ6T9QMvj3eGD
# # -----END RSA PRIVATE KEY-----
# #
# # 🔓 Публичный ключ RSA:
# # -----BEGIN PUBLIC KEY-----
# # MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAucrIn4fM3ANSMAJUnD64
# # CHCwUFI1nIFE/SshMcU75xniuQQN9AETz4kUPg4a0AL/i32AWCpJ1/KxsPd3wRPc
# # bs2bDxmbbRC8pgrRzitzZLxGrRtvutl83TJq0Gx/0wxNv9JDPlmkPsqrVX9o6b64
# # L67RqdMCWXHdiEY/aqNK8J9Pcyny94eaW6pvl7pPz+U3DYuCH9QwwOIsY4EN/Mih
# # 6uQXPxCFcWv3XV3MA14YpQb7otwru3A74RLuMYZYQE56d4FQRPcELxhr32/0Vm/E
# # oNx8AnGe1ZXmsiuswHWK2v8kgeIb4yyPnwe4qABCyIq5SJXdzhiXIVGOqYYPrHZO
# # ywIDAQAB
# # -----END PUBLIC KEY-----


# from graphviz import Digraph
#
# # Создаем граф
# dot = Digraph(comment="ER Diagram", format='png')
# dot.attr('node', shape='plaintext')
# dot.attr(splines='ortho')
#
# # Описание таблиц с полями, ключами и их типами
# tables = {
#     "users": {
#         "fields": ["id", "username", "password_hash", "role_id", "public_key"],
#         "pk": ["id"],
#         "fk": {"role_id": "roles.id"}
#     },
#     "roles": {
#         "fields": ["id", "name"],
#         "pk": ["id"],
#         "fk": {}
#     },
#     "projects": {
#         "fields": ["id", "name", "description", "creator_id"],
#         "pk": ["id"],
#         "fk": {"creator_id": "users.id"}
#     },
#     "files": {
#         "fields": ["id", "project_id", "user_id", "filename", "file_path", "encryption_key"],
#         "pk": ["id"],
#         "fk": {"project_id": "projects.id", "user_id": "users.id"}
#     },
#     "keys": {
#         "fields": ["id", "user_id", "file_id", "project_id", "encrypted_key"],
#         "pk": ["id"],
#         "fk": {"user_id": "users.id", "file_id": "files.id", "project_id": "projects.id"}
#     },
#     "requests": {
#         "fields": ["id", "user_id", "username", "project_id", "manager_id"],
#         "pk": ["id"],
#         "fk": {"user_id": "users.id", "project_id": "projects.id", "manager_id": "users.id"}
#     },
#     "user_projects": {
#         "fields": ["user_id", "project_id"],
#         "pk": ["user_id", "project_id"],
#         "fk": {"user_id": "users.id", "project_id": "projects.id"}
#     },
# }
#
# # Создаем таблицы с HTML-разметкой
# for table_name, table_info in tables.items():
#     rows = [f'<TR><TD BGCOLOR="lightblue" COLSPAN="2"><B>{table_name}</B></TD></TR>']
#     for field in table_info["fields"]:
#         props = []
#         if field in table_info["pk"]:
#             props.append("PK")
#         if field in table_info["fk"]:
#             props.append("FK")
#         tag = " / ".join(props)
#         rows.append(f'<TR><TD ALIGN="LEFT">{field}</TD><TD>{tag}</TD></TR>')
#
#     table_html = f"""<
#     <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
#         {''.join(rows)}
#     </TABLE>>"""
#     dot.node(table_name, table_html)
#
# # Добавляем связи между таблицами
# for table_name, table_info in tables.items():
#     for fk_field, ref in table_info["fk"].items():
#         ref_table, _ = ref.split('.')
#         dot.edge(table_name, ref_table, label=fk_field)
#
# # Генерируем файл
# dot.render('er_diagram', cleanup=False)

# from graphviz import Digraph
#
#
# def draw_architecture(name):
#     dot = Digraph(comment=f"{name} Architecture", format='png')
#     dot.attr(rankdir='LR', fontsize='20')
#
#     if name == "Одноуровневая":
#         dot.node('App', 'Приложение (монолит)\nUI + Логика + БД')
#
#     elif name == "Двухуровневая":
#         dot.node('Client', 'Клиентское приложение')
#         dot.node('ServerDB', 'Сервер с логикой\nи встроенной БД')
#         dot.edge('Client', 'ServerDB')
#
#     elif name == "Трёхуровневая":
#         dot.node('Client', 'Клиент')
#         dot.node('Server', 'Серверное приложение\n(логика)')
#         dot.node('DB', 'База данных')
#         dot.edge('Client', 'Server')
#         dot.edge('Server', 'DB')
#
#     elif name == "Многоуровневая":
#         dot.node('Client', 'Клиент')
#         dot.node('Gateway', 'API Gateway / Балансировщик')
#         dot.node('AuthService', 'Сервис авторизации')
#         dot.node('DataService', 'Сервис данных')
#         dot.node('DB1', 'БД пользователей')
#         dot.node('DB2', 'БД файлов')
#
#         dot.edge('Client', 'Gateway')
#         dot.edge('Gateway', 'AuthService')
#         dot.edge('Gateway', 'DataService')
#         dot.edge('AuthService', 'DB1')
#         dot.edge('DataService', 'DB2')
#
#     else:
#         raise ValueError("Неизвестная архитектура")
#
#     filename = name.lower().replace(" ", "_")
#     dot.render(filename, cleanup=False)
#     print(f"Схема {name} сохранена в файл: {filename}.png")
#
#
# # Генерируем все 4 архитектуры
# for arch in ["Одноуровневая", "Двухуровневая", "Трёхуровневая", "Многоуровневая"]:
#     draw_architecture(arch)
# from graphviz import Digraph
#
# dot = Digraph(comment="Detailed Framework Module Comparison", format="png")
# dot.attr(rankdir='LR', fontsize='20', splines='ortho')
#
# frameworks = {
#     "FastAPI": {
#         "FastAPI App": ["Routing", "Dependency Injection", "Pydantic Models", "OpenAPI Docs"]
#     },
#     "Flask": {
#         "Flask App": ["Routing", "Jinja2 Templates", "Flask Extensions", "Werkzeug"],
#         "Flask Extensions": ["Flask-Login", "Flask-Migrate"]
#     },
#     "Django": {
#         "Django Project": ["ORM", "Admin", "Templates", "Middleware", "Authentication"]
#     },
#     "Node.js (Express)": {
#         "Express App": ["Routing", "Middleware", "View Engine", "Body Parser", "Custom Modules"],
#         "Middleware": ["Logger", "Error Handler"]
#     },
#     "Spring Boot": {
#         "Spring Boot App": ["Spring MVC", "Spring Security", "Spring Data JPA", "Actuator", "Thymeleaf"],
#         "Spring Security": ["JWT", "OAuth2"]
#     }
# }
#
# for fw, structure in frameworks.items():
#     with dot.subgraph(name=f"cluster_{fw}") as c:
#         c.attr(label=fw, style='filled', color='lightgrey')
#         for parent, children in structure.items():
#             parent_id = f"{fw}_{parent}"
#             c.node(parent_id, parent, shape="box", style="filled", color="lightblue")
#             for child in children:
#                 child_id = f"{fw}_{child}"
#                 c.node(child_id, child)
#                 c.edge(parent_id, child_id)
#
# dot.render("framework_modules_detailed_diagram_2", cleanup=False)

# from graphviz import Digraph
#
# dot = Digraph(comment='Architecture', format='png')
# dot.attr(rankdir='LR', style='filled', fontsize='12')
#
# dot.node('Client', 'Клиент (браузер/Postman)\nотправляет HTTP-запросы', shape='ellipse', fillcolor='#D9EDF7', style='filled')
# dot.node('FastAPI', 'FastAPI (Web Framework)', fillcolor='#DFF0D8')
# dot.node('Router', 'Маршруты (APIRouter)', fillcolor='#DFF0D8')
# dot.node('Services', 'Сервисы\n(Шифрование, Аутентификация, и т.п.)', fillcolor='#DFF0D8')
# dot.node('DB', 'База данных\n(MySQL + SQLAlchemy)', fillcolor='#FCF8E3')
# dot.node('Models', 'ORM Модели', fillcolor='#F5F5F5')
# dot.node('Schemas', 'Pydantic Схемы', fillcolor='#F5F5F5')
# dot.node('Files', 'Хранение файлов\n(upload_dir)', fillcolor='#F5F5F5')
#
# dot.edges([('Client', 'FastAPI'), ('FastAPI', 'Router')])
# dot.edges([('Router', 'Schemas'), ('Router', 'Services'), ('Router', 'DB'), ('Router', 'Files')])
# dot.edges([('DB', 'Models'), ('Models', 'DB')])
# dot.edge('Services', 'DB')
# dot.edge('Services', 'Files')
#
# dot.render('diagrams/architecture', view=True)

# from graphviz import Digraph
#
# dot = Digraph(comment='Routes', format='png')
# dot.attr(compound='true', style='filled', fontsize='10')
#
# # Цвета методов
# method_colors = {
#     'GET': '#B2EBF2',     # голубой
#     'POST': '#C8E6C9',    # зелёный
#     'DELETE': '#FFCDD2',  # красный
#     'PUT': '#FFF9C4'      # жёлтый
# }
#
# def add_node(graph, name, path, method, params=None):
#     color = method_colors.get(method, '#E0E0E0')
#     param_str = f"\nParams: {params}" if params else ""
#     label = f"{path}\\n{method}{param_str}"
#     graph.node(name, label, fillcolor=color, style='filled')
#
# # --- Аутентификация ---
# with dot.subgraph(name='cluster_auth') as auth:
#     auth.attr(label='Аутентификация')
#     add_node(auth, 'register', '/register', 'POST', 'username, password')
#     add_node(auth, 'login', '/login', 'POST', 'username, password')
#
# # --- Пользователи ---
# with dot.subgraph(name='cluster_users') as users:
#     users.attr(label='Пользователи')
#     add_node(users, 'get_users', '/users/', 'GET')
#     add_node(users, 'create_user', '/users/', 'POST', 'username, password, role_id')
#     add_node(users, 'delete_user', '/users/{id}', 'DELETE', 'id')
#     add_node(users, 'update_user', '/users/{id}', 'PUT', 'username, password, role_id')
#
# # --- Роли ---
# with dot.subgraph(name='cluster_roles') as roles:
#     roles.attr(label='Роли')
#     add_node(roles, 'get_roles', '/roles/', 'GET')
#     add_node(roles, 'create_role', '/roles/', 'POST', 'name, permissions')
#     add_node(roles, 'delete_role', '/roles/{id}', 'DELETE', 'id')
#     add_node(roles, 'update_role', '/roles/{id}', 'PUT', 'name, permissions')
#
# # --- Проекты ---
# with dot.subgraph(name='cluster_projects') as projects:
#     projects.attr(label='Проекты')
#     add_node(projects, 'get_projects', '/projects/', 'GET')
#     add_node(projects, 'create_project', '/projects/', 'POST', 'name, description')
#     add_node(projects, 'delete_project', '/projects/{id}', 'DELETE', 'id')
#     add_node(projects, 'update_project', '/projects/{id}', 'PUT', 'name, description')
#
# # --- Связь пользователь–проект ---
# with dot.subgraph(name='cluster_user_projects') as up:
#     up.attr(label='Связь пользователь–проект')
#     add_node(up, 'add_user_project', '/user-projects/', 'POST', 'user_id, project_id')
#     add_node(up, 'remove_user_project', '/user-projects/', 'DELETE', 'user_id, project_id')
#
# # --- Файлы ---
# with dot.subgraph(name='cluster_files') as files:
#     files.attr(label='Файлы')
#     add_node(files, 'upload_file', '/files/', 'POST', 'file')
#     add_node(files, 'list_files', '/files/', 'GET')
#     add_node(files, 'download_file', '/files/download/{id}', 'POST', 'id')
#     add_node(files, 'delete_file', '/files/{id}', 'DELETE', 'id')
#
# # --- Заявки ---
# with dot.subgraph(name='cluster_requests') as reqs:
#     reqs.attr(label='Заявки')
#     add_node(reqs, 'create_request', '/requests/', 'POST', 'user_id, project_id, file_ids')
#     add_node(reqs, 'get_requests', '/requests/', 'GET')
#
# # --- Администрирование ---
# with dot.subgraph(name='cluster_admin') as admin:
#     admin.attr(label='Администрирование')
#     add_node(admin, 'admin_overview', '/admin/overview', 'GET')
#
# # Генерация схемы
# dot.render('diagrams/routes_colored_detailed', view=True)

# from graphviz import Digraph
#
# arch = Digraph('Architecture', format='png')
# arch.attr(rankdir='LR', style='filled', fontsize='10', compound='true')
#
# # Цвета
# color_service = '#C5E1A5'
# color_db = '#FFE082'
# color_ext = '#B3E5FC'
#
# # Внешние пользователи
# arch.node('User', 'Клиент (браузер)', shape='oval', fillcolor=color_ext, style='filled')
#
# # API Gateway
# arch.node('Gateway', 'API Gateway\n(REST)', shape='box', fillcolor=color_service, style='filled')
#
# # Auth service
# arch.node('Auth', 'Auth Service', shape='box', fillcolor=color_service, style='filled')
# arch.node('AuthDB', 'Auth DB\n(Users, Tokens)', shape='cylinder', fillcolor=color_db, style='filled')
#
# # Project service
# arch.node('Project', 'Project Service', shape='box', fillcolor=color_service, style='filled')
# arch.node('ProjectDB', 'Project DB\n(Projects, Relations)', shape='cylinder', fillcolor=color_db, style='filled')
#
# # File service
# arch.node('File', 'File Service', shape='box', fillcolor=color_service, style='filled')
# arch.node('FileStorage', 'Storage\n(S3, Local FS)', shape='cylinder', fillcolor=color_db, style='filled')
#
# # Request service
# arch.node('Request', 'Request Service', shape='box', fillcolor=color_service, style='filled')
# arch.node('RequestDB', 'Request DB', shape='cylinder', fillcolor=color_db, style='filled')
#
# # Связи
# arch.edges([
#     ('User', 'Gateway'),
#     ('Gateway', 'Auth'),
#     ('Gateway', 'Project'),
#     ('Gateway', 'File'),
#     ('Gateway', 'Request'),
#
#     ('Auth', 'AuthDB'),
#     ('Project', 'ProjectDB'),
#     ('File', 'FileStorage'),
#     ('Request', 'RequestDB'),
# ])
#
# arch.render('diagrams/architecture', view=True)

# from graphviz import Digraph
#
# crypto = Digraph('EncryptionFlow', format='png')
# crypto.attr(rankdir='LR', style='filled', fontsize='10')
#
# color_process = '#D1C4E9'
# color_data = '#FFECB3'
# color_sec = '#C8E6C9'
#
# # Пользователь -> Шифрование пароля
# crypto.node('User', 'Пользователь', shape='oval', fillcolor=color_data, style='filled')
# crypto.node('Password', 'Ввод пароля', shape='box', fillcolor=color_data, style='filled')
# crypto.node('Hash', 'SHA-256\n+ Salt', shape='box', fillcolor=color_sec, style='filled')
# crypto.node('AuthDB', 'Auth DB\n(Хэш пароля)', shape='cylinder', fillcolor=color_data, style='filled')
#
# # JWT
# crypto.node('JWTGen', 'Генерация JWT\n(с подписью)', shape='box', fillcolor=color_sec, style='filled')
# crypto.node('ClientToken', 'JWT\nна клиенте', shape='note', fillcolor=color_data, style='filled')
#
# # Защита файлов
# crypto.node('UploadFile', 'Загрузка файла', shape='box', fillcolor=color_data, style='filled')
# crypto.node('EncryptFile', 'AES-256\nШифрование файла', shape='box', fillcolor=color_sec, style='filled')
# crypto.node('Storage', 'Файловое хранилище\n(Зашифровано)', shape='cylinder', fillcolor=color_data, style='filled')
#
# # Передача токена
# crypto.edge('User', 'Password')
# crypto.edge('Password', 'Hash')
# crypto.edge('Hash', 'AuthDB')
#
# crypto.edge('Hash', 'JWTGen')
# crypto.edge('JWTGen', 'ClientToken')
#
# # Защищённый доступ к API
# crypto.edge('ClientToken', 'UploadFile')
# crypto.edge('UploadFile', 'EncryptFile')
# crypto.edge('EncryptFile', 'Storage')
#
# crypto.render('diagrams/encryption', view=True)
#
from graphviz import Digraph

arch = Digraph('Architecture', format='png')
arch.attr(rankdir='LR', fontsize='10', compound='true')

color_api = '#BBDEFB'
color_service = '#C8E6C9'
color_db_table = '#FFF9C4'

# Внешний пользователь
arch.node('User', 'Client', shape='oval', style='filled', fillcolor=color_api)

arch.node('Gateway', 'Server', shape='box', style='filled', fillcolor=color_api)

# Кластер с сервисами
with arch.subgraph(name='cluster_services') as db:
    db.attr(label='Services', style='dashed', color='gray')

    services = {
        'src_auth': 'Auth ',
        'src_user': 'Users ',
        'src_role': 'Roles ',
        'src_project': 'Projects ',
        'src_up': 'User–Project',
        'src_file': 'Files ',
        'src_request': 'Requests '
    }
    for node, label in services.items():
        db.node(node, label, shape='box', style='filled', fillcolor=color_service)
        arch.edge('Gateway', node, style='dashed', arrowhead='none')


# База данных — цилиндр
arch.node('MainDB', 'Database', shape='cylinder', style='filled', fillcolor='#FFD54F')

# Кластер с таблицами
with arch.subgraph(name='cluster_tables') as db:
    db.attr(label='Tables', style='dashed', color='gray')
    tables = {
        'tbl_users': 'Users',
        'tbl_roles': 'Roles',
        'tbl_projects': 'Projects',
        'tbl_user_project': 'User–Project',
        'tbl_files': 'Files',
        'tbl_keys': 'Keys',
        'tbl_requests': 'Requests',
    }
    for node, label in tables.items():
        db.node(node, label, shape='box', style='filled', fillcolor=color_db_table)
        arch.edge('MainDB', node, style='dashed', arrowhead='none')  # Связь от цилиндра к таблицам

# Взаимосвязи
arch.edge('User', 'Gateway')


# Добавляем стрелку от Server к MainDB
arch.edge('src_project', 'MainDB', label='SQL/ORM')

# Генерация схемы
arch.render('diagrams/architecture_with_cylinder_db', view=True)


#

# from graphviz import Digraph
#
# # Создание объекта графа
# dot = Digraph(comment='App Architecture', format='png')
# dot.attr(rankdir='TB')  # Горизонтальное направление
# dot.attr('node', shape='box', style='filled', fontname='Arial')
#
# # Определение модулей
# dot.node('App', 'App Module\n(UI, MVVM, Single-Activity)', color='lightblue', shape='component')
# dot.node('Network', 'Network Module\n(Retrofit, OkHttp, Repositories)', color='lightgreen', shape='component')
# dot.node('Reader', 'Reader Module\n(TXT, PDF, DOCX Readers)', color='lightgreen', shape='component')
#
# # Связи между модулями
# dot.edge('App', 'Network', label=' DI\n(ViewModel -> Repository)')
# dot.edge('App', 'Reader', label=' DI\n(ViewModel -> FileHandler)')
#
# # Генерация и сохранение схемы
# dot.render('diagrams/app_architecture', view=True)


# from graphviz import Digraph
#
# # Создание графа
# dot = Digraph(comment='Sample Relational Database Schema', format='png')
# dot.attr(rankdir='LR', splines='ortho')
#
# # Примерные таблицы и их поля
# tables = {
#     'Users': ['id (PK)', 'name', 'email', 'password'],
#     'Roles': ['id (PK)', 'role_name'],
#     'UserRoles': ['user_id (FK)', 'role_id (FK)'],
#     'Projects': ['id (PK)', 'title', 'description', 'owner_id (FK)'],
#     'Files': ['id (PK)', 'filename', 'path', 'project_id (FK)', 'uploaded_by (FK)'],
#     'AuditLogs': ['id (PK)', 'user_id (FK)', 'action', 'timestamp']
# }
#
# # Добавляем таблицы как HTML-таблицы
# for table, columns in tables.items():
#     label = f"<<TABLE BORDER='1' CELLBORDER='0' CELLSPACING='0'>"
#     label += f"<TR><TD BGCOLOR='lightgray'><B>{table}</B></TD></TR>"
#     for col in columns:
#         label += f"<TR><TD ALIGN='LEFT'>{col}</TD></TR>"
#     label += "</TABLE>>"
#     dot.node(table, label=label, shape='plain')
#
# # Связи (внешние ключи)
# relations = [
#     ('UserRoles', 'Users', 'user_id'),
#     ('UserRoles', 'Roles', 'role_id'),
#     ('Projects', 'Users', 'owner_id'),
#     ('Files', 'Projects', 'project_id'),
#     ('Files', 'Users', 'uploaded_by'),
#     ('AuditLogs', 'Users', 'user_id')
# ]
#
# # Добавляем стрелки с подписями
# for src, dst, label in relations:
#     dot.edge(src, dst, label=label)
#
# # Сохраняем и генерируем PNG
# output_path = dot.render('diagrams/rel_schema', format='png', cleanup=True)

# from graphviz import Digraph
#
# # Создание графа
# dot = Digraph(comment='Sample Document-Oriented Database Schema', format='png')
# dot.attr(rankdir='LR', splines='ortho')
#
# # Коллекции и поля (структура JSON-документов)
# collections = {
#     'users': ['_id', 'name', 'email', 'roles [Array of ObjectId]', 'created_at'],
#     'roles': ['_id', 'name', 'permissions [Array of String]'],
#     'projects': ['_id', 'title', 'description', 'owner_id (ref users)', 'members [Array of ObjectId]'],
#     'files': ['_id', 'filename', 'path', 'project_id (ref projects)', 'uploaded_by (ref users)', 'metadata'],
#     'audit_logs': ['_id', 'user_id (ref users)', 'action', 'timestamp']
# }
#
# # Добавление коллекций как HTML-таблиц
# for collection, fields in collections.items():
#     label = f"<<TABLE BORDER='1' CELLBORDER='0' CELLSPACING='0'>"
#     label += f"<TR><TD BGCOLOR='lightblue'><B>{collection}</B></TD></TR>"
#     for field in fields:
#         label += f"<TR><TD ALIGN='LEFT'>{field}</TD></TR>"
#     label += "</TABLE>>"
#     dot.node(collection, label=label, shape='plain')
#
# # Связи между коллекциями (ссылки по ObjectId)
# relations = [
#     ('users', 'roles', 'roles[]'),
#     ('projects', 'users', 'owner_id'),
#     ('projects', 'users', 'members[]'),
#     ('files', 'projects', 'project_id'),
#     ('files', 'users', 'uploaded_by'),
#     ('audit_logs', 'users', 'user_id')
# ]
#
# # Добавляем связи
# for src, dst, label in relations:
#     dot.edge(src, dst, label=label)
#
# # Сохраняем как PNG
# output_path = dot.render('diagrams/document_db_schema', format='png', cleanup=True)
#
# print(f"Схема документной базы данных сохранена: {output_path}")

# from graphviz import Digraph
#
# dot = Digraph(comment='Key-Value Store Schema', format='png')
#
# # Узлы - пары ключ-значение
# dot.node('KV1', 'user:1001\n{\n  name: "Alice",\n  age: 30\n}', shape='note')
# dot.node('KV2', 'session:xyz123\n{\n  token: "...",\n  user_id: 1001\n}', shape='note')
# dot.node('KV3', 'cart:1001\n["item1", "item2"]', shape='note')
#
# # Сохраняем
# dot.render('diagrams/key_value_db_schema', format='png', cleanup=True)
# print("Схема Key-Value БД сохранена.")

# from graphviz import Digraph
#
# dot = Digraph(comment='Column-Oriented Database Schema', format='png')
#
# # Таблица как колонны
# dot.node('users', label=\
#     '''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
#     <TR><TD BGCOLOR="lightgreen"><B>users</B></TD></TR>
#     <TR><TD>user_id</TD></TR>
#     <TR><TD>name</TD></TR>
#     <TR><TD>email</TD></TR>
#     <TR><TD>last_login</TD></TR>
#     </TABLE>>''', shape='plain')
#
# dot.node('orders', label=\
#     '''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
#     <TR><TD BGCOLOR="lightgreen"><B>orders</B></TD></TR>
#     <TR><TD>order_id</TD></TR>
#     <TR><TD>user_id</TD></TR>
#     <TR><TD>amount</TD></TR>
#     <TR><TD>status</TD></TR>
#     </TABLE>>''', shape='plain')
#
# dot.edge('orders', 'users', label='user_id')
#
# # Сохраняем
# dot.render('diagrams/column_db_schema', format='png', cleanup=True)
# print("Схема колонно-ориентированной БД сохранена.")

# from graphviz import Digraph
#
# dot = Digraph(comment='Graph DB Schema', format='png')
#
# # Вершины (узлы)
# dot.node('User1', 'User: Alice', shape='ellipse', style='filled', fillcolor='lightyellow')
# dot.node('User2', 'User: Bob', shape='ellipse', style='filled', fillcolor='lightyellow')
# dot.node('Project1', 'Project: SecureDocs', shape='ellipse', style='filled', fillcolor='lightblue')
#
# # Рёбра (связи)
# dot.edge('User1', 'Project1', label='OWNS')
# dot.edge('User2', 'Project1', label='MEMBER_OF')
# dot.edge('User1', 'User2', label='COLLEAGUE')
#
# # Сохраняем
# dot.render('diagrams/graph_db_schema', format='png', cleanup=True)
# print("Схема графовой БД сохранена.")

# from graphviz import Digraph
#
# dot = Digraph(comment='Server Architecture (FastAPI MVC)', format='png')
# dot.attr(rankdir='TB', splines='ortho', fontsize='12')
#
# # Главные блоки
# dot.node('API', 'FastAPI App', shape='box', style='filled', fillcolor='lightblue')
#
# # Модули
# dot.node('Routes', 'Routes\n(Обработка запросов)', shape='component', fillcolor='lightgray', style='filled')
# dot.node('Schemas', 'Schemas\n(Pydantic модели)', shape='component', fillcolor='lightyellow', style='filled')
# dot.node('Services', 'Services\n(Логика, шифрование, токены)', shape='component', fillcolor='lightgreen', style='filled')
# dot.node('Models', 'Models\n(SQLAlchemy ORM)', shape='component', fillcolor='lightpink', style='filled')
# dot.node('DB', 'DB\n(Подключение базы)', shape='component', fillcolor='orange', style='filled')
#
# # База данных
# dot.node('Database', 'MySQL', shape='cylinder', style='filled', fillcolor='white')
#
# # Взаимосвязи
# dot.edge('API', 'Routes', label='обработка HTTP-запросов')
# dot.edge('Routes', 'Schemas', label='валидация данных')
# dot.edge('Routes', 'Services', label='вызов логики')
# dot.edge('Services', 'Models', label='работа с ORM')
# dot.edge('Models', 'DB', label='инициализация')
# dot.edge('DB', 'Database', label='подключение')
# dot.edge('Models', 'Database', style='dashed', label='SQL операции')
#
# # Вывод PNG
# dot.render('diagrams/server_architecture', format='png', cleanup=True)
# print("Схема архитектуры серверной части сохранена как server_architecture.png")


# from graphviz import Digraph
#
# # Создаем направленный граф сверху вниз
# dot = Digraph(comment='API Routes Scheme', format='png')
# dot.attr(rankdir='TB', fontsize='12', compound='true', splines='ortho')
#
# # Цвета методов
# colors = {
#     "GET": "palegreen",
#     "POST": "lightskyblue",
#     "PUT": "lightyellow",
#     "DELETE": "lightcoral"
# }
#
# # Структура маршрутов
# routes = {
#     "Auth (/auth)": [
#         ("POST /register", "POST"),
#         ("POST /login", "POST"),
#     ],
#     "Users (/users)": [
#         ("GET /", "GET"),
#         ("GET /{username}", "GET"),
#         ("GET /{user_id}", "GET"),
#         ("DELETE /{user_id}", "DELETE"),
#         ("PUT /{user_id}/role", "PUT"),
#     ],
#     "Roles (/roles)": [
#         ("GET /", "GET"),
#         ("GET /{role_id}", "GET"),
#         ("POST /", "POST"),
#         ("DELETE /{role_id}", "DELETE"),
#     ],
#     "Projects (/projects)": [
#         ("GET /", "GET"),
#         ("GET /{project_name}", "GET"),
#         ("GET /{project_id}", "GET"),
#         ("POST /", "POST"),
#         ("DELETE /{project_id}", "DELETE"),
#     ],
#     "UserProject (/up)": [
#         ("GET /project/{project_id}", "GET"),
#         ("POST /", "POST"),
#         ("DELETE /", "DELETE"),
#     ],
#     "Files (/files)": [
#         ("GET /", "GET"),
#         ("GET /project/{project_id}", "GET"),
#         ("GET /user/{user_id}", "GET"),
#         ("GET /{file_id}", "GET"),
#         ("POST /", "POST"),
#         ("POST /download/{file_id}", "POST"),
#         ("DELETE /{file_id}", "DELETE"),
#         ("PUT /update/{file_id}", "PUT"),
#     ],
#     "Requests (/requests)": [
#         ("GET /{manager_id}", "GET"),
#         ("POST /request/", "POST"),
#     ]
# }
#
# # Добавляем подграфы для каждой группы маршрутов
# for group, endpoints in routes.items():
#     with dot.subgraph(name=f'cluster_{group}') as sub:
#         sub.attr(label=group, style='filled', fillcolor='lightgray')
#         for ep, method in endpoints:
#             sub.node(f"{group}_{ep}", ep, style='filled', fillcolor=colors[method])
#
# # Рендерим схему
# dot.render('diagrams/api_routes', format='png', cleanup=True)
# print("Схема маршрутов сохранена как api_routes.png")

# from graphviz import Digraph
#
# dot = Digraph(comment='User Registration and Key Exchange', format='png')
# dot.attr(rankdir='TB')
#
# dot.node('Client', 'Клиент\n(Мобильное устройство)', shape='box', style='filled', fillcolor='lightblue')
# dot.node('Server', 'Сервер', shape='box', style='filled', fillcolor='lightgray')
# dot.node('Keystore', 'Хранилище ключей', shape='cylinder', fillcolor='white', style='filled')
#
# # Стрелки
# dot.edge('Client', 'Server', 'Регистрация', color='black')
# dot.edge('Server', 'Client', 'Успех/Ошибка', color='black')
# dot.edge('Client', 'Keystore', 'Сохранение RSA-ключей', color='blue')
# dot.edge('Client', 'Server', 'Отправка публичного ключа и данных', color='green')
#
# # Рендер
# dot.render('diagrams/scheme_registration', cleanup=True)

# from graphviz import Digraph
#
# dot = Digraph(comment='Encrypted File Upload', format='png')
# dot.attr(rankdir='TB')
#
# dot.node('Client', 'Клиент\n(Руководитель)', shape='box', style='filled', fillcolor='lightblue')
# dot.node('Keystore', 'Хранилище ключей', shape='cylinder', fillcolor='white', style='filled')
# dot.node('Server', 'Сервер', shape='box', style='filled', fillcolor='lightgray')
# dot.node('Storage', 'Хранилище файлов', shape='folder')
# dot.node('DB', 'База данных', shape='cylinder')
#
# dot.edge('Client', 'Keystore', 'Получение RSA публичного ключа')
# dot.edge('Client', 'Client', 'Генерация AES-ключа\nШифрование файла и AES-ключа', color='blue')
# dot.edge('Client', 'Server', 'Отправка файла и данных', color='green')
# dot.edge('Server', 'Storage', 'Сохранение файла')
# dot.edge('Server', 'DB', 'Сохранение данных')
#
# dot.render('diagrams/scheme_file_upload', cleanup=True)


# from graphviz import Digraph
#
# dot = Digraph(comment='Encrypted File Download and Decryption', format='png')
# dot.attr(rankdir='TB')
#
# dot.node('Client', 'Клиент', shape='box', style='filled', fillcolor='lightblue')
# dot.node('Keystore', 'Хранилище ключей', shape='cylinder', fillcolor='white', style='filled')
# dot.node('Server', 'Сервер', shape='box', style='filled', fillcolor='lightgray')
# dot.node('Storage', 'Хранилище файлов', shape='folder')
# dot.node('DB', 'База данных', shape='cylinder')
#
# dot.edge('Client', 'Server', 'Скачиваение файла', color='black')
# dot.edge('Server', 'Storage', 'Получение зашифрованного файла')
# dot.edge('Server', 'DB', 'Получение AES-ключа')
# dot.edge('Server', 'Client', 'Возвращение файла и ключа')
# dot.edge('Client', 'Keystore', 'Получение приватного ключа', color='blue')
# dot.edge('Client', 'Client', 'Расшифровка AES-ключа\nРасшифровка файла', color='green')
#
# dot.render('diagrams/scheme_file_download', cleanup=True)
