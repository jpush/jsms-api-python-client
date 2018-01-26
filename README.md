# JSMS API PYTHON CLIENT

这是短信 API 的 Python 版本封装开发包，是由极光官方提供的，一般支持最新的 API 功能。支持 Python 2.7 和 Python 3 常见版本。

对应的 API 文档：https://docs.jiguang.cn/jsms/server/rest_api_summary/

## Installing

```bash
$ pip install jsms
```

## Usage

### 初始化

```python
import jsms
jsms_client = jsms.Jsms(app_key, master_secret)
```

### 发送验证码

```python
jsms_client.send_code(mobile, temp_id)
```

**参数说明:**

> mobile: 接收验证码的手机号码

> temp_id: 模板ID

### 发送语音短信验证码

```python
jsms_client.send_voice_code(mobile, code=None, lang=None, ttl=None)
```

**参数说明:**

> mobile: 接收验证码的手机号码

> ttl: 超时时间，默认为 60 秒

> code: 语音验证码的值，验证码仅支持 4-8 个数字

> lang: 播报语言选择，0：中文播报，1：英文播报，2：中英混合播报

### 验证

```python
jsms_client.verify_code( msg_id, code);
```

**参数说明:**

> msg_id: 发送验证码 `send_code/send_voice_code` 函数返回的数组中的 msg_id 键对应的值

> code: 手机接收到的验证码

### 发送模板短信

```python
jsms_client.send_teml(mobile, temp_id, temp_para=None, time=None)
```

**参数说明:**

> mobile: 接收验证码的手机号码

> temp_id: 模板 ID

> temp_para: 模板参数，需要替换的参数名和 value 的键值对，接受一个 dict

> time: 定时短信发送时间，格式为 yyyy-MM-dd HH:mm:ss，默认为 `None` 表示立即发送

### 查询定时模板短信

```python
jsms_client.show_schedule_message(schedule_id)
```

### 删除定时模板短信

```python
jsms_client.delete_schedule_message(schedule_id)
```

### 应用余量查询

```python
jsms_client.app_balance()
```

### 调用返回码说明

https://docs.jiguang.cn/jsms/server/rest_api_summary/#_1

## Example

在项目的 [examples](https://github.com/jpush/jsms-api-python-client/tree/master/examples) 文件夹有简单示例代码, 开发者可以参考其中的样例快速了解该库的使用方法。

### 简单使用方法

- 编辑 context.py 文件，填写信息

```python
jsms_client = jsms.Jsms('xxxx', 'xxxx')
mobile = 'xxxxxxxxxxx'
```

- 运行示例

```bash
$ python examples/sms.py text_code
$ python examples/sms.py voice_code
$ python examples/sms.py tmpl_task
$ python examples/sms.py blance
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jsms-api-python-client.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
