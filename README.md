# 基于 Django 框架的网上快捷购物系统

## 一、项目简介

本项目是一个基于 Django 框架开发的网页版网上购物系统，为用户提供便捷、流畅的线上购物体验，同时为开发者展示 Django 在实际项目中的应用。系统实现了商品展示、购物车管理、订单处理等核心功能，适合作为学习 Django 开发、Web 项目实践的参考案例。

## 二、核心功能

**用户管理**：支持管理员注册、登录、密码重置功能，上传管理商品。

**商品展示**：分类展示各类商品，包含展示商品图片、价格、描述等详细信息，支持商品搜索功能，方便用户快速找到心仪商品。

**购物车功能**：用户可将商品添加至购物车，对购物车中的商品进行数量修改、删除操作，并实时计算购物车总价。

**订单处理**：用户确认购物车商品信息后可提交订单，系统生成订单号，记录订单详情，支持订单状态查看。

**支付模拟**：集成模拟支付功能，展示支付流程，但不涉及真实资金交易。（还未实现）

## 三、技术栈

**后端**：

**Django**：使用高性能 Python Web 框架，用于搭建整个后端系统，处理业务逻辑、数据库交互等。

**Django REST framework**：用于构建 API 接口，方便与前端进行数据交互。

**MySQL**：关系型数据库，用于存储用户信息、商品信息、订单信息等数据。

**前端**：

**HTML/CSS/JavaScript**：实现页面布局与交互逻辑。

**Bootstrap**：快速构建响应式、适配移动设备的 Web 页面。

**jQuery**：简化 JavaScript 代码，实现页面动态效果支持。

## 四、部署与运行

**克隆项目**：在终端中运行以下命令，将项目克隆到您的设备：



```
git clone \[你的GitHub仓库链接]
```

**创建虚拟环境（可选）**：



```
python -m venv venv

source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
```

**安装依赖**：进入项目根目录，运行以下命令安装所需的 Python 包：



```
pip install -r requirements.txt
```

**配置数据库**：打开项目根目录下的`settings.py`文件，配置您的 MySQL 数据库连接信息：



```
DATABASES = {

&#x20;   'default': {

&#x20;       'ENGINE': 'django.db.backends.mysql',

&#x20;       'NAME': 'your\_database\_name',

&#x20;       'USER': 'your\_username',

&#x20;       'PASSWORD': 'your\_password',

&#x20;       'HOST': '127.0.0.1',

&#x20;       'PORT': '3306',

&#x20;   }

}
```

**迁移数据库**：在终端中运行以下命令，创建数据库表：



```
python manage.py makemigrations

python manage.py migrate
```

**运行项目**：在终端中运行以下命令启动 Django 开发服务器：



```
python manage.py runserver
```

**访问项目**：打开浏览器，输入`http://127.0.0.1:8000/`即可访问项目。

## 五、项目结构

shoppingproject/              # 项目根目录（自动生成，与项目同名）

├── shopping\_project/          # Django 配置目录（与项目同名）

│   ├── \_\_init\_\_.py        # 初始化文件（标识为 Python 包）

│   ├── settings.py        # 项目配置文件（重点修改此文件）

│   ├── urls.py            # 项目路由文件

│   ├── asgi.py            # ASGI 服务器入口

│   └── wsgi.py            # WSGI 服务器入口（Gunicorn 使用）

├── shop/                  # 应用目录（可自定义名称，如 app、products 等）

│   ├── \_\_init\_\_.py        # 初始化文件

│   ├── admin.py           # 后台管理配置

│   ├── apps.py            # 应用配置

│   ├── models.py          # 数据库模型

│   ├── tests.py           # 测试文件

│   ├── urls.py            # 应用路由文件

│   ├── views.py           # 视图函数

│   ├── forms.py           # 表单类（如商品上传表单）

│   ├── templates/          # 模板目录

│   │   └── shop/          # 应用模板目录（建议与应用同名）

│   │       ├── base.html  # 基础模板（所有页面继承）

│   │       ├── product\_list.html  # 商品列表页

│   │       ├── upload\_product.html  # 上传商品页

│   │       ├── about.html       # 关于我们页

│   │       └── contact.html     # 联系我们页

│   └── static/            # 静态文件目录（开发环境使用，生产环境由 collectstatic 收集）

│       └── css/

│           └── styles.css # 自定义 CSS 文件

├── staticfiles/           # 生产环境静态文件目录（由 collectstatic 生成）

├── media/                 # 媒体文件目录（用户上传文件，如商品图片）

├── venv/                  # 虚拟环境目录（部署时排除）

├── .gitignore             # Git 忽略文件（建议排除 venv、db.sqlite3 等）

├── manage.py              # Django 命令行工具

└── requirements.txt       # 依赖包列表（部署时使用）

## 六、贡献指南

如果你对项目感兴趣，欢迎参与贡献！你可以：

提交[Issue](https://github.com/[你的GitHub用户名]/[你的仓库名]/issues)反馈问题或提出建议。

提交[Pull Request](https://github.com/[你的GitHub用户名]/[你的仓库名]/pulls)修复问题或添加新功能。

在提交 Pull Request 前，请确保：

代码符合 PEP8 规范（Python 代码）和前端代码规范。

添加必要的注释和测试用例。

希望这个网上购物系统能为你的学习和开发带来帮助！如果觉得项目不错，别忘了给个 Star⭐哦！&#x20;