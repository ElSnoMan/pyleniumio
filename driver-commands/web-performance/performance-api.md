---
description: Pylenium's custom performance API to capture different metrics.
---

# Performance API

## Syntax

```python
py.performance -> Performance
py.performance.get() -> WebPerformance
```

## Usage

The <mark style="color:orange;">**Performance**</mark>** ** class is where everything lives. It provides access to the following methods:

### WebPerformance

The main method used to generate a <mark style="color:orange;">**WebPerformance**</mark> object from the current web page. This is really all you need from this API and will be discussed in more detail [further below in Metrics](performance-api.md#metrics).

{% hint style="danger" %}
Calling this method too soon may yield NoneTypes because the browser hasn't generated them yet.
{% endhint %}

```python
py.performance.get() -> WebPerformance
```

### Time Origin

Return the <mark style="color:yellow;">**timeOrigin**</mark> precision value. This is the high-resolution timestamp of the start time of the performance measurement.

```python
py.performance.get_time_origin() -> float
```

### Navigation Timing

Return the <mark style="color:yellow;">**PerformanceNavigationTiming**</mark> W3 object as a Python object called <mark style="color:orange;">**NavigationTiming**</mark>.

```python
py.performance.get_navigation_timing() -> NavigationTiming
```

### Paint Timing

Return the <mark style="color:yellow;">**PerformancePaintTiming**</mark> object as a Python object called <mark style="color:orange;">**PaintTiming**</mark>.

```python
py.performance.get_paint_timing() -> PaintTiming
```

### Resources

Return a list of <mark style="color:yellow;">**PerformanceResourceTiming**</mark> objects as Python objects called <mark style="color:orange;">**\[ResourceTiming]**</mark>.

```python
py.performance.get_resources() -> List[ResourceTiming]
```

## Metrics

All of the timing objects include A LOT of data points, but many of them may not be useful.

{% hint style="info" %}
If you want to see ALL the data points, take a look at [the file in the GitHub Repo](https://github.com/ElSnoMan/pyleniumio/blob/main/pylenium/performance.py)
{% endhint %}

This is why the <mark style="color:orange;">**WebPerformance**</mark> object exists! It contains calculations for metrics that have been very useful when we talk about and measure web performance. After navigating to a website and capturing these metrics with <mark style="color:purple;">`py.performance.get()`</mark>, we can do whatever we want with them!

With a few lines of code, you have access to many valuable metrics:

```python
# perf will be used in the examples below
py.visit("https://your-website.com")
perf = py.performance.get()
```

### Page Load Time

The time it takes for the page to load as experienced by the user.

```python
perf.page_load_time() -> float
```

### Time to First Byte

The time it takes before the first byte of response is received from the server.

```python
perf.time_to_first_byte() -> float
```

### Time to First Contentful Paint

The time it takes for the majority of content to be fully rendered and consumable by the user.

```python
perf.time_to_first_contentful_paint() -> float
```

### Time to Interactive (TTI)

The time it takes for the layout to be stabilized and the page is responsive.

```python
perf.time_to_interactive() -> float
```

### Number of Requests

The number of requests sent from start of navigation until end of page load.

```python
perf.number_of_requests() -> int
```

### Time to DOM Content Loaded

The time it takes for the DOM content to load.

```python
perf.time_to_dom_content_loaded() -> float
```

### Page Weight

The amount of bytes transferred for the page to be loaded.

```python
perf.page_weight() -> float
```

### Connection Time

The time taken to connect to the server.

```python
perf.connection_time() -> float
```

### Request Time

The time taken to send a request to the server and receive the response.

```python
perf.request_time() -> float
```

### Fetch Time

The time to complete the document fetch (including accessing any caches, etc.).

```python
perf.fetch_time() -> float
```

## Examples

Store the entire <mark style="color:orange;">**WebPerformance**</mark> object in a variable, then convert it to a <mark style="color:yellow;">**Dictionary**</mark> to log it.

```python
perf = py.performance.get()
py.log.info(perf.dict())
```

Store a single data point in a variable and test against it.

```python
tti = py.performance.get().time_to_interactive()
assert tti < BASELINE, f"TTI should be less than our baseline."
```

