# mikrotik-cn-ip-list

一个用于生成 MikroTik 中国大陆 IPv4 地址列表脚本的小仓库。

脚本会从远程规则源下载 `cnip.json`，提取其中的 IPv4 网段，并生成可直接导入 MikroTik 的 `address-list` 脚本。

## 功能

- 自动下载最新中国大陆 IP 数据
- 过滤掉 IPv6 地址
- 生成 MikroTik RouterOS 可用的 `.rsc` 脚本
- 输出为 `CN` 地址列表

## 目录结构

```text
build_ip_address/
  main.py
README.md
LICENSE
```

## 环境要求

- Python 3.10+
- `httpx`

## 安装依赖

```bash
pip install httpx
```

如果你的环境里 `pip` 不可用，也可以使用：

```bash
py -m pip install httpx
```

## 使用方法

在项目目录中运行：

```bash
py build_ip_address/main.py
```

运行后会生成：

```text
cn_ipv4_script.rsc
```

## 生成内容示例

生成的脚本会包含类似下面的内容：

```routeros
/log info "Loading CN ipv4 address list"
/ip firewall address-list remove [/ip firewall address-list find list=CN]
/ip firewall address-list
:do { add address=1.0.1.0/24 list=CN } on-error={}
```

## 数据来源

当前使用的数据源：

- `https://github.com/DustinWin/ruleset_geodata/releases/download/sing-box-ruleset/cnip.json`

## 说明

- 当前脚本只保留 IPv4 地址段
- 导出的地址列表名称为 `CN`
- 输出文件会写到脚本运行时的当前工作目录

## License

MIT
