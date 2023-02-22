
// jQuery
jQuery(document).ready(function ($) {

    if ($('.gallery-image').length) {
        $('.gallery-image').magnificPopup({
            delegate: '.popup-img', // child items selector, by clicking on it popup will open
            type: 'image',
            gallery: {
                enabled: true
            },
            zoom: {
                enabled: true,
                easing: 'ease-in-out',
                duration: 300,
                opener: function (element) {
                    return element.closest('div').find('img');
                }
            }
        });
    }


    // isotope 
    if ($('.isotop-section').length) {
        $('.item-details').isotope({
            // options
            itemSelector: '.item',
            layoutMode: 'fitRows'
        });

        $('.item-details').isotope({
            filter: $('.item-menu .active').data('filter')
        });

        $(document).on('click', '.item-menu li', function () {
            $('.item-menu li').removeClass('active');
            $(this).addClass('active');


            // filter items on button click
            var selector = $(this).data('filter');
            $('.item-details').isotope({
                filter: $(this).data('filter')
            });
        });

    }

    // Animated hr line
    setTimeout(function () {
        $('.trans--grow').addClass('grow');
    }, 275);



});




// back to top

//Get the button
var mybutton = document.getElementById("scrollUp");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// Header 

document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) {
            document.getElementById('navbar_top').classList.add('fixed-top');
            document.getElementById('navbar_top').classList.add('scroll');
            // add padding top to show content behind navbar
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        } else {
            document.getElementById('navbar_top').classList.remove('fixed-top');
            document.getElementById('navbar_top').classList.remove('scroll');
            // remove padding top from body
            document.body.style.paddingTop = '0';
        }
    });

});


const scrollSpy = new bootstrap.ScrollSpy(document.body, {
    target: '#main_nav',
    offset: 140
})



// Line chart

var xValues = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG'];
var chartSelector = document.querySelectorAll('#myChart');
if (chartSelector.length) {
    new Chart("myChart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                label: 'Amount Invested',
                data: [10, 15, 20, 25, 27, 25, 23, 25],
                borderColor: "#0077b6",
                fill: false
            },
            {
                label: 'Worth of Investement',
                data: [25, 18, 16, 17, 20, 25, 30, 35],
                borderColor: "#dc3545",
                fill: false
            }]
        },
        options: {
            legend: { display: true }
        }
    });
}


// DoughnutChart
var DoughnutChartSelector = document.querySelectorAll('#myDoughnutChart');
if (DoughnutChartSelector.length) {

    var xValues = ["Investment", "Employer", "Member"];
    var yValues = [60, 40, 30];
    var barColors = [
        "#0077b6",
        "#dc3545",
        "cyan"
    ];

    new Chart("myDoughnutChart", {
        type: "doughnut",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
            }
        }
    });
}

//PieChart
var PieChartSelector = document.querySelectorAll('#myPieChart');
if (PieChartSelector.length) {
    var xValues = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG"];
    var yValueBlue = [10, 15, 20, 25, 27, 25, 23, 25, 0];
    var yValueRed = [25, 18, 16, 17, 20, 25, 30, 35, 0];
    var barColorBlue = ["#0077b6", "#0077b6", "#0077b6", "#0077b6", "#0077b6", "#0077b6", "#0077b6", "#0077b6"];
    // var barColorRed = ["#dc3545", "#dc3545", "#dc3545", "#dc3545", "#dc3545", "#dc3545", "#dc3545", "#dc3545"];
    var barColorRed = jQuery('#myPieChart').attr('data-barColor2').split(",");


    new Chart("myPieChart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                label: 'Amount Invested',
                backgroundColor: barColorBlue,
                data: yValueBlue
            },
            {
                label: 'Worth of Investement',
                backgroundColor: barColorRed,
                data: yValueRed
            }]
        },
        options: {
            legend: { display: true },
            title: {
                display: false,
                text: "World Wine Production 2018"
            }
        }
    });
}

// DoughnutChart2
var myDoughnutChart2 = document.querySelectorAll('#myDoughnutChart2');
if (myDoughnutChart2.length) {
    var xValues = ["Investment", "Employer", "Member"];
    var yValues = [50, 40, 50];
    var barColors = [
        "#6a994e",
        "#4cc9f0",
        "#8e9aaf"
    ];

    new Chart("myDoughnutChart2", {
        type: "doughnut",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
            }
        }
    });

}

// SwiperSlide 


var mySwiper = document.querySelectorAll('.mySwiper');
if (mySwiper.length) {

    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 3,
        spaceBetween: 30,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },

        navigation: {
            enabled: false,
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            // when window width is >= 300px
            320: {
                slidesPerView: 1
            },
            // when window width is >= 480px
            768: {
                slidesPerView: 2,
            },
            // when window width is >= 768px
            900: {
                slidesPerView: 3,
            },
            // when window width is >= 768px
            // 1100: {
            //     slidesPerView: 4,
            // }
        }
    });
}