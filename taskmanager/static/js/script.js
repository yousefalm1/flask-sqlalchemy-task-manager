document.addEventListener('DOMContentLoaded', function () {
    // SideNav Initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // DatePicker Initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm yyyy",
        i18n: {done: "Select"}

    });

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // Collapsible initialization
    let collapsibles  = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
})