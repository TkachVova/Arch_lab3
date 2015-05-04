<!doctype html>
<html ng-app="app" ng-controller="pizzaController">
    <head>
    <title>PizzaHut</title>
    <!-- jQuery, Angular -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.3.15/angular.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.0rc1/angular-route.min.js"></script>
    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <!-- AngularStore app -->
    <script src="app.js" type="text/javascript"></script>

    </head>
    <body>
        <div class="container">
            <div class="jumbotron">
                <h2>
                <a href="/" style="text-decoration:none">
                    <img ng-src="Pizza_Hut_logo.png"  height="40px" width="40px" alt="logo" />
                </a>Pizza Hut
                </h2>
            </div>
            <div style="clear:both"></div>
        </div>


        <div class="container-fluid">
            <div class="row-fluid">
                <div class="span11 offset1">
                    <div class="container">

        <div class="row">
            <div class="col-md-12">
                <strong class="error" ng-bind="error"></strong>
                <p data-ng-hide="addMode"><a data-ng-click="toggleAdd()" href="javascript:;" class="btn btn-primary">Add New</a></p>
                <form name="addPizza" data-ng-show="addMode" style="width:600px;margin:0px auto;">
                    <div class="form-group">
                        <label for="cid" class="col-sm-2 control-label">ID:</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="cid" placeholder="please enter id" data-ng-model="newpizza.Id" required />
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="cname" class="col-sm-2 control-label">Name:</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="cname" placeholder="please enter your name" data-ng-model="newpizza.name" required />
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="address" class="col-sm-2 control-label">Address:</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="address" placeholder="please enter your address" data-ng-model="newpizza.ingridients" required />
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="city" class="col-sm-2 control-label">City:</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="city" placeholder="please enter your city" data-ng-model="newpizza.price" required />
                        </div>
                    </div>
                    <br />
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <input type="submit" value="Add" data-ng-click="add()" data-ng-disabled="!addPizza.$valid" class="btn btn-primary" />
                            <input type="button" value="Cancel" data-ng-click="toggleAdd()" class="btn btn-primary" />
                        </div>
                    </div>
                    <br />
                </form>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <br />
                <br />
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="table-responsive">
                    <table class="table table-bordered table-hover" style="width:800px">
                        <tr>
                            <th>Id</th>
                            <th>Name</th>
                            <th>Ingridients</th>
                            <th>Cost</th>
                            <th></th>
                        </tr>
                        <tr data-ng-repeat="pizza in pizzas">
                            <td><strong data-ng-hide="pizza.editMode" ng-bind="pizza.id"></strong></td>
                            <td>
                                <p data-ng-hide="pizza.editMode" ng-bind="pizza.name"></p>
                                <input data-ng-show="pizza.editMode" type="text" data-ng-model="pizza.name" />
                            </td>
                            <td>
                                <p data-ng-hide="pizza.editMode" ng-bind="pizza.ingridients"></p>
                                <input data-ng-show="pizza.editMode" type="text" data-ng-model="pizza.ingridients" />
                            </td>
                            <td>
                                <p data-ng-hide="pizza.editMode" ng-bind="pizza.price"></p>
                                <input data-ng-show="pizza.editMode" type="text" data-ng-model="pizza.price" />
                            </td>
                            <td>
                                <p data-ng-hide="pizza.editMode"><a data-ng-click="toggleEdit(pizza)" href="javascript:;">Edit</a> | <a data-ng-click="deletep(pizza)" href="javascript:;">Delete</a></p>
                                <p data-ng-show="pizza.editMode"><a data-ng-click="save(pizza)" href="javascript:;">Save</a> | <a data-ng-click="toggleEdit(pizza)" href="javascript:;">Cancel</a></p>
                            </td>
                        </tr>
                    </table>
                    <hr />
                </div>
            </div>
        </div>

    </div>
                </div>
            </div>
        </div>

    </body>
</html>