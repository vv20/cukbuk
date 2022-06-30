function loadRecipes() {
	if (window.location.pathname == '/') {
		$.ajax('/recipes', {
			'success': setRecipeContent
		})
	}
}

function setRecipeContent(data) {
	$('#recipeList').html(data)
}
