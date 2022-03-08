$(function () {
   $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

   $('#date_birth').datetimepicker({
       format: 'DD-MM-YYYY',
       // format: 'YYYY-MM-DD',
       date: moment().format("DD-MM-YYYY"),
       locale: 'es'
       //minDate: moment().format("YYYY-MM-DD")
   });
   // $('.btnAddDetpago').on('click', function () {
   //      $('#myModalDetpago').modal('show');
   //  });
   //
   //  $('#myModalDetpago').on('hidden.bs.modal', function (e) {
   //      $('#frmDetpago').trigger('reset');
   //  })
   //
   //  $('#frmDetpago').on('submit', function (e) {
   //      e.preventDefault();
   //      var parameters = new FormData(this);
   //      parameters.append('action', 'create_detpago');
   //      submit_with_ajax(window.location.pathname, 'Notificación',
   //          '¿Estas seguro de crear al siguiente cliente?', parameters, function (response) {
   //              $('#myModalDetpago').modal('hide');
   //          });
   //  });
});