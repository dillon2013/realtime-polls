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
        controller: 'indexCtrl',
        templateUrl : 'static/js/index/template/indexTemplate.html'
    })

    // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
    .state('index.questions', {
        url: 'questions',
        templateUrl : 'static/js/index/template/questionsTemplate.html'
    });

    $locationProvider.html5Mode(true);

})

.run(function ($state,$rootScope,SocketService) {
    $rootScope.$state = $state;
    $rootScope.emitState = function (state) {
        SocketService.sock.sendMessage({
            event : 'stateChange',
            previousState : $state.current.name,
            newState : state
        })
    };

    //$rootscope.$on('clientInit', function (event, data) {
    //    if(data.state)
    //});
});