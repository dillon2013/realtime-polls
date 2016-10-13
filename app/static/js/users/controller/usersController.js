angular.module('MainApp').controller('usersCtrl', function ($scope, $http) {
    $scope.test = 'Dillon';

    var ws = new WebSocket("ws://localhost:8888/ws");
    ws.onopen = function() {
        ws.send("Hello, world");
    };
    ws.onmessage = function (evt) {
        alert(evt.data);
    };

    $http({
        method : "GET",
        url : "/api/users"
    }).then(function mySucces(response) {
        $scope.users = response.data.users;
        console.log(response.data);
    }, function myError(response) {
        console.log(response)
    });
});