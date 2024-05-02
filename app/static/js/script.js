document.addEventListener("DOMContentLoaded", function() {
    const titleInput = document.querySelector('.NewNote .title-input');
    const bodyEditor = document.querySelector('.NewNote trix-editor');
    const wtfButton = document.getElementById('wtf');
    const explanationDiv = document.querySelector('.NewNote .explanation');
    const darkModeToggle = document.getElementById('darkMode');
    const newNoteButton = document.querySelector('.NewNote .action .new_note');

    // Function to handle form submission
function handleSubmit(event) {
    event.preventDefault();
    const titleInput = document.querySelector('.NewNote .title-input');
    const titleValue = titleInput.value.trim();

    // Validate title
    if (titleValue === '') {
        alert('Please add a title to your note');
        return;
    }

    // Submit the form
    event.target.submit();
}

// Add event listener to form submission
const form = document.querySelector('.NewNote form');
if (form) {
    form.addEventListener('submit', handleSubmit);
}


    // Function to handle dark mode toggle
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', function() {
            document.body.classList.toggle('dark_mode');
        });
    }

    // Function to create a new note
    // if (newNoteButton) {
    //     newNoteButton.addEventListener('click', function() {
    //         // Reset title and body inputs
    //         if (titleInput) {
    //             titleInput.value = '';
    //         }
    //         if (bodyEditor) {
    //             bodyEditor.editor.loadHTML('');
    //         }
    //     });
    // }

    // Open explanation category
    if (wtfButton && explanationDiv) {
        wtfButton.addEventListener('click', function() {
            explanationDiv.classList.toggle('open');
        });
    }
});
