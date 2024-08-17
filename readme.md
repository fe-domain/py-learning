# START PROJECT

- pipenv 自动创建和管理项目的虚拟环境，在 安装/卸载 软件包时从 Pipfile 添加/删除软件包， 也会自动生成 Pipfile.lock 保证项目的依赖可靠性

### install way1
```
    pip install pipenv
    pipenv shell
    pipenv install third-package
    pipenv run pytest

```

### install way2
```
    $envPath = pwd
    python3 -m venv /Users/jakequc/Desktop/ai-sets/py-learning
    source /Users/jakequc/Desktop/ai-sets/py-learning/bin/activate
    python3 -m pip install package-name
```

### install pytorch
https://pytorch.org/
pipenv install torch torchvision torchaudio
