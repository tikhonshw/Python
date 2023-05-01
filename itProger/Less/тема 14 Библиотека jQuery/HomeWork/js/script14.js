// объеденил две темы только для того чтобы они обе были под рукой
// надо было показать человеку разницу написания js и jQuery

var job = [];

$('#add').click(function () {
    // job.push($('#job').val());
    // for (i = 0; i < job.length; i++) {
    //   console.log(job[i]);
    // }
    $('#showJob').append('<p class="listJob">' + $('#job').val() + '</p>');
    $('#job').val('');
    $('#info').fadeIn('slow');
    setTimeout(function () {
      $('#info').fadeOut('slow')
    }, 2000);
});

$('#btShowJob').click(function () {
    $('#showJob').toggle('slow');
});

// $('#showJob .listJob').on('click', function (e) {
//   // $('this').css('jobClose');
//   alert('sadasd' + e);
// })

$(function() {
        $(document).on('click touchstart', '.listJob', function(){
            // alert($(this));
            $(this).toggleClass('jobClose');
        });
    });
