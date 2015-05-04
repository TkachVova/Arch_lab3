/**
 * Created by vladymyr on 04.05.15.
 */
  //create angularjs controller
    var pizzaApp = angular.module('app', ['ngRoute']);
    pizzaApp.controller('pizzaController', ['$scope', '$http', pizzaController]);






    //angularjs controller method
    function pizzaController($scope, $http, pizzaService) {

        //declare variable for mainain ajax load and entry or edit mode
        $scope.test = "HelloWorld"
        $scope.loading = true;
        $scope.addMode = false;

        $http.get('/pizzas/').success(function (data) {
            $scope.pizzas = data.pizzas;
            $scope.loading = false;
        })
        .error(function () {
            $scope.error = "An Error has occured while loading pizzas!";
            $scope.loading = false;
        });




        //by pressing toggleEdit button ng-click in html, this method will be hit
        $scope.toggleEdit = function () {
            this.pizza.editMode = !this.pizza.editMode;
        };

        //by pressing toggleAdd button ng-click in html, this method will be hit
        $scope.toggleAdd = function () {
            $scope.addMode = !$scope.addMode;
        };

        //Inser Pizza
        $scope.add = function () {
            $scope.loading = true;
            $http.post('/pizzas/', this.newpizza).success(function (data) {
                alert("Added Successfully!!");
                $scope.addMode = false;
                $scope.pizzas.push(data);
                $scope.loading = false;
            }).error(function (data) {
                $scope.error = "An Error has occured while Adding pizza! " + data;
                $scope.loading = false;
            });
        };

        //Edit Pizza
        $scope.save = function () {
            alert("Edit");
            $scope.loading = true;
            var frien = this.pizza;
            alert(frien);
            $http.put('/pizzas/' + frien.Id, frien).success(function (data) {
                alert("Saved Successfully!!");
                frien.editMode = false;
                $scope.loading = false;
            }).error(function (data) {
                $scope.error = "An Error has occured while Saving pizza! " + data;
                $scope.loading = false;
            });
        };

       //Delete pizza
        $scope.deletep = function () {
            $scope.loading = true;
            var Id = this.pizza.Id;
            $http.delete('/pizzas/' + Id).success(function (data) {
                alert("Deleted Successfully!!");
                $.each($scope.pizzas, function (i) {
                    if ($scope.pizzas[i].Id === Id) {
                        $scope.pizzas.splice(i, 1);
                        return false;
                    }
                });
                $scope.loading = false;
            }).error(function (data) {
                $scope.error = "An Error has occured while Saving pizza! " + data;
                $scope.loading = false;
            });
        };

    }