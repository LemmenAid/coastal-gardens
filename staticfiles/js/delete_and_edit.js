document.addEventListener("DOMContentLoaded", function () {
    // Handle comment deletion modal
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }

    // Handle story deletion modal
    const deleteStoryModalElement = document.getElementById("deleteStoryModal"); // Get the DOM element
    const deleteStoryModal = new bootstrap.Modal(deleteStoryModalElement); // Initialize the modal instance
    const deleteStoryConfirm = document.getElementById("deleteStoryConfirm");

    deleteStoryModalElement.addEventListener("show.bs.modal", function (event) {
        const button = event.relatedTarget; // Button that triggered the modal
        const storyId = button.getAttribute("data-story_id"); // Extract story ID
        const deleteUrl = `/delete_story/${storyId}/`; // Construct the delete URL
        deleteStoryConfirm.setAttribute("href", deleteUrl); // Set the modal confirm button's href
    });

    // Ensure correct modal visibility on button click
    const deleteStoryButtons = document.querySelectorAll('[data-bs-target="#deleteStoryModal"]');
    deleteStoryButtons.forEach(button => {
        button.addEventListener("click", () => {
            deleteStoryModal.show();
        });
    });
});



view:
@login_required
def delete_story(request, story_id):
    """
    Allows the author of a member story to delete their story.

    Args:
        request: The HTTP request object.
        story_id: ID of the story to be deleted.

    Returns:
        Redirects to the member_stories page with a success or error message.
    """
    post = get_object_or_404(Post, id=story_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Story deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own stories!')
    return HttpResponseRedirect(reverse('member_stories'))