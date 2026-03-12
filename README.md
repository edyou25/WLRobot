# WLRobot

## WERoot 文档（Sphinx + Read the Docs Theme）

文档源码位于 `docs/source`，已配置 `sphinx_rtd_theme`。

### 使用 conda 环境构建

```bash
conda run -n ielts-env sphinx-build -M html docs/source docs/build
```

生成网页目录：

```text
docs/build/html
```

### 本地部署（静态服务）

```bash
cd docs/build/html
python3 -m http.server 8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

说明：文档流程统一使用现有 `conda` 环境 `ielts-env`，不在仓库内创建额外 Python 虚拟环境。

### GitHub Pages 自动部署

仓库已配置 GitHub Actions 工作流：

```text
.github/workflows/pages.yml
```

触发条件：

```text
push 到 main 分支
```

注意：GitHub 仓库设置中的 Pages Source 需要改为 `GitHub Actions`，不要继续使用 `Deploy from a branch /docs`，因为当前 `docs/` 存放的是 Sphinx 源文件，不是最终 HTML。
