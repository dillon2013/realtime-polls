angular.module('MainApp').factory('pollsModel', function () {
    return [
        {
            question : 'What is the Arsenal football stadium capacity?',
            answers : [
                {answer : '20,000', value : 0, selected : false},
                {answer : '55,000', value : 0, selected : false},
                {answer : '60,000', value : 0, selected : false},
                {answer : '40,000', value : 0, selected : false}
            ]
        },
        {
            question : 'What is the Tottenham football stadium capacity?',
            answers : [
                {answer : '20,000', value : 0, selected : false},
                {answer : '55,000', value : 0, selected : false},
                {answer : '10,000', value : 0, selected : false},
                {answer : '30,000', value : 0, selected : false}
            ]
        }
    ]
});