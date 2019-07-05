$(function() {

    function ZBConnectionViewModel(parameters) {
        var self = this;

        // var faviconUrl = document.querySelector("link[rel~='mask-icon-theme']").href
        // || link.href
        // || window.location.origin + "/favicon.ico";


        self.onAfterBinding = function() {
            var connection = $("#sidebar_plugin_klipper");
            connection.collapse("hide");
         }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBConnectionViewModel,
        dependencies: ["connectionViewModel"]
    });


    function ZBStateViewModel(parameters) {
        var self = this;
        
        self.printerStateViewModel = parameters[0];

        self.printerStateViewModel.stateString.subscribe(function(p){
            var s = $('#state_wrapper');

            if (p == 'Printing') {
                s.addClass('printing')
            } else {
                s.removeClass('printing')
            }
        });

        self.onAfterBinding = function() {
        }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBStateViewModel,
        dependencies: ["printerStateViewModel"]
    });





});


