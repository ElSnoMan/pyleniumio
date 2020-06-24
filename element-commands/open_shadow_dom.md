---
description: The command to open/expand a Shadow DOM element.
---

# open\_shadow\_dom

## Syntax

```python
Element.open_shadow_dom()
```

## Usage

Shadow DOMs are a bit tricky because, like iframes, you need to "switch" to its context to find elements or objects within it. Check out this example using `chrome://extensions`:

```python
def test_loading_extension_to_browser(py):
    py.visit('chrome://extensions/')
    shadow1 = py.get('extensions-manager').open_shadow_dom()
    shadow2 = shadow1.get('extensions-item-list').open_shadow_dom()
    extension_shadow_dom = shadow2.find('extensions-item')[1].open_shadow_dom()
    assert extension_shadow_dom.get('#name-and-version').should().contain_text('Get CRX')
```

## Yields

* `The Shadow Root (Element)`. With this element you can search for things within the Shadow context.

