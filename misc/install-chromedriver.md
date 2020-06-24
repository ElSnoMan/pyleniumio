---
description: This is NO LONGER NEEDED in version 1.4.1+
---

# Install chromedriver

{% hint style="danger" %}
Pylenium installs these for you automatically! YOU DO NOT NEED TO DO THIS!
{% endhint %}

## Options

There are many ways to install the driver executables needed to work with Selenium. This document will go over some of them, but use the one that works for you:

* **`Chocolatey`** - Package Manager for Windows
* **`Homebrew`** - Package Manager for Mac
* **`webdriver-manager`** - A great tool to manage drivers for any OS
* **`Manual Installation`** - worst-case scenario, you can always install them manually

{% hint style="info" %}
In a future release, we will take care of this step for you :\)
{% endhint %}

## The driver must be on your PATH

Pylenium will only look for drivers that exist on your PATH. There are multiple ways to do this, so this doc will break down the most common.

{% hint style="success" %}
You can skip this step if you already have the drivers on your PATH
{% endhint %}

## Chocolatey

If you are on Windows, you can use the **Chocolatey** package manager by going to their installation page:

{% embed url="https://chocolatey.org/docs/installation" %}

{% hint style="warning" %}
Follow the instructions for your Terminal of choice: **Command Prompt** or **Powershell**
{% endhint %}

### Install chromedriver

1. Go to the installation page and copy the Command for your Terminal
2. Open your Terminal in **Administrative Mode**
3. Paste the command and execute it
4. Close the Terminal and re-open it
5. Install chromedriver

{% code title="Terminal" %}
```bash
choco --version
# 0.10.15

choco install chromedriver
# accept any prompts and choco will print where it was installed

chromedriver --version
# ChromeDriver 80.0.3987.106
```
{% endcode %}

### Add to PATH

Copy the file path where **choco** installed the chromedriver and set it in your PATH. The following link shows how you can manually add a directory to your PATH.

{% embed url="https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/" %}

{% hint style="warning" %}
After editing your PATH, restart your IDE and Terminals for the new PATH to register
{% endhint %}

## Homebrew

If you are on MacOS, you can the use the **Homebrew** package manager by going to their installation page:

{% embed url="https://brew.sh/" %}

### Install chromedriver

1. Run the script and follow the prompts
2. Install chromedriver

{% code title="Terminal" %}
```bash
brew cask install chromedriver
```
{% endcode %}

### Add to PATH

{% hint style="success" %}
brew automatically install it to your `/usr/local/bin` directory which is _already_ on your PATH
{% endhint %}

## webdriver-manager

This is a **Node** module that installs and manages different drivers. You will need [Node.js](https://nodejs.org/en/download/) installed to use this, but it works for both **Windows** and **MacOS**, making it a crowd favorite.

{% embed url="https://www.npmjs.com/package/webdriver-manager" %}

### Install chromedriver

```bash
webdriver-manager update --output_dir="file-path"
```

### Add to PATH

This doesn't automatically add it to your path, so take note where the **chromedriver** was saved so you can manually add it.

## Manual Installation

Worst-case scenario, you can always install the drivers manually.

### Install chromedriver

1. Click on the link below to go to Chrome's downloads
2. Click on the version that you want
3. Download the chromedriver

{% embed url="https://sites.google.com/a/chromium.org/chromedriver/downloads" %}

### Add to PATH

You can either copy and paste the chromedriver to a directory that is **already** on the PATH, or you can add a folder to the PATH as well. Here is a helpful doc:

{% embed url="https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/" %}

{% hint style="warning" %}
After editing your PATH, restart your IDE and Terminals for the new PATH to register
{% endhint %}

