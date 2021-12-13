(async() => {
    let previosScrollPos = undefined;

    while (true) {
        //Slow down the loop down a little, saves on resources
        await sleep(1);

        //get the current scroll position
        let scrollPos = window.scrollY;

        //check if the user has scrollPos, if not, dont continue
        if (previosScrollPos === scrollPos)
            continue;

        //get the document styles
        let styles = getComputedStyle(document.documentElement),
            navBar = document.getElementsByTagName('nav')[0], // get the nav bar element
            headerHeight = parseFloat(styles.getPropertyValue('--header-height')); // get the header height

        //convert the nav bar height to px from rem
        let headerHeightPX = remToPx(headerHeight);

        //if the user scrolled past the header, change its class
        if (scrollPos > headerHeightPX - (headerHeightPX * 0.8)) {
            navBar.classList.add("belowHeader");
            navBar.classList.remove("overHeader");
        } else {
            navBar.classList.add("overHeader");
            navBar.classList.remove("belowHeader");
        }

        //set the previous scroll position to the current scroll position
        previosScrollPos = scrollPos;
    }
})();