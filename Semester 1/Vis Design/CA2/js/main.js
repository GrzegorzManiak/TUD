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

    while (true) {
        // Get the current scroll position  
        let scroll = document.documentElement.scrollTop,
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

        if (scroll == prevPos) continue;
        else notScrolledFor = 0;

        currentPage = Math.round(scroll / height);
        selectPageIndicator(currentPage);

        prevPos = scroll;
    }
}

const imgs = {
    '0': { 
        img: './imgs/aboutus/1.jpg', //The path to the image
        elem: undefined, //Onece the image is loaded, this will be set to the image element
        name:'', //The name of the group memeber
        bio: '' //Their bio
    },
    '1': { 
        img: './imgs/aboutus/2.jpg', 
        elem: undefined,
        name:'',
        bio: '' 
    },
    '2': { 
        img: './imgs/aboutus/3.jpg', 
        elem: undefined,
        name:'',
        bio: '' 
    },
    '3': { 
        img: './imgs/aboutus/4.jpg', 
        elem: undefined,
        name:'',
        bio: '' 
    },
    '4': { 
        img: './imgs/aboutus/5.jpg', 
        elem: undefined,
        name:'',
        bio: '' 
    },
}

//Carousel
function addCarouselItems() {
    let carousel = document.getElementById('carousel');

    Object.keys(imgs).forEach((key, i) => {
        let img = document.createElement('img');
        img.src = imgs[key].img;

        if (i == 0) {
            img.className = 'scaleOutToLeft';
            img.id = 'carouselLeft';
        } else if (i == 1) {
            img.className = 'carouselSelected';
            img.id = 'carouselCenter';
        } else if (i == 2) {
            img.className = 'scaleOutToRight';
            img.id = 'carouselRight';
        } else stack = [img, ...stack]

        imgs[key].elem = img;
        carousel.appendChild(img);
    });

    addCarouselInteractions();
}

let stack = [];

function addCarouselInteractions() {
    Object.keys(imgs).forEach((key) => {
        let elem = imgs[key].elem;

        elem.addEventListener('click', () => {
            //Which side did the uer click on?
            let from = '';

            //This is the element currently in the middle of the carousel
            let cs = document.getElementById('carouselCenter');

            //If the image from the left is clicked
            if (elem.id == 'carouselLeft') {
                //Aimate the image to scale in from the left hand side to the middle
                elem.className = 'scaleInFromLeft';

                //set 'from' to left since the user clicked on the left most img
                from = 'left';
            }

            //If the image from the right is clicked
            if (elem.id == 'carouselRight') {
                //Aimate the image to scale in from the right hand side to the middle
                elem.className = 'scaleInFromRight';

                //set 'from' to right since the user clicked on the right most img
                from = 'right';
            }

            //The image that just got clicked is now in the middle
            elem.id = 'carouselCenter';

            let left = document.getElementById('carouselLeft'), // Gets the left most image
                right = document.getElementById('carouselRight'); // Gets the right most image

            //Move the center image in the correct direction
            switch (from) {
                case 'left': //move the img to the right
                    if (right) {
                        right.id = '';
                        right.className = 'moveCenterFromRight';
                        stack = [...stack, right];
                    }

                    cs.id = 'carouselRight';
                    cs.className = 'scaleOutToRight';
                    left = document.getElementById('carouselLeft');

                    if (!left) {
                        stack[0].className = 'moveLeftFromCenter';
                        stack[0].id = 'carouselLeft';
                        stack.shift();
                    }
                    break;

                case 'right': // move the img to the left
                    if (left) {
                        left.id = '';
                        left.className = 'moveCenterFromLeft';
                        stack = [left, ...stack];
                    }

                    cs.id = 'carouselLeft';
                    cs.className = 'scaleOutToLeft';
                    right = document.getElementById('carouselRight');

                    if (!right) {
                        stack[stack.length - 1].className = 'moveRightFromCenter';
                        stack[stack.length - 1].id = 'carouselRight';
                        stack.pop();
                    }
                    break;
            }
        });
    });
}