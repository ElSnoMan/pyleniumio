# Run Tests in Containers

## Configure the Test Run

Regardless of the scaling option you go with \(Selenoid, Zalenium, Docker vs Kubernetes, etc.\), you will need to connect your tests to a **Remote URL.**

You can do this two ways:

* Update **remote\_url** in ****`pylenium.json`
* Pass in the argument when running the tests in the CLI

### Run Tests in CLI

{% hint style="info" %}
This is the most common option since it is what you will use in your pipelines and CI
{% endhint %}

{% code title="Terminal $ \(venv\) \# example" %}
```bash
python -m pytest tests/ui -n 2 --remote_url="http://localhost:4444/wd/hub"
```
{% endcode %}

### Update pylenium.json

{% hint style="info" %}
This option is great for local development and debugging
{% endhint %}

{% code title="pylenium.json" %}
```bash
"remote_url": "http://localhost:4444/wd/hub"
```
{% endcode %}

### Config Layers

* Layer 1 - `pylenium.json` is deserialized into **PyleniumConfig**
* Layer 2 - If there are any CLI args, they will override their respective values in **PyleniumConfig**

## Docker Example

With **Docker** installed, you can easily spin up a **Selenium Grid** with the `docker-compose` command.

### docker-compose.yml

You will need a `docker-compose.yml` file and then open a Terminal in the same directory as this file.

{% code title="docker-compose.yml" %}
```yaml
version: "3"
services:

  selenium-hub:
    image: selenium/hub
    ports:
      - "4444:4444"
    environment:
        GRID_MAX_SESSION: 16
        GRID_BROWSER_TIMEOUT: 300
        GRID_TIMEOUT: 300

  chrome:
    image: selenium/node-chrome
    depends_on:
      - selenium-hub
    environment:
      HUB_PORT_4444_TCP_ADDR: selenium-hub
      HUB_PORT_4444_TCP_PORT: 4444
      NODE_MAX_SESSION: 2
      NODE_MAX_INSTANCES: 2

  firefox:
    image: selenium/node-firefox
    depends_on:
      - selenium-hub
    environment:
      HUB_PORT_4444_TCP_ADDR: selenium-hub
      HUB_PORT_4444_TCP_PORT: 4444
      NODE_MAX_SESSION: 4
      NODE_MAX_INSTANCES: 4
```
{% endcode %}

This configuration will spin up a **Hub** node \(load balancer\), a **Chrome** node with 2 available drivers and a **Firefox** node with 4 available drivers.

### Spin up the Grid

With a single command you will have all of this created for you:

{% code title="Terminal $" %}
```bash
docker-compose up -d
```
{% endcode %}

{% hint style="info" %}
Once complete, you can visually see these Grid by going to [http://localhost:4444/grid/console](http://localhost:4444/grid/console)
{% endhint %}

Now **Configure the Test Run** \(steps at top of this doc\) to target the Hub which will balance the tests across its Nodes.

### Scale Nodes

With the YAML file example above, it will create 1 chrome Node with 2 available drivers by default. You can easily scale this to the number you need.

{% code title="Terminal $" %}
```bash
docker-compose up -d --scale chrome=5
```
{% endcode %}

This will spin up the Grid with 5 chrome Nodes!

### Tear Down the Grid

When you're done using the Grid, a single command will tear it completely down.

{% code title="Terminal $" %}
```bash
docker-compose down
```
{% endcode %}

