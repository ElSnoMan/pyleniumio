---
description: >-
  Pylenium, for Chrome and Firefox, allows you to capture and interact Network
  Requests
---

# Inspect Network Requests

{% code title="test_network_reqs.py" %}
```python
def test_clicking_about_sends_RecordHit_request(py: Pylenium):
    py.visit("https://qap.dev")

    # Click About should send a request to /RecordHit
    py.get("a[href='/about']").click()
    request = py.webdriver.wait_for_request("/api/census/RecordHit")

    # Do things with request (like assert!)
    assert request.method == "POST"
    assert request.response.status_code == 200
    assert request.url == "https://www.qap.dev/api/census/RecordHit"
```
{% endcode %}
