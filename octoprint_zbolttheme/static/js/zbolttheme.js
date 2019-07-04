$(function() {

    function ZBoltViewModel(parameters) {
        var self = this;

        var faviconUrl = document.querySelector("link[rel~='mask-icon-theme']").href
        || link.href
        || window.location.origin + "/favicon.ico";

        console.log('test');
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBoltViewModel,
        // dependencies: ["AppearanceViewModel"],
        elements: ["head"]
    });



});


