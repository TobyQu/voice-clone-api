# 贡献指南

感谢您对声音复刻 API 项目的兴趣！我们欢迎各种形式的贡献，包括但不限于代码贡献、文档改进、问题报告和功能请求。

## 如何贡献

### 报告问题

如果您发现了问题或者有改进建议，请通过 GitHub 的 Issues 功能提交，并包含以下信息：

1. 问题的简短描述
2. 问题发生的环境（操作系统、Python 版本等）
3. 重现问题的步骤
4. 预期行为和实际行为
5. 相关的错误消息和日志

### 提交代码

1. Fork 这个仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

### 代码审查

所有提交的代码都将经过审查。为了加快审查过程：

- 确保代码符合项目的编码风格
- 为新功能添加测试
- 保持更改的范围尽可能小
- 撰写清晰的提交消息

## 开发指南

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/yourusername/voice-clone-api.git
cd voice-clone-api

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows 使用: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt
```

### 代码风格

我们使用 [black](https://github.com/psf/black) 和 [isort](https://github.com/PyCQA/isort) 来格式化代码，使用 [flake8](https://github.com/PyCQA/flake8) 进行代码检查：

```bash
# 格式化代码
black app tests
isort app tests

# 代码检查
flake8 app tests
```

### 测试

添加新功能时，请务必添加对应的测试。运行测试：

```bash
pytest tests/
```

对于提交到主分支的代码，所有测试必须通过。

## 文档贡献

文档是项目的重要组成部分。如果您发现文档中有错误或者您想改进文档，欢迎提交 PR。

## 版本控制与发布

我们使用 [语义化版本控制](https://semver.org/)。如果您的贡献将更改 API 或添加重要功能，请在 CHANGELOG.md 中记录这些更改。

## 行为准则

请参阅 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 了解我们社区的行为准则。

## 许可证

通过贡献代码，您同意您的贡献将在项目的 [LICENSE](LICENSE) 下发布。 