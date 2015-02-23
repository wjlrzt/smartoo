smartooApp.controller('homeController', ['$scope', '$window', function($scope, $window) {
    $scope.practice = function(event) {
        var searchText = searchTextNormalization($scope.searchText);
        if (!searchText) {
            return;
        }

        // go to the practice page
        // TODO: first check if it's correct topic (if not get suggested
        // similar topics)
        // TODO: lower/upper case normalization
        var practiceUrl = '/practice/' + searchText;
        console.log(practiceUrl);

        if (event.ctrlKey == 1) {
            $window.open(practiceUrl);
            //$window.open(practiceUrl, '_blank');
        } else {
            console.log('normal');
            $window.location.href = practiceUrl;
        }
    }
}]);


// ========================================================================
//     Helper methods
// ========================================================================

// normalize search text, for example strip leading/trailing spaces, replaces
// spaces with underscores, removes URL prefix etc.
function searchTextNormalization(searchText) {
    // strip leading and trailing spaces
    searchText = $.trim(searchText);

    // remove URL prefix (if there is)
    parts = searchText.split('/');
    searchText = parts[parts.length - 1];

    // replace white space characters by underscores
    searchText = searchText.replace(/\s+/g, "_");

    return searchText;
}


