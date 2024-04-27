document.addEventListener("DOMContentLoaded", function() {
    const titleInput = document.querySelector('.title input');
    const bodyEditor = document.querySelector('trix-editor');

    // Function to handle form submission
    function handleSubmit(event) {
        event.preventDefault();
        const titleValue = titleInput.value.trim();
        const bodyValue = bodyEditor.editor.getDocument().toString().trim();

        if (titleValue === '' || bodyValue === '') {
            alert('Please add a title and a body to your note');
            return;
        }

        // Here you can submit the form or perform any other action
        console.log('Note submitted:', titleValue, bodyValue);
    }

    // Add event listener to form submission
    document.querySelector('form').addEventListener('submit', handleSubmit);

    // Function to handle dark mode toggle
    document.getElementById('darkMode').addEventListener('change', function() {
        document.body.classList.toggle('dark_mode');
    });

    // Function to create a new note
    document.querySelector('.action.new_note').addEventListener('click', function() {
        // Reset title and body inputs
        titleInput.value = '';
        bodyEditor.editor.loadHTML('');
    });
});

// open explanation category
document.addEventListener("DOMContentLoaded", function() {
    const wtfButton = document.getElementById('wtf');
    const explanationDiv = document.querySelector('.explanation');

    // Toggle the open class on explanation div when the wtf button is clicked
    wtfButton.addEventListener('click', function() {
        explanationDiv.classList.toggle('open');
    });
});

