 $('#registrousuario').click(function(){
                var formdata= new FormData($("#form-usuario").get(0));
                $.ajax({
                            type:'post',
                            url:"/crear/personas/",
                            dataType: 'json',
                            async: true,
                            data: formdata,
                            success: function(response){
                                if (response.exito){
                                        $("#form-usuario").get(0).reset();
                                        alert("Usuario creado con exito!");
                                }else{
                                	validate(response.msn);
                                } 
                               
                            },
                            processData: false,
                            contentType: false,
                }); 
            });

var W3CDOM = (document.getElementsByTagName && document.createElement);

function validate(msn) {
	validForm = true;
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
	if (!x['documento'].value.match( /^\d+$/))
		writeError(x['documento'],'Documento No valido');
	if (msn)
		writeError(x['documento'],'Documento ya existe');
	if (!x['password'].value.match('(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,20})$'))
		writeError(x['password'],'minimo 8 caracteres, 1 mayuscula, 1 digito');
	if (!x['first_name'].value.match('^[a-zA-Z \s*]*$'))
		writeError(x['first_name'],'nombre no valido');
	if (!x['last_name'].value.match('^[a-zA-Z \s*]*$'))
		writeError(x['last_name'],'apellido no valido');
	if (!W3CDOM)
		alert(errorstring);
	if (firstError)
		firstError.focus();
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
