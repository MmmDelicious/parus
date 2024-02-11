$(document).ready(function() {


    //обработчик поиска
    $("#searchForm").submit(function(event) {
        event.preventDefault();

        var searchInput = $("#searchInput").val();

        $.ajax({
            type: "POST",
            url: "/search",
            data: {searchInput: searchInput},
            success: function(response) {
                $("table tbody").html(response);

            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    //обработчик выпадающего меню с локациями(выводит товары для указанной локации)
    $("#locationSelect").change(function(event) {
        event.preventDefault();

        var searchInput = $(this).val();

        $.ajax({
            type: "POST",
            url: "/filter_products",
            data: { searchInput: searchInput },
            success: function(response) {
               $("body").html(response);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    //добавление локаций в бд
    $("#addLocationForm").submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/add_location",
            data: formData,
            success: function(response) {
                $("#addLocationModal").hide();
                $("body").html(response);

            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    //обработчик модального окна добавления нового товара
    $("#addProductForm").submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/add_product",
            data: formData,
            success: function(response) {
               $("#addProductModal").hide();
               $("body").html(response);

            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    //обработчик модального окна добавления товара из базы
    $("#addExistingProductForm").submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/add_existing_product",
            data: formData,
            success: function(response) {
                $("#addExistingProductModal").hide();
                $("body").html(response);

            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });

    //запросы для кнопок добавить и удалить товар, тут была попытка менять количество товара не перерисовывая полностью страницу.
    $('.add-inventory').click(function() {
        $('#inventoryAction').val('add');
        $('#inventoryProductId').val($(this).data('product-id'));
        $('#inventoryLocationId').val($(this).data('location-id'));
        $('#inventoryChangeModal').modal('show');
    });

    $('.remove-inventory').click(function() {
        $('#inventoryAction').val('remove');
        $('#inventoryProductId').val($(this).data('product-id'));
        $('#inventoryLocationId').val($(this).data('location-id'));
        $('#inventoryChangeModal').modal('show');
    });

    $('#inventoryChangeForm').submit(function(e) {
        e.preventDefault();
        $('#inventoryChangeModal').modal('show');
        var formData = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/change_inventory",
            data: formData,
            success: function(response) {
                var productId = $('#inventoryProductId').val();
                var locationId = $('#inventoryLocationId').val();
                $('#inventoryCount_' + productId + '_' + locationId).text(response.newCount);
                $('#inventoryChangeModal').modal('hide');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });


     //сортировка таблицы по цене( при нажатии на название столбца)
    $('#priceHeader').click(function(e) {
        e.preventDefault();



        $.ajax({
            type: "GET",
            url: "/sorted_by_price",
            success: function(response) {
                    $("body").html(response);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
         //сортировка таблицы по количеству( при нажатии на название столбца)
    $('#countHeader').click(function(e) {
        e.preventDefault();


        var formData = $(this).serialize();
        $.ajax({
            type: "GET",
            url: "/sorted_by_count",
            success: function(response) {
                    $("body").html(response);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});
