
    document.getElementById('image').onchange = function(evt) {
        var tgt = evt.target || window.event.srcElement,
            files = tgt.files;

        // FileReader support
        if (FileReader && files && files.length) {
            var fr = new FileReader();
            fr.onload = function() {
                document.getElementById('img').src = fr.result;
            }
            fr.readAsDataURL(files[0]);
        }

        // Not supported
        else {
            // fallback -- perhaps submit the input to an iframe and temporarily store
            // them on the server until the user's session ends.
        }
    }

    $('#exampleModal').on('show', function(e) {
        var link = e.relatedTarget(),
            modal = $(this),
            username = link.data("service_id"),
            email = link.data("email");

        modal.find("#email").val(email);
        modal.find("#username").val(username);
    });

    function myFunction(x) {
        x.className = "nav-link active router-link-active";
    }




    // When the user scrolls down 50px from the top of the document, resize the header's font size
    window.onscroll = function() {
        scrollFunction()
    };

    function scrollFunction() {
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            document.getElementById("header").className = "header sticky";
        } else {
            document.getElementById("header").className = "header";
        }
    }
    $(document).ready(function() {
        $('#myTable').dataTable({

            dom: '<"float-left"f><"float-right"B><"float-right"l>rt<"row"<"col-sm-4"i><"col-sm-4"p>>',
            "oLanguage": {

                "sSearch": "Quick Search:"

            }
        });
    });

    $(document).ready(function() {
        $('#myTable1').dataTable({
            dom: '<"float-left"f><"float-right"B><"float-right"l>rt<"row"<"col-sm-4"i><"col-sm-4"p>>',
        });


    });


    function myFunctionNavbar(x) {
        // alert(x);
        var element = document.getElementById(x);
        tabcontent = document.getElementsByClassName("nav-link active router-link-active");
        //tabcontent.className="nav-link";
        for (var i = 0; i < tabcontent.length; i++) {
            tabcontent[i].className = "nav-link active router-link-active";
        }
        element.className = "nav-link ";
        /*var menu = document.getElementById("myDIV1");

   var links = menu.getElementsByClassName("nav-link active");
   for (var i = 0; i < links.length; i++) {
    links[i].className="nav-link";
  }*/

        //alert(element.className);

        $('#main-container').load('/navbar-content/' + x);
    }
    function load_main_content1(x) {
        // alert(x);
        var element = document.getElementById(x);
        var home = document.getElementById("home");
        tabcontent = document.getElementsByClassName("nav-link active");
        //tabcontent.className="nav-link";
        for (var i = 0; i < tabcontent.length; i++) {
            tabcontent[i].className = "nav-link";
        }
        element.className = "nav-link active";
        home.className = "nav-link active router-link-active"
        alert(x);
        $('#main_content_div').load('/main-content/' + x);
    }

    function load_main_content(x) {
        // alert(x);
        var element = document.getElementById(x);
        var home = document.getElementById("home");
        tabcontent = document.getElementsByClassName("nav-link active");
        //tabcontent.className="nav-link";
        for (var i = 0; i < tabcontent.length; i++) {
            tabcontent[i].className = "nav-link";
        }
        element.className = "nav-link active";
        home.className = "nav-link active router-link-active"
        /*var menu = document.getElementById("myDIV1");

   var links = menu.getElementsByClassName("nav-link active");
   for (var i = 0; i < links.length; i++) {
    links[i].className="nav-link";
  }*/

        //alert(element.className);

        $('#main_content_div').load('/main-content/' + x);
    }

    // Add active class to the current button (highlight it)
    var menu = document.getElementById("myDIV");
    var btns = menu.getElementsByClassName("btn");
    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("btn active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
        });
    }

    function myFunction2() {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable2");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }

    function expandTextarea(id) {
        document.getElementById(id).addEventListener('keyup', function() {
            this.style.overflow = 'hidden';
            this.style.height = 0;
            this.style.height = this.scrollHeight + 'px';
        }, false);
    }

    expandTextarea('newsbody');

    /* When the user clicks on the button,
    toggle between hiding and showing the dropdown1 content */
    function myFunction() {
        document.getElementById("mydropdown1").classList.toggle("show");
    }

    function filterFunction() {
        var input, filter, ul, li, a, i;
        input = document.getElementById("myInput2");
        filter = input.value.toUpperCase();
        div = document.getElementById("mydropdown1");
        a = div.getElementsByTagName("option");
        for (i = 0; i < a.length; i++) {
            txtValue = a[i].textContent || a[i].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "";
            } else {
                a[i].style.display = "none";
            }
        }
    }

    function myFunctionclick(e) {

        var d = document.getElementById(e);
        var d1 = document.getElementById('session');
        document.getElementById("mydropdown1").classList.toggle("show");
        d1.value = d.id;


    }

    /* When the user clicks on the button,
  toggle between hiding and showing the dropdown1 content */
    function myFunctionSelect2() {

        document.getElementById("mydropdownSelect2").classList.toggle("show");
    }

    function filterFunctionSelect2() {
        var input, filter, ul, li, a, i;
        input = document.getElementById("myInputSelect2");
        filter = input.value.toUpperCase();
        div = document.getElementById("mydropdownSelect2");
        a = div.getElementsByTagName("option");
        for (i = 0; i < a.length; i++) {
            txtValue = a[i].textContent || a[i].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "";
            } else {
                a[i].style.display = "none";
            }
        }
    }

    function myFunctionclickSelect2(e) {

        var d = document.getElementById(e);
        var d1 = document.getElementById('group');

        d1.value = d.id;
        document.getElementById("mydropdownSelect2").classList.toggle("show");

    }

    $(document).ready(function() {
        $('#nav-icon1,#nav-icon2,#nav-icon3,#nav-icon4').click(function() {
            $(this).toggleClass('open');
        });
    });

    function closeNav() {

        document.getElementById("left-menu").style.width = "20px";
        document.getElementById("main").style.marginLeft = "0";
    }

