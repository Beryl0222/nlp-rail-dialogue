# 铁路咨询的多意图理解与对话修复

这是面向可训练多意图槽位理解的Python项目资料。现有内容提供本地合成输入、数据约定及资料检查入口，业务操作入口尚未提供。

## 运行环境

Python 3.11。依赖版本锁在 requirements.txt。可在已准备的环境中运行 `python3 -m unittest discover -s tests -v` 检查资料，`python3 -m support.inspect_data` 查看材料数量。两项命令仅验证现有输入，不能证明业务处理已完成。

容器用法：`docker build -t rail-dialogue .` 后执行 `docker run --rm rail-dialogue`。业务能力开发后，应把使用方法与相应检查补充到本说明中。

## 现有材料

`data`保存原始记录和必要的人工例子；[数据约定](docs/资料格式.md)解释字段。`support`只负责资料读取，`tests`验证文件引用与原文区间，不提供业务推断。输入可以替换为同格式记录。
