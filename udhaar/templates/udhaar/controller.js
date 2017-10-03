
function addNameField(){
  var objTo = document.getElementById('spawn');
  var objCopy = document.getElementById('name').outerHTML;
  objTo.innerHTML+=objCopy;
  //objTo.appendChild(clone);
}

function addTrans(){
  var objTo = document.getElementById('form-parent');
  var objCopy = document.getElementById('form-row').outerHTML;
  objTo.innerHTML+=objCopy;

}

function addNewMember(){
  var objTo = document.getElementById('update-group');
  var objCopy = document.getElementById('new-member').outerHTML;
  objTo.innerHTML+=objCopy;

}
