$(function () {
    $('#data').DataTable({
        responsive: true, // Se ajusten os datos
        autoWidth: false,  // Se respetan los anchos que se colocan
        destroy: true,  // Permite reinicializar la tabla con otro proceso
        deferRender: true,  // Permite agilizar la carga de más de 50 0000 filas
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "apellidos"},
            {"data": "dni"},
            {"data": "puesto.name"},
            {"data": "area.name"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a href="/erp/empleado/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/erp/empleado/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
