var active_tags = new Set()

function loadRecipes() {
	if (window.location.pathname == '/') {
        url = '/recipes'
        if (active_tags.size > 0) {
            url += '?tags=' + Array.from(active_tags)
        }
		$.ajax(url, {
			'success': setRecipeContent
		})
	}
}

function setRecipeContent(data) {
	$('#recipeList').html(data)
}

function toggleTag(tag) {
    if (active_tags.has(tag)) {
        active_tags.delete(tag)
    }
    else {
        active_tags.add(tag)
    }
    $('#button-' + tag).toggleClass('filter-button-on')
    $('#button-' + tag).toggleClass('filter-button-off')
    loadRecipes()
}
