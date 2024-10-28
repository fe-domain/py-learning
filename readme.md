# START PROJECT

- pipenv 自动创建和管理项目的虚拟环境，在 安装/卸载 软件包时从 Pipfile 添加/删除软件包， 也会自动生成 Pipfile.lock 保证项目的依赖可靠性

pip install sauron
sauron pname.py

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
    python -m venv /Users/jakequc/Desktop/learn-codes/py-learning
    source /Users/jakequc/Desktop/learn-codes/py-learning/bin/activate
    python -m pip install package-name

    # deactivate 退出虚拟环境
```

### create virtualenv[推荐]
pip install virtualenv
pyenv shell 3.8.18  # 切换到特定版本
virtualenv venv    # 创建虚拟环境
source venv/bin/activate #激活虚拟环境



### install pytorch
https://pytorch.org/
pipenv install torch torchvision torchaudio


### re 正则
. 匹配人意换行符 \n 外的字符
* 前面的字符出现 0 次或以上
? 表示前面的符号出现 0 次或 1 次
.* 贪婪匹配，匹配从 .* 前面为开始到最后结束的所有内容
*? 非贪婪，遇到开始和结束就进行截取，因此截取多次符合的结果，中间没有字符也会被截取
(.*?) 非贪婪，与上面一样，只是只保留括号的内容