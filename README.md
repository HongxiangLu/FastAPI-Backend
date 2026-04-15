# FastAPI 移动端展品管理后端原型

这是一个基于 FastAPI 开发的极简、轻量级后端项目，专为移动端应用提供数据接口。它支持文字描述、本地图片和视频资源的存储与访问。

## 🚀 项目特性

*   **轻量级架构**：使用 SQLite 数据库，无需额外配置数据库服务。
*   **极致开发体验**：基于 SQLModel (SQLAlchemy + Pydantic)，代码简洁，类型安全。
*   **多媒体支持**：图片和视频直接存储在本地磁盘，通过静态文件服务高速访问。
*   **移动端友好**：RESTful 设计，自动生成交互式 API 文档 (Swagger UI)。
*   **局域网共享**：配置为监听 `0.0.0.0`，方便同一 Wi-Fi 下的移动设备直接连接测试。

## 🛠️ 技术栈

*   **核心框架**: FastAPI
*   **数据库 ORM**: SQLModel (SQLite)
*   **Web 服务器**: Uvicorn
*   **环境管理**: Conda

## 📁 项目结构

```text
FastAPI-Backend/
├── app/
│   ├── api/
│   │   └── exhibits.py     # 展品相关 API 接口 (CRUD)
│   ├── database.py         # 数据库连接与会话管理
│   ├── models.py           # SQLModel 数据模型 (Exhibit)
│   └── main.py             # 程序入口 & 静态文件挂载
├── media/                  # 📂 本地多媒体存储目录
│   ├── images/             # 存放展品图片
│   └── videos/             # 存放展品视频
├── environment.yml         # Conda 环境依赖配置
├── database.db             # SQLite 数据库文件 (运行时自动生成)
└── README.md               # 项目说明文档
```

## 🛠️ 快速开始

### 1. 环境准备 (Conda)

在项目根目录下，使用 Conda 创建并激活环境：

```bash
# 创建环境
conda env create -f environment.yml

# 激活环境
conda activate fastapi
```

### 2. 运行项目

你可以使用以下任一方式启动后端服务：

**方式 A：直接运行 Python 模块 (推荐)**
```bash
python -m app.main
```

**方式 B：使用 Uvicorn 命令**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

启动后，访问 `http://<服务器IP>:8000/` 即可看到欢迎消息。

## 📖 API 使用说明

### 1. 交互式文档
访问 [http://<服务器IP>:8000/docs](http://<服务器IP>:8000/docs) 查看并测试所有 API。

### 2. 核心接口
*   **获取展品列表**: `GET /exhibits/` (支持 `skip` 和 `limit` 分页参数)
*   **创建新展品**: `POST /exhibits/`
    *   请求体示例：
        ```json
        {
          "title": "展品名称",
          "content": "展品详细描述文字",
          "image_url": "media/images/example.jpg",
          "video_url": "media/videos/example.mp4"
        }
        ```

### 3. 多媒体资源访问
本项目已将 `media/` 文件夹挂载为静态目录。
*   **图片访问路径**: `http://<服务器IP>:8000/media/images/文件名.jpg`
*   **视频访问路径**: `http://<服务器IP>:8000/media/videos/文件名.mp4`

## 📱 移动端连接指南

为了让同一 Wi-Fi 下的手机访问后端：
1.  确保电脑防火墙允许 8000 端口通过。
2.  在电脑终端输入 `ipconfig` 找到你的局域网 IP (如 `192.168.1.5`)。
3.  在移动端应用中，将 API 基础地址设置为 `http://<服务器IP>:8000`。

## 📜 Git Commit 规范

本项目参考 [Conventional Commits](https://www.conventionalcommits.org/) 约定式提交规范，建议提交格式如下：

`<type>: <description>`

### 常用 Type 类型：
*   **feat**: 引入新功能
*   **fix**: 修复 Bug
*   **docs**: 仅文档改动 (如 README.md)
*   **style**: 不影响代码含义的改动 (空格、格式化、缺失分号等)
*   **refactor**: 代码重构 (既不是修复 Bug 也不是引入新功能)
*   **perf**: 提高性能的改动
*   **test**: 添加或修正测试用例
*   **chore**: 构建过程或辅助工具的变动 (如更新 Conda 环境)

### 示例：
*   `feat: 增加展品视频存储支持`
*   `fix: 修复展品模型字段类型错误`
*   `docs: 更新部署文档`

## ⚠️ 开发注意事项
*   **数据库迁移**：由于是轻量原型，如修改了 `models.py` 中的字段，请删除 `database.db` 后重新运行，程序会自动重建表结构。
