
const checkAndHide(textInputElement, textSubmissionButton)33{
  const textInputElement = Document.getElementById('question');
  const textSubmissionButton = Document.getElementById('question-submit');
// const event = new KeyboardEvent("syntheticKey", false);
 1 textInputElement.addEventListener("keydown", event => {
    if (event.isComposing || event.keyCode === 229) {
      element.classList.remove('hidden');
      console.warn('Showing the Submit Button')
})};