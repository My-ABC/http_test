# http_test

[中文文档](README-zh.md) | [English Documentation](README.md)

## 项目简介
这是一个用于测试 HTTP 协议的项目。

## 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/My-ABC/http_test.git
   ```
2. 进入项目目录：
   ```bash
   cd http_test
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行项目：
   ```bash
   python http.py
   ```

5. 在浏览器中访问 `http://127.0.0.1:81`，你将看见结果或者
   在浏览器中访问 `http://127.0.0.1:81/a`，你将看见结果或者
   在浏览器中访问 `http://127.0.0.1:81/a/b.html`，你将看见结果或者
   在浏览器中访问 `http://127.0.0.1:81/a/c.html`，你将看见结果

## 使用说明
1. 在 `http.py` 文件中，你可以看到 `handle_client` 函数，该函数用于处理客户端请求。