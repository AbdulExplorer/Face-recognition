// Function to reveal additional categories
function showMoreCategories() {
    const additionalCategories = document.getElementById('additional-categories');
    if (additionalCategories.classList.contains('hidden')) {
        additionalCategories.classList.remove('hidden');
    } else {
        additionalCategories.classList.add('hidden');
    }
}

// Navigation function
function navigateTo(page) {
    window.location.href = page;
}
