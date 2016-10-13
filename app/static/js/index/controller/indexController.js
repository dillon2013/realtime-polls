angular.module('MainApp').controller('indexCtrl',
    function ($scope, questionsModel, $timeout, SocketService, $rootScope, $state) {

    $scope.questionIndex = 0;
    $scope.questions = questionsModel;

    $rootScope.$on('clientInit', function (event, data) {
        $timeout(function (){
            $scope.questionIndex = data.questionIndex;
        });

        //console.log($state.current.name);

        if(data.state !== $state.current.name){
            $state.go(data.state)
        }
    });

    $scope.clickNext = function () {
        var message = {event: 'nextQuestion', questionIndex : $scope.questionIndex};
        SocketService.sock.sendMessage(message);
    };

    $scope.clickPrevious = function () {
        var message = {event: 'previousQuestion', questionIndex : $scope.questionIndex};
        SocketService.sock.sendMessage(message);
    };


    $rootScope.$on('nextQuestion', assignIndex);
    $rootScope.$on('previousQuestion', assignIndex);
    $rootScope.$on('stateChange', function (event, data) {
        console.log(data);
       $state.go(data.newState);
    });

    function assignIndex(event, data) {
        $timeout(function (){
            $scope.questionIndex = data.questionIndex;
        });
    }

    $scope.submitAnswer = function (questionIndex, answerIndex) {
        console.log(questionIndex, answerIndex);
    };

    $scope.selectAnswer= function (index) {
        console.log('selected answer is: ', index);
        $scope.answerIndex = index;
    };


    $rootScope.$on('chatting', function (event, data) {

    });

    $rootScope.$on('serverMessage', function (event, data) {

    });

});