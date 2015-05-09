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
        $scope.addMode = false;

        $http.get('/pizzas/').success(function (data) {
            $scope.pizzas = data.pizzas;
        })
        .error(function () {
            $scope.error = "An Error has occured while loading pizzas!";
        });

        $scope.newpizza = {
            "id":"",
            "name":"",
            "ingridients":"",
            "price":""
        }


        //by pressing toggleEdit button ng-click in html, this method will be hit
        $scope.toggleEdit = function () {
            this.pizza.editMode = !this.pizza.editMode;
        };

        //by pressing toggleAdd button ng-click in html, this method will be hit
        $scope.toggleAdd = function () {
            var max = 0;
            for(var i = 0; i < $scope.pizzas.length; i++)
            {
                if (max < $scope.pizzas[i].id)
                {
                    max = $scope.pizzas[i].id;
                }
            }
            $scope.newpizza.id = max + 1;
            $scope.addMode = !$scope.addMode;
        };

        //Insert Pizza
        $scope.add = function () {
            //alert($scope.newpizza);
            //alert(JSON.stringify($scope.newpizza))
            $http.post('/pizzas/', JSON.stringify($scope.newpizza)).success(function () {
                alert("Added Successfully!!");
                var p = {
                    "id": $scope.newpizza.id,
                    "name":$scope.newpizza.name,
                    "ingridients":$scope.newpizza.ingridients,
                    "price":$scope.newpizza.price
                }
                $scope.pizzas.push(p);

                $scope.toggleAdd();
                $scope.newpizza.id = "";
                $scope.newpizza.name = "";
                $scope.newpizza.ingridients = "";
                $scope.newpizza.price = "";
            }).error(function () {
                $scope.error = "An Error has occured while Adding pizza! " ;
            });
        };

        //Edit Pizza
        $scope.save = function (pizzaid, pizzaname, pizzaing, pizzaprice) {
            //alert("Edit");
            var frien = {
                "id": pizzaid,
                "name":pizzaname,
                "ingridients":pizzaing,
                "price":pizzaprice
            }
           // alert(JSON.stringify(frien));
            $http.put('/pizzas/'+frien.id, JSON.stringify(frien)).success(function () {
                alert("Edited Successfully!!");
                frien.editMode = false;
            }).error(function () {
                $scope.error = "An Error has occured while Saving pizza! ";
            });
        };

       //Delete pizza
        $scope.deletep = function (pizzaid) {
            //alert(pizzaid);
            $http.delete('/pizzas/'+pizzaid).success(function () {
                alert("Deleted Successfully!!");
                $.each($scope.pizzas, function (i) {
                    if ($scope.pizzas[i].id === pizzaid) {
                        $scope.pizzas.splice(i, 1);
                        return false;
                    }
                });
            }).error(function () {
                $scope.error = "An Error has occured while Deleting pizza! ";
            });
        };

    }