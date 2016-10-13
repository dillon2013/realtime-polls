angular.module('MainApp').service('SocketService', function ($rootScope) {
    var self = this;
    var recInterval = null;

    var newCon = function () {
        self.sock = new SockJS('http://localhost:8888/ws', null, {sessionId:20});

        clearInterval(recInterval);

        self.sock.onopen = function() {
            console.log(self.sock);
        };

        self.sock.onmessage = function(e) {
            self.data = e;
            console.log(e.data.event+':', e.data);
            var event = e.data.event;
            $rootScope.$emit(event, e.data);
        };

        self.sock.onclose = function() {
            self.sock = null;
            recInterval = setInterval(function() {
                newCon();
            }, 2000);
        };

        self.sock.sendMessage = function (msg) {
            var message = JSON.stringify(msg);
            self.sock.send(message);
        };
    };

    newCon();

});