angular.module('MainApp', ['ui.router']);

angular.module('MainApp').config(function($interpolateProvider, $stateProvider, $urlRouterProvider, $locationProvider) {

    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');

    $urlRouterProvider.otherwise('/');

    $stateProvider


    // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
    .state('login', {
        url: '/login',
        templateUrl : 'static/js/login/template/loginTemplate.html'
    })

    // HOME STATES AND NESTED VIEWS ========================================
    .state('index', {
        url: '/',
        //controller: 'indexCtrl',
        templateUrl : 'static/js/index/template/indexTemplate.html'
    })

    // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
    .state('index.polls', {
        url: 'polls',
        controller: 'pollsController',
        templateUrl : 'static/js/polls/template/pollsTemplate.html'
    });

    $locationProvider.html5Mode(true);

})

.run(function ($state,$rootScope, $timeout,SocketService) {

    $rootScope.$state = $state;
    $rootScope.questionIndex = 0;

    $rootScope.emitState = function (state) {
        console.log('state emmiting', state);
        SocketService.sock.sendMessage({
            event : 'stateChange',
            previousState : $state.current.name,
            newState : state
        })
    };

    $rootScope.$on('clientInit', function (event, data) {
        console.log(data);
        console.log('yo homie!');
        $timeout(function (){
            $rootScope.questionIndex = data.questionIndex;
        });

        if(data.state !== $state.current.name){
            $state.go(data.state)
        }
    });

    $rootScope.$on('stateChange', function (event, data) {
        console.log('state change homie');
        $state.go(data.newState);
    });
});