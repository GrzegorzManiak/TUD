function remToPx(rem) {
    let styles = getComputedStyle(document.documentElement);
    //all rem is, is the root font size of the HTML document, which is generally 16px.
    //this means, all we have to do is get the font size of the HTML document,
    //multiply it by the rem value, and we have the px value.

    //we have to parse the value of the font size, because it is a string.
    //returned as '16px', formating it returns it as a 16.
    return parseFloat(styles.fontSize) * rem;
}

(async() => {
    let previosScrollPos = undefined;

    while (true) {
        //Slow down the loop a little
        await sleep(1);

        //get the current scroll position
        let scroll = document.scrollingElement.scrollTop;

        //check if the user has scrolled, if not, dont continue
        if (previosScrollPos === scroll)
            continue;

        let styles = getComputedStyle(document.documentElement),
            navBar = document.getElementsByTagName('nav')[0],
            headerHeight = parseInt(styles.getPropertyValue('--header-height'));

        //convert the nav bar height to px from rem
        let headerHeightPX = remToPx(headerHeight);

        //if the user scrolled past the header, change its class
        if (scroll > headerHeightPX - (headerHeightPX * 0.3)) {
            navBar.classList.add("belowHeader");
            navBar.classList.remove("overHeader");
        } else {
            navBar.classList.add("overHeader");
            navBar.classList.remove("belowHeader");
        }

        //set the previous scroll position to the current scroll position
        previosScrollPos = scroll;
    }
})();