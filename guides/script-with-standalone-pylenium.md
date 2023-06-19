---
description: How to use Pylenium in a regular script instead of in a test
---

# 🌐 Script with Standalone Pylenium

## Setup

Pylenium needs two things in order to be instantiated:

* <mark style="color:orange;">**PyleniumConfig**</mark>
* <mark style="color:orange;">**Pylenium**</mark>

Create a `main.py` file and add the necessary imports:

{% code title="main.py" %}
```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig
```
{% endcode %}

### Create an instance of PyleniumConfig

Start by creating an instance of PyleniumConfig. Leaving it blank will create a config with default values. **NOTE**: This _<mark style="color:red;">does not</mark>_ use <mark style="color:yellow;">**`pylenium.json`**</mark>

{% code title="Default config" %}
```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

config = PyleniumConfig()
```
{% endcode %}

To use <mark style="color:yellow;">**`pylenium.json`**</mark>, you'd have to read the file first:

{% code title="Use pylenium.json" %}
```python
import json
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

with open("pylenium.json") as file:
    pylenium_json = json.load(file)

config = PyleniumConfig(**pylenium_json)
```
{% endcode %}

You can set config values directly in the script - mixing and matching as needed

```python
import json
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

with open("pylenium.json") as file:
    pylenium_json = json.load(file)

config = PyleniumConfig(**pylenium_json)
config.browser = "firefox"
```

### Create an instance of Pylenium

Once the config is ready, instantiate Pylenium with it:

```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

config = PyleniumConfig()
py = Pylenium(config)
```

## Write your Script

You now have access to Pylenium's many commands to script what you need:

{% code title="Google Search" %}
```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

config = PyleniumConfig()
py = Pylenium(config)

py.visit("https://google.com")
py.get("[name='q']").type("pylenium.io\n")
py.should().contain_title("pylenium.io")
py.quit()
```
{% endcode %}

## Run your Script

Use python to execute `main.py`

```bash
python main.py
```

