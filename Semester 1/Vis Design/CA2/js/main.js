const pages = {
    'home': './index.html',
    'ui/ux': './uxui.html'
}

let stack = [],
    currentPageName,
    scroll,
    height;

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
                hamburgerContent.className = 'hamburgerContentVisible';
                document.documentElement.className = 'htmlStopScroll';
                navLogo.className = 'logoColorMenuOpen';
                break;

            case false:
                hamburgerContent.className = 'hamburgerContentInvisible';
                document.documentElement.className = '';
                navLogo.className = 'logoColorMenuClosed';
                break;
        }
    });
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
        li.class = key;

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
        loaded = false,
        notScrolledFor = 0;

    while (true) {
        // Get the current scroll position  
        scroll = document.scrollingElement.scrollTop; // Scroll top dosent work on mobile?
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

        if (currentPage == 1 && !loaded) {
            await sleep(100);
            addCarouselItems();
            loaded = true;
        }

        prevPos = scroll;
    }
}

const imgs = {
    '0': {
        img: './imgs/aboutus/1.jpg',
        elem: undefined,
        name: 'Greg',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
    '1': {
        img: './imgs/aboutus/2.jpg',
        elem: undefined,
        name: 'Grzegorz',
        bio: 'Hey, my name is Grzegorz Maniak, I\'m studying computing at TU Tallaght campus, I have a great interest in web and software development, I also enjoy the outdoors, I love to travel, camp and hike.'
    },
    '2': {
        img: './imgs/aboutus/3.jpg',
        elem: undefined,
        name: 'Gregor',
        bio: 'My name is Moyin Olusona. I am 17 years old and am in my first year of college. I went to St. Louis High school. My favourite subjects were English and Geography. I like to read and watch tv and movies.'
    },
    '3': {
        img: './imgs/aboutus/4.jpg',
        elem: undefined,
        name: 'Gorg',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
}

//Carousel
function addCarouselItems() {
    let carousel = document.getElementById('carousel');
    carousel.className = 'carouselVisable';

    Object.keys(imgs).forEach((key, i) => {
        //create the parent element for this img, heading and bio
        let div = document.createElement('div');

        //add text to the div
        div.innerHTML = `<h2 class='carouselText'>${imgs[key].name}</h2><img class='carouselImg' src="${imgs[key].img}" alt="${imgs[key].name}"><p class='carouselText'>${imgs[key].bio}</p>`;

        //give the div a name
        div.name = key;

        switch (i) {
            case 0: // Image on the left hand side
                div.className = 'scaleOutToLeft';
                div.id = 'carouselLeft';
                break;

            case 1: // Image in the middle
                div.className = 'carouselSelected';
                div.id = 'carouselCenter';
                div.getElementsByTagName('img')[0].useMap = '#aboutus';
                break;

            case 2: // Image on the right hand side
                div.className = 'scaleOutToRight';
                div.id = 'carouselRight';
                break;

            default:
                // Since this image wont be seen, add it to the stack
                stack = [div, ...stack];
                // and make it invisable
                div.className = 'invisible';
                break;
        }

        imgs[key].elem = div;
        carousel.appendChild(div);

        div.addEventListener('click', () => {
            carouselScroll(div);
        });
    });
}

function carouselScroll(elem) {
    //Which side did the uer click on?
    let from = '';

    //This is the element currently in the middle of the carousel
    let cs = document.getElementById('carouselCenter');
    cs.getElementsByTagName('img')[0].useMap = '';

    //If the image from the left is clicked
    if (elem.id == 'carouselLeft') {
        //Aimate the image to scale in from the left hand side to the middle
        elem.className = 'scaleInFromLeft';

        //set 'from' to left since the user clicked on the left most img
        from = 'Left';
    }

    //If the image from the right is clicked
    if (elem.id == 'carouselRight') {
        //Aimate the image to scale in from the right hand side to the middle
        elem.className = 'scaleInFromRight';

        //set 'from' to right since the user clicked on the right most img
        from = 'Right';
    }

    //The image that just got clicked is now in the middle
    elem.id = 'carouselCenter';
    elem.getElementsByTagName('img')[0].useMap = '#aboutus';

    let left = document.getElementById('carouselLeft'), // Gets the left most image
        right = document.getElementById('carouselRight'); // Gets the right most image

    //Move the center image in the correct direction
    switch (from) {
        case 'Left': //move the img to the right
            //If theres an image to the right, move it behind the center
            if (right) {
                right.id = '';
                right.className = 'moveCenterFromRight'; //animate the move
                stack = [...stack, right]; //add the img to the stack
            }

            if (!document.getElementById('carouselLeft')) {
                stack[0].className = 'moveLeftFromCenter'; //animate the move
                stack[0].id = 'carouselLeft'; //lable the imgs position
                stack.shift(); //remove the img from the stack
            }

            cs.id = 'carouselRight'; //lable the imgs position
            cs.className = 'scaleOutToRight'; //animate the move

            return;

        case 'Right': // move the img to the left
            //If theres an image to the left, move it behind the center
            if (left) {
                left.id = '';
                left.className = 'moveCenterFromLeft'; //animate the move
                stack = [left, ...stack]; //add the img to the stack
            }

            if (!document.getElementById('carouselRight')) {
                stack[stack.length - 1].className = 'moveRightFromCenter'; //animate the move
                stack[stack.length - 1].id = 'carouselRight'; //lable the imgs position
                stack.pop(); //remove the img from the stack
            }

            cs.id = 'carouselLeft'; //lable the imgs position
            cs.className = 'scaleOutToLeft'; //animate the move

            return;
    }
}

function carousel(side) {
    switch (side) {
        case 'left':
            return carouselScroll(document.getElementById('carouselLeft'));

        case 'right':
            return carouselScroll(document.getElementById('carouselRight'));
    }
}