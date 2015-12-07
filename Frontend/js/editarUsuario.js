var W3CDOM = (document.getElementsByTagName && document.createElement);

window.onload = function () {
  document.forms[0].onsubmit = function () {
    return validate()
  }
}

function validate() {
  validForm = 'true';
  firstError = null;
  errorstring = '';
  var x = document.forms[0].elements;
  for (var i=0;i<x.length;i++) {
    if (!x[i].value)
      writeError(x[i],"Campo es requerido");
  }
  if (x['email'].value.indexOf('@') == -1)
    writeError(x['email'],'No es un email valido');
  if (!x['fechaNacimiento'].value.match(/^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/))
    writeError(x['fechaNacimiento'],'Fecha  no valida');
  if (!x['telefono'].value.match( /^(?:\+|-)?\d+$/))
    writeError(x['telefono'],'Telefono no  valido');
  if (!x['first_name'].value.match('^[a-zA-Z \s*]*$'))
    writeError(x['first_name'],'nombre no valido');
  if (!x['last_name'].value.match('^[a-zA-Z \s*]*$'))
    writeError(x['last_name'],'apellido no valido');
  if (!W3CDOM)
    alert(errorstring);
  if (firstError)
    firstError.focus();
  if (validForm){
    return true;
  }
  return false;
};            
      
function writeError(obj,message) {
  validForm = false;
  if (obj.hasError) return;
  if (W3CDOM) {
  obj.onchange = removeError;
    var sp = document.createElement('span');
    sp.className = 'alert';
    sp.style.color="red"
    sp.appendChild(document.createTextNode(message));
    obj.parentNode.appendChild(sp);
    obj.hasError = sp;
  }else {
    errorstring += obj.name + ': ' + message + '\n';
    obj.hasError = true;
  }
  if (!firstError)
    firstError = obj;
};
      
function removeError(){
  //this.className = this.className.substring(0,this.className.lastIndexOf(' '));
  this.parentNode.removeChild(this.hasError);
  this.hasError = null;
  this.onchange = null;
}
