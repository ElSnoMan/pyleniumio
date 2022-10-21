FROM gitpod/workspace-full-vnc

USER root

# RUN apt-get update -qqy && apt-get install -y wget curl gnupg2

# So we can install browsers and browser drivers later
RUN wget https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb && rm packages-microsoft-prod.deb
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN mkdir -p /home/gitpod/selenium /var/run/supervisor /var/log/supervisor && \
    chmod -R 777 /var/run/supervisor /var/log/supervisor

ENV DEBIAN_FRONTEND=noninteractive

# Browsers
RUN apt-get update -qqy && \
    apt-get -qy install google-chrome-stable firefox && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Browser Drivers
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
    && echo "Using ChromeDriver version: "$CHROME_DRIVER_VERSION \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && rm -rf /home/gitpod/selenium/chromedriver \
    && unzip /tmp/chromedriver_linux64.zip -d /home/gitpod/selenium \
    && rm /tmp/chromedriver_linux64.zip \
    && mv /home/gitpod/selenium/chromedriver /home/gitpod/selenium/chromedriver-$CHROME_DRIVER_VERSION \
    && chmod 755 /home/gitpod/selenium/chromedriver-$CHROME_DRIVER_VERSION \
    && sudo ln -fs /home/gitpod/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver
RUN GK_VERSION="0.31.0" \
    && echo "Using GeckoDriver version: "$GK_VERSION \
    && wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GK_VERSION/geckodriver-v$GK_VERSION-linux64.tar.gz \
    && rm -rf /home/gitpod/selenium/geckodriver \
    && tar -C /home/gitpod/selenium -zxf /tmp/geckodriver.tar.gz \
    && rm /tmp/geckodriver.tar.gz \
    && mv /home/gitpod/selenium/geckodriver /home/gitpod/selenium/geckodriver-$GK_VERSION \
    && chmod 755 /home/gitpod/selenium/geckodriver-$GK_VERSION \
    && ln -fs /home/gitpod/selenium/geckodriver-$GK_VERSION /usr/bin/geckodriver

# To run browser tests
ENV DISPLAY :99.0
ENV DISPLAY_NUM 99
ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24
ENV SCREEN_DPI 96
ENV VNC_PORT 5900
ENV NO_VNC_PORT 7900
