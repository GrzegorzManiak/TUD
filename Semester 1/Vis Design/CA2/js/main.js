const pages = {
    'home': './home.html',
    'tips': './tips.html',
    'css': './css.html',
    'html': './html.html',
    'about us': './aboutus.html',
    'survey': './survey.html'
}

const imgs = {
    'gregoria': {
        img: './imgs/aboutus/greg1.png',
        elem: undefined,
        name: 'Gregoria',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
    'grzegorz': {
        img: './imgs/aboutus/greg5.png',
        elem: undefined,
        name: 'Grzegorz',
        bio: 'Hey, my name is Grzegorz Maniak, I\'m studying computing at TU Tallaght campus, I have a great interest in web and software development, I also enjoy the outdoors, I love to travel, camp and hike.'
    },
    'gregor': {
        img: './imgs/aboutus/greg2.png',
        elem: undefined,
        name: 'Gregor',
        bio: 'Ello, my name is Gregor, I\'m studying computing at TU Tallaght campus, I have a great interest in web and software development, I also enjoy the outdoors, I love to travel, camp and hike.'
    },
    'grock': {
        img: './imgs/aboutus/greg4.png',
        elem: undefined,
        name: 'Grock',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
    'grebama': {
        img: './imgs/aboutus/greg3.png',
        elem: undefined,
        name: 'Grebama',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
}

let curentlyAnimating = false,
    currentPageName,
    scrollPos,
    height,
    stack = [];

//
// GENERAL FUNCTIONS
//

function remToPx(rem) {
    let styles = getComputedStyle(document.documentElement);
    //all rem is, is the root font size of the HTML document, which is generally 16px.
    //this means, all we have to do is get the font size of the HTML document,
    //multiply it by the rem value, and we have the px value.

    //we have to parse the value of the font size, because it is a string.
    //returned as '16px', formating it returns it as a 16.
    return parseFloat(styles.fontSize) * rem;
}

// Really basic sleep function.
function sleep(ms) {
    // Create a new promise, no rejection as this cant fail
    return new Promise((resolve) => {
        // Time out for some ammount of time,
        // once done exec resolve(), resolving the promise.
        setTimeout(resolve, ms);
    })
}


function hamburger(id) {
    let hamburgerBtn = document.getElementById(id),
        navLogo = document.getElementById('navLogo'),
        hamburgerContent = document.getElementById('hamburgerContent');

    hamburgerBtn.addEventListener('click', () => {
        switch (hamburgerBtn.checked) {
            case true:
                hamburgerContent.className = hamburgerContent.className.replace('hamburgerContentInvisible', '');
                hamburgerContent.className += ' hamburgerContentVisible';

                document.documentElement.className = 'htmlStopScroll';
                navLogo.classList.replace('logoColorMenuClosed', 'logoColorMenuOpen');
                break;

            case false:
                hamburgerContent.className = hamburgerContent.className.replace('hamburgerContentVisible', '');
                hamburgerContent.className += ' hamburgerContentInvisible';

                document.documentElement.className = '';
                navLogo.classList.replace('logoColorMenuOpen', 'logoColorMenuClosed');
                break;
        }
    });

    document.documentElement.className = '';
}

// adds elements to the nav bar from the 'pages' object.
function addElements(navID, selected, urlParams = '') {
    // Get the navbar element
    let element = document.getElementById(navID);

    // For each item in the Pages object
    Object.keys(pages).forEach((key) => {
        // create a bew LI element and a new P element
        let li = document.createElement('li'),
            p = document.createElement('p');

        // Assign the LI an ID
        li.class = key;

        // Assign the P its text content
        p.textContent = key;

        // Adds an event listner, eg when this element is clicked
        li.addEventListener('click', async(elm) => {
            // delaying the execution of the function,
            // active so that the animation has time to finish.
            await sleep(200);

            // if the user is trying to get, eg, from home => home, dont refresh
            if (currentPageName != key)
                document.location = `${pages[key]}?${urlParams}`;
        });

        if (currentPageName == key) p.className = selected;

        li.appendChild(p);
        element.appendChild(li)
    });
}

function selectPageIndicator(num) {
    // get the elements inside the 'pageIndicator' element
    let elements = [...document.getElementsByClassName('pageIndicatorElement')];
    // convert it from a Dom collection to an array

    elements.forEach((elm, i) => {
        if (i == num && i < elements.length) elm.className = 'pageIndicatorElement pageIndicatorElementActive';
        else elm.className = 'pageIndicatorElement';
        i++;
    });
}

async function startScroll() {
    let prevPos = -1,
        currentPage = 0,
        notScrolledFor = 0;

    while (true) {
        // Get the current scroll position  
        scrollPos = document.scrollingElement.scrollTop;
        height = document.documentElement.clientHeight;

        await sleep(5);
        let closerToPage = Math.round(scroll / height),
            moveTo = closerToPage * height

        if (scroll != moveTo) {
            await sleep(1);
            notScrolledFor++;

            if (notScrolledFor > 100) {
                window.scrollTo(0, moveTo);
                notScrolledFor = 0;
            }
        }

        if (scrollPos == prevPos) continue;
        else notScrolledFor = 0;

        currentPage = Math.round(scrollPos / height);
        selectPageIndicator(currentPage);

        prevPos = scrollPos;
    }
}