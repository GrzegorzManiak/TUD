const pages = {
    'home': './index.html',
    'ui/ux': './uxui.html'
}

let currentPageName;

// Really basic sleep function.
function sleep(ms) {
    // Create a new promise, no rejection as this cant fail
    return new Promise((resolve) => {
        // Time out for some ammount of time,
        // once done exec resolve(), resolving the promise.
        setTimeout(resolve, ms);
    })
}

function currentPage(page) {
    currentPageName = page;
}

// adds elements to the nav bar from the 'pages' object.
function addElements(navID, selected) {
    // Get the navbar element
    let element = document.getElementById(navID);

    // For each item in the Pages object
    Object.keys(pages).forEach((key) => {
        // create a bew LI element and a new P element
        let li = document.createElement('li'),
            p = document.createElement('p');

        // Assign the LI an ID
        li.id = key;

        // Assign the P its text content
        p.textContent = key;

        // Adds an event listner, eg when this element is clicked
        li.addEventListener('click', async(elm) => {
            // Im delaying the page change to let clicking transform finish
            await sleep(200);

            // if the user is trying to get, eg, from home => home, dont refresh
            if (currentPageName != key) document.location = pages[key];
        });

        if (currentPageName == key) p.className = selected;

        li.appendChild(p);
        element.appendChild(li)
    });
}

function selectPageIndicator(num) {
    let elements = [...document.getElementsByClassName('pageIndicatorElement')],
        i = 0;

    elements.forEach((elm) => {
        if (i == num && i < elements.length) elm.className = 'pageIndicatorElement pageIndicatorElementActive';
        else elm.className = 'pageIndicatorElement';
        i++;
    });
}

async function startScroll() {
    let prevPos = -1,
        currentPage = 0,
        notScrolledFor = 0;

    //window.scrollTo(0, 0);

    while (true) {
        // Get the current scroll position  
        let scroll = document.documentElement.scrollTop,
            height = document.documentElement.clientHeight;

        await sleep(5);
        let closerToPage = Math.round(scroll / height),
            moveTo = closerToPage * height

        console.log(height, scroll, closerToPage, moveTo);

        if (scroll != moveTo) {
            await sleep(1);
            notScrolledFor++;

            if (notScrolledFor > 100) {
                window.scrollTo(0, moveTo);
                notScrolledFor = 0;
            }
        }

        if (scroll == prevPos) continue;
        else notScrolledFor = 0;

        currentPage = Math.round(scroll / height);
        selectPageIndicator(currentPage);

        prevPos = scroll;
    }
}

let currentlySelected = 0;
//Carousel
function carousel() {
    let carousel = document.getElementById('carousel'),
        images = [...carousel.getElementsByTagName('img')];

    images.forEach((img, i) => {
        if (i == currentlySelected) img.className = 'csl';
        else if (i - 1 == currentlySelected) img.className = 'carouselLeft';
        else if (i - 2 == currentlySelected) img.className = 'carouselRight';
        else img.className = 'carouselMiddle';
    });
}