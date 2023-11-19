$(document).ready(function () {
    var table = $('#tabla').DataTable({
        responsive: true,
        "language": {
            url: "/static/js/location/es_ES.json"
        }
    });
});
function abrir_modal(url) {
    $('#myModal').load(url, function() {
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        })
        $(this).modal('show');
        });
    return false;
}
function cerrar_modal(){
    $('#myModal').modal('close');
    return false;
}
function eliminar() {
    var x = confirm("Desea Eliminar?");
    if (x)
        return true;
    else
        return false;
}