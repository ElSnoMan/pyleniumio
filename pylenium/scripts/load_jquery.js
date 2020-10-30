(function(jqueryUrl, iframe, callback) {
    if (typeof jqueryUrl != 'string') {
        jqueryUrl = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js';
    }

    function insertJquery(doc) {
        if (typeof jQuery == 'undefined') {
            let script = doc.createElement('script');
            let head = doc.getElementsByTagName('head')[0];
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
    }

    if (iframe != null) {
        let context = iframe.contentDocument;
        insertJquery(context);
    }
    else {
        insertJquery(document)
    }
})(arguments[0], arguments[1], arguments[arguments.length - 1]);
