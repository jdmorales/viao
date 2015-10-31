
$('#crearCultivo').click(function(){
        var formdata= new FormData($("#form-cultivo").get(0));

        $.ajax({
            type:'post',
            url:"/cultivo/",
            dataType: 'json',
            async: true,
            data: formdata,
            success: function(response){

                if (response.exito){
                    $("#form-cultivo").get(0).reset();
                         
                          $("#jefe option[value="+formdata.get("jefe")+"]").remove();
                           alert("Cultivo crearo exitosamente");
                    }else{
                        validate();
                    }               
            },
         processData: false,
         contentType: false,
    }); 
});
var W3CDOM = (document.getElementsByTagName && document.createElement);
function validate() {
    validForm = true;
    firstError = null;
    errorstring = '';
    var x = document.forms[0].elements;
    for (var i=0;i<x.length;i++) {
        if (!x[i].value)
            writeError(x[i],"Campo es requerido");
    }

    if(x['jefe'].value == "Elige un Jefe")
        writeError(x['jefe'],"Campo es requerido");
    if(x['area'].value > 20)
        writeError(x['area'],"Menor o igual a 20");
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