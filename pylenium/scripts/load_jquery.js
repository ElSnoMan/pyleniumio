(function(jqueryUrl, callback) {
    if (typeof jqueryUrl != 'string') {
        jqueryUrl = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js';
    }
    if (typeof jQuery == 'undefined') {
        let script = document.createElement('script');
        let head = document.getElementsByTagName('head')[0];
        let done = false;
        script.onload = script.onreadystatechange = (function() {
            if (!done && (!this.readyState || this.readyState === 'loaded'
                    || this.readyState === 'complete')) {
                done = true;
                script.onload = script.onreadystatechange = null;
                head.removeChild(script);
                callback();
            }
        });
        script.src = jqueryUrl;
        head.appendChild(script);
    }
    else {
        callback();
    }
})(arguments[0], arguments[arguments.length - 1]);
