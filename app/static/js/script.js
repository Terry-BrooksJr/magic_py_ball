const checkAndHide(textInputElement, textSubmissionButton)33{
  const textInputElement = Document.getElementById('question');
  const textSubmissionButton = Document.getElementById('question-submit');
// const event = new KeyboardEvent("syntheticKey", false);
 1 textInputElement.addEventListener("keydown", event => {
    if (event.isComposing || event.keyCode === 229) {
      element.classList.remove('hidden');
      console.warn('Showing the Submit Button')
})}

const xhr = null;
getXmlHttpRequestObject = function () {
  if (!xhr) {
    xhr = new XMLHttpRequest();
  }
  return xhr;
}; 

//Function to allow communication of the Response from the PostGres DB where the reponses are stored. 
function dataCallback() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    console.log('Data Received from Wisdom Vault');
    getDate();
    eightBallAnswerArea = document.getElementById('answer');
    eightBallAnswerArea.innerHTML = xhr.responseText;
  }
}