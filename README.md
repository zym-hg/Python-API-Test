# Python-API-Test
基于 Python + Pytest 的公开 API 自动化测试项目。

## 项目简介
本项目使用 Python 语言，结合 Requests 库和 Pytest 框架，对公开的 API 接口进行自动化测试验证。
测试内容包括：
1. 正向用例：验证接口连通性、HTTP 状态码（200）及返回 JSON 数据的关键字段。
2. 反向用例：验证异常请求下的接口处理机制。

## 技术栈
*   Python 3
*   Requests 库
*   Pytest 框架

## 运行方式
1. 安装依赖：`pip install requests pytest`
2. 运行测试用例：`pytest test_api_pytest.py`

## 测试结果
在控制台执行后，Pytest 将自动运行 2 个测试用例（包含正向与反向），并输出 PASS 结果。
