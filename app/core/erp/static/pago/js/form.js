$(function () {

   $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

   $('.btnAddDetpago').on('click', function () {
        $('#myModalDetpago').modal('show');
    });

    $('#myModalDetpago').on('hidden.bs.modal', function (e) {
        $('#frmDetpago').trigger('reset');
    })

    $('#frmDetpago').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_detpago');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear al siguiente cliente?', parameters, function (response) {
                $('#myModalDetpago').modal('hide');
            });
    });
});