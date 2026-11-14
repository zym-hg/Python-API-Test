# Python-API-Test
基于 Python + Requests 的公开 API 接口自动化测试验证项目。

## 项目简介
使用 Python 的 `requests` 库对公开天气 API 接口进行自动化测试。
包含对 HTTP 状态码的断言（是否为200），以及对响应 JSON 数据中关键业务字段（如 IP、地区）的校验。

## 技术栈
*   Python 3
*   Requests 库

## 运行方式
1. 安装依赖：`pip install requests`
2. 运行脚本：`python first_test.py`

## 测试结果
运行脚本后，控制台将自动打印接口返回结果，并输出测试通过（PASS）或失败（FAIL）的结论。
