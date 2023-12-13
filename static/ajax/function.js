//Adding review
const monthNames = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"];

$('#commentForm').submit(function(e){
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDay() + " " + monthNames[dt.getUTCMonth()] + " " + dt.getFullYear()

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(res){
            console.log("Comment Saved to DB...");

            if (res.bool == true) {
                $("#review-res").html("Avis ajouté avec succès !")
                $(".hide-comment-form").hide()
                $(".add-review").hide()

                let _html = '<div class="comment-list">'
                    _html+= '<div class="comments">'
                    _html+= '<figure class="img-thumbnail">'
                    _html+= '   <img src="https://cdn-icons-png.flaticon.com/512/6596/6596121.png" alt="{{review.user}}" width="80" height="80">'
                    _html+= '</figure>'
                    _html+= '<div class="comment-block">'
                    _html+= '<div class="comment-header">'
                    _html+= '<div class="comment-arrow"></div>'
                    _html+= '<div class="ratings-container float-sm-right">'
                    _html+= '<div class="product-ratings">'
                    for (let i = 1; i < res.context.rating; i++) {
                        _html += '<i class="fa fa-star text-dark"></i>'
                    }
                    _html+= '</div>'
                    _html+= '</div>'
                    _html+= '<span class="comment-by">'
                    _html+= '<strong>'+ res.context.user +'</strong> – ' + time + ''
                    _html+='</span>'
                    _html+= '</div>'
                    _html+= '<div class="comment-content">'
                    _html+= '<p>'+ res.context.review +'</p>'
                    _html+= '</div>'
                    _html+= '</div>'
                    _html+= '</div>'
                    _html+= '</div>'

                    $(".comment-content-list").prepend(_html)
            }

        }
    })
})

//filter by category and marque no-refresh page
$(document).ready(function(){
    $(".filter-checkbox, #price-filter-btn").on('click', function(){
        console.log("Le checkbox est touché");

        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;


        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter") // brand , category

            console.log("La valeur du filtre est ", filter_value);
            console.log("La clée du filtre est ", filter_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter= ' + filter_key + ' ]:checked')).map(function(element){
                return element.value
            })
        })
        console.log("L'object filtré est ", filter_object);
        $.ajax({
            url: '/filter-product',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Essayer de filtrer le produit...");
            },
            success:function(response){
                console.log(response);
                console.log("Donnés filtrée avec succès...");
                $("#filtered-produit").html(response.data)
            }
        })
    })


    // Filter by price
    $("#max_price").on('blur', function() {
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        // console.log("Le prix actuel est ", current_price);
        // console.log("Le prix min est ", min_price);
        // console.log("Le prix max est ", max_price);

        if (current_price < parseInt(min_price) || current_price > parseInt(max_price)) {
            // console.log('Error price occured');

            min_price = Math.round(min_price * 100)/100
            max_price = Math.round(max_price * 100)/100

            // console.log("Le prix min est--- ", min_price);
            // console.log("Le prix max est--- ", max_price);
            alert("Le prix doit être compris entre " + min_price + " GNF " + " et " + max_price + ' GNF')
            $(this).val(min_price)
            $('#range').val(min)


            $(this).focus()
            return false
        }
    })
})
