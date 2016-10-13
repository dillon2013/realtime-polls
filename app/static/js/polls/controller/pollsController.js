angular.module('MainApp').controller('pollsController',
    function ($scope, pollsModel, $timeout, SocketService, $rootScope, $state) {

        $scope.questions = pollsModel;


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