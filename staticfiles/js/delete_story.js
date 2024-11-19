document.addEventListener("DOMContentLoaded", function () {
    const deleteStoryModal = document.getElementById('deleteStoryModal');
    const deleteStoryConfirm = document.getElementById('deleteStoryConfirm');

    deleteStoryModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; // Button that triggered the modal
        const storyId = button.getAttribute('data-story_id'); // Extract story ID
        const deleteUrl = `/delete_story/${storyId}/`; // Construct the delete URL
        deleteStoryConfirm.setAttribute('href', deleteUrl); // Set the modal confirm button's href
    });
});
