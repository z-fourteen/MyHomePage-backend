# MyHomePage-backend

这是一个基于 Django 的后端项目，为你的个人主页或相关应用提供 API 支持。

## 项目结构

- `backend/`：Django 后端主目录
- `api/`：API 相关模块
- `db.sqlite3`：默认 SQLite 数据库文件
- `manage.py`：Django 管理脚本
- `requirements.txt`：Python 依赖包列表

## 快速开始

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/z-fourteen/MyHomePage-backend.git
   ```
2. 进入项目目录并创建虚拟环境：
   ```bash
    cd backend
    python -m venv env
    source env/bin/activate  # Linux/macOS
    .\env\Scripts\activate   # Windows
    ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行Django项目：
   ```bash
    python manage.py migrate
    python manage.py runserver
   ```